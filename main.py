"""
Weather Forecast Application

A Streamlit web application that displays weather forecasts for a specified location.
Uses Plotly for data visualization.
"""

import streamlit as st
import plotly.express as px

# Set page configuration
st.title("Weather Forecast for the Next Days")

# User input section
place = st.text_input("Place:", help="Enter the name of the city or location")
days = st.slider(
    "Forecast Days",  # Fixed typo in "Forecast"
    min_value=1,
    max_value=5,
    value=1,  # Add default value
    help="Select the number of forecasted days",
)

# Data selection
option = st.selectbox(
    "Select data to view",
    options=("Temperature", "Sky"),
    help="Choose the type of weather data to display",
)

# Validate input
if not place:
    st.warning("Please enter a location to get the forecast.")
else:
    st.subheader(f"{option} for the next {days} days in {place}")

    # Create and display the plot
    # Note: Current figure is empty - needs data source
    figure = px.line(title=f"{option} Forecast", labels={"x": "Date", "y": option})
    st.plotly_chart(figure, use_container_width=True)
