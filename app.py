import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression

# Configuração da página
st.set_page_config(page_title="Dashboard Estudantil", page_icon="📊​", layout="wide")

# Título do dashboard
st.title("Impacto dos Hábitos no Desempenho Estudantil")
st.markdown("Este dashboard apresenta uma análise dos hábitos dos estudantes e seu impacto no desempenho acadêmico. Explore os dados abaixo.")

# Carregar os dados
@st.cache_data
def load_data():
    data = pd.read_csv("student_habits_performance.csv")
    return data
data = load_data()

# Indicadores principais (KPIs)
col1, col2, col3 = st.columns(3)

media_nota = round(data['exam_score'].mean(), 1)
media_estudo = round(data['study_hours_per_day'].mean(), 1)
media_saude_mental = round(data['mental_health_rating'].mean(), 1)

# Inserindo os dados nas colunas
with col1:
    st.metric(label="Média de Notas", value=f"{media_nota}/100")
with col2:
    st.metric(label="Média de Horas de Estudo", value=f"{media_estudo} horas/dia")
with col3:
    st.metric(label="Nível de Saúde Mental", value=f"{media_saude_mental}/10")

st.divider()

#  Abas
st.subheader("Mergulho nos dados")
aba1, aba2, aba3 = st.tabs(["O Peso do Esforço", "Dreno de Tempo", "Corpo e Mente"])

# Aba 1: O Peso do Esforço
with aba1:
    st.markdown("### Mais estudo = Mais nota?")
    st.markdown("Veja a relação direta entre o tempo de estudo e o resultado final. Passe o mouse sobre os pontos para detalhes.")

# Criando o gráfico interativo com Plotly
    fig_estudo = px.scatter(
        data,
        x='study_hours_per_day',
        y='exam_score',
        color="mental_health_rating",
        color_continuous_scale="Viridis",
        labels={
            'study_hours_per_day': 'Horas de Estudo por Dia',
            'exam_score': 'Nota do Exame',
            'mental_health_rating': 'Nível de Saúde Mental'
        },
    )

    # Exibindo o gráfico no Streamlit para ocupar a largura toda
    st.plotly_chart(fig_estudo, use_container_width=True)

# Aba 2: Dreno de Tempo
with aba2:
    st.markdown("### A Armadilha das Telas")
    st.markdown("Veja como o tempo gasto em redes sociais impacta a distribuição das notas")

    fig_social = px.box(
        data,
        x='social_media_hours',
        y='exam_score',
        color="social_media_hours",
        labels={
            'social_media_hours': 'Horas em Redes Sociais',
            'exam_score': 'Nota do Exame'
        },
    )
    st.plotly_chart(fig_social, use_container_width=True)

# Aba 3: Corpo e Mente
with aba3:
    st.markdown("### O Equilíbrio entre Corpo e Mente")
    st.markdown("Veja como a saúde física afeta o desempenho acadêmico")

    fig_social = px.violin(
        data,
        x='diet_quality',
        y='exam_score',
        color="diet_quality",
        labels={
            'diet_quality': 'Qualidade da Dieta',
            'exam_score': 'Nota do Exame'
        },
    )
    st.plotly_chart(fig_social, use_container_width=True)

# Simulador Interativo
st.sidebar.header("Simulador de Notas")
st.sidebar.markdown("Ajuste sua rotina abaixo e veja a previsão da sua nota:")

horas_estudo = st.sidebar.slider("Horas de estudo por dia", 0, 24, 5)
horas_redes = st.sidebar.slider("Horas em Redes Sociais", 0, 24, 3)
saude_mental = st.sidebar.slider("Nível de Saúde Mental", 1, 10, 5)

# Separando Causa de Efeito para o modelo de regressão
X = data[['study_hours_per_day', 'social_media_hours', 'mental_health_rating']]
y = data['exam_score']

# Criando e treinando o modelo
model = LinearRegression()
model.fit(X, y)

# Empacotando as escolhas do usuário no mesmo fortato
entrada_usuario = pd.DataFrame({
    'study_hours_per_day': [horas_estudo],
    'social_media_hours': [horas_redes],
    'mental_health_rating': [saude_mental]
})

# Fazendo a previsão
nota_prevista = model.predict(entrada_usuario)[0]

# Exibindo o resultado
st.sidebar.divider()
st.sidebar.markdown("### Resultado Previsto")
st.sidebar.metric(label="Nota Prevista", value=f"{round(nota_prevista, 1)}/100")

# Feedback visual
if nota_prevista >= 70:
    st.sidebar.success("Excelente! Continue assim!")
elif nota_prevista >= 50:
    st.sidebar.warning("Bom, mas pode melhorar.")
else:
    st.sidebar.error("Precisa melhorar. Vamos focar nos estudos!")