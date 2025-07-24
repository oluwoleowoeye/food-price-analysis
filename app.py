
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide") # Optional: Use wide layout

st.title("Food Price Anomaly Analysis Report")

st.markdown("""
This application presents an analysis of the Food Price Anomaly Indicator (IFPA).
""")

# --- Data Loading and Preparation ---
@st.cache_data
def load_data(file_path):
    excel_file = pd.ExcelFile(file_path)
    sheet_name = excel_file.sheet_names[0]
    df = excel_file.parse(sheet_name)
    df['TimePeriod'] = pd.to_numeric(df['TimePeriod'])
    return df

# Load the data
data_path = 'cleaned_food_price_data.xlsx' # Make sure this file is accessible to the Streamlit app
df_github = load_data(data_path)

st.header("Data Overview")
st.write("First 5 rows of the data:")
st.write(df_github.head())

st.write("Column Information:")
st.write(df_github.info())

# --- Overall Trends Visualization ---
st.header("Overall Trends in Food Price Anomalies")

st.markdown("The following time series plot shows the overall trend of the Food Price Anomaly Indicator across all available data.")

# Overall Time Series Plot
fig1, ax1 = plt.subplots(figsize=(12, 6))
sns.lineplot(data=df_github, x='TimePeriod', y='Value', ax=ax1)
ax1.set_title('Time Series of Food Price Anomaly Indicator (IFPA)')
ax1.set_xlabel('Time Period')
ax1.set_ylabel('Value (IFPA)')
ax1.grid(True)
st.pyplot(fig1)

# --- Regional/Country Comparisons and Anomalies ---
st.header("Regional/Country Comparisons and Anomalies")

st.markdown("To understand variations in food price anomalies, we compare the IFPA trends for a selection of countries. The plot below shows the time series for these countries, with highlighted points indicating anomalies (IFPA >= 1).")

# Get unique countries for selectbox
unique_countries = df_github['GeoAreaName'].unique().tolist()

# Add a selectbox for country selection (optional: start with a default selection)
selected_countries = st.multiselect(
    "Select countries for comparison:",
    options=unique_countries,
    default=['Nigeria', 'Kenya', 'Angola', 'Uganda'] # Default selection
)

# Filter the DataFrame for the selected countries
if selected_countries:
    df_compare = df_github[df_github['GeoAreaName'].isin(selected_countries)].copy()

    # Identify anomalies where Value (IFPA) is >= 1
    anomalies_compare = df_compare[df_compare['Value'] >= 1].copy()

    # Country Comparison Plot with Anomalies
    fig2, ax2 = plt.subplots(figsize=(14, 7))
    sns.lineplot(data=df_compare, x='TimePeriod', y='Value', hue='GeoAreaName', marker='o', markersize=5, linestyle='-', ax=ax2)
    sns.scatterplot(data=anomalies_compare, x='TimePeriod', y='Value', hue='GeoAreaName', color='red', marker='X', s=100, legend=False, ax=ax2)

    ax2.set_title('Food Price Anomaly Indicator (IFPA) Time Series Comparison with Anomalies')
    ax2.set_xlabel('Time Period')
    ax2.set_ylabel('Value (IFPA)')
    ax2.grid(True)
    ax2.legend(title='Country')
    st.pyplot(fig2)
else:
    st.info("Please select at least one country for comparison.")


# --- Key Anomalies Table ---
st.header("Key Anomalies")

st.markdown("The table below lists the specific instances across all data where the IFPA was 1 or greater.")

# Identify anomalies where Value (IFPA) is >= 1 across all data
anomalies_all = df_github[df_github['Value'] >= 1].copy()

st.write(anomalies_all)


# --- Conclusions and Recommendations (from previous analysis) ---
st.header("Conclusions and Recommendations")

st.markdown("""
Based on the analysis conducted, here are some key conclusions and recommendations for policymakers:

**Conclusions:**

*   **Overall Trend:** The Food Price Anomaly Indicator (IFPA) shows variability over time, with certain periods exhibiting higher levels of food price anomalies across the dataset.
*   **Regional Differences and Hotspots:** The comparison of selected countries demonstrates that the experience of food price anomalies varies significantly by region, with some countries facing more frequent or intense volatility.
*   **Anomaly Identification:** Specific instances where the IFPA reached or exceeded the threshold for abnormal price levels (IFPA >= 1) were identified, highlighting periods and locations of potential food price shocks.
*   **Limited Basic Predictability:** A basic predictive model using only the previous year's IFPA value showed limited predictive power, suggesting that multiple complex factors influence food price anomalies.

**Recommendations for Policymakers:**

*   **Targeted Monitoring:** Prioritize targeted monitoring of food price indicators in countries and regions historically vulnerable to high volatility.
*   **Early Warning Systems:** Strengthen or develop early warning systems incorporating the IFPA to detect potential food price shocks early.
*   **Investigate Drivers of Anomalies:** Conduct further analysis to understand the underlying causes of significant food price anomalies in identified hotspots.
*   **Support Vulnerable Populations:** Develop and strengthen social safety nets and food security programs during periods of high food price anomalies.
*   **Diversify Food Sources and Markets:** Encourage diversification of domestic food production and reduce reliance on volatile international markets.
*   **Improve Data Collection and Analysis:** Continue investing in robust data collection and explore more sophisticated analytical techniques for better prediction.
""")

