# food-price-analysis

Link to deployed app 
https://food-price-analysis-7sp4pzef6fxrhwp6e9da2f.streamlit.app/

# Goal: Analyze food price anomalies using the Food Price Anomaly Indicator (IFPA) data.
Data Source: Data was obtained from [https://unstats.un.org/sdgs/dataportal]
# Steps Performed:
Downloaded the Excel data file.
Loaded the data into a pandas DataFrame and explored its structure.
Created time series plots to visualize the overall trend of the IFPA and compare trends across selected countries.
Identified specific instances (anomalies) where the IFPA was high (>= 1).
Performed basic statistical analysis, including calculating correlations between numerical columns (finding low correlations with IFPA).
Built and evaluated a basic linear regression model to predict IFPA using a lagged value (which showed limited predictive power).
Structured the analysis findings into a dynamic report format.
Developed a Streamlit web application (app.py) to present the data, visualizations, and key findings interactively.
Created a requirements.txt file listing the necessary Python libraries for the Streamlit app.

# Outcome: A Streamlit web application that visually presents the food price anomaly analysis, ready to be deployed and shared.
Go to https://streamlit.io/cloud.
Log in and connect your GitHub account.
Click on "New app".
Select your GitHub repository and the app.py file as the main file.
Click "Deploy!".
Streamlit Cloud will then read your requirements.txt and deploy your application.


# Essentially, the project involved getting the data, analyzing it with visualizations and basic statistics, summarizing the findings, and then packaging it into an interactive web app using Streamlit for easier sharing and understanding by a wider audience, such as policymakers.

