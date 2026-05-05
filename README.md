# Student Habits & Performance: Interactive Dashboard & Grade Simulator

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

Welcome to Version 2.0 of my Data Analytics project!

In my previous version, I used static charts to answer: **What actually makes a good student?** Now, I decided to take it to the next level by transforming that analysis into a **fully interactive web application** with a predictive Machine Learning model running under the hood.

To make this happen, I used **Python (Pandas, Streamlit, Plotly, and Scikit-Learn)** to bring the data to life.

### What I Built

Instead of just looking at past data, this project now allows users to interact with the charts and even predict future outcomes based on custom inputs.

Here is what the application covers:
- **Interactive Analytics:** Dynamic tabs exploring correlation heatmaps, the impact of study vs. social media, and violin plots showing how physical and mental health affect academic success. Hover over the charts to see the exact data points!
- **The Grade Simulator:** A sidebar powered by a **Linear Regression** model. You can adjust sliders for your own study hours, social media usage, and mental health level, and the algorithm will predict your final exam score in real-time, providing color-coded feedback!

---

## Live Demo
**[Click here to access the live web app!](https://students-dashboard-v2-jopsico.streamlit.app/)**

## The Dashboard
<img width="1896" height="914" alt="image" src="https://github.com/user-attachments/assets/f9515f10-d264-448d-adce-8496241b13db" />

## Want to run it yourself?

If you want to poke around the code or run the application on your local machine, it's super easy to set up.

1. Make sure you have Python installed.
2. Install the required libraries:
   ```bash
   py -m pip install streamlit pandas plotly scikit-learn
3. Clone this repo, open the folder in your terminal, and run the Streamlit server:
   ```bash
   py -m streamlit run app.py
