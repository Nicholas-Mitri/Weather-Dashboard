"""
Weather Forecast Application

A Streamlit web application that displays weather forecasts for a specified location.
Uses Plotly for data visualization.
"""

import streamlit as st
import plotly.express as px
import backend

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
    st.subheader(f"{option} for the next {days} days in {place.title()}")

    data = backend.get_data(place, days, option)

    if option == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in data]
        dates = [dict["dt_txt"] for dict in data]
        # Create and display the plot
        figure = px.line(
            x=dates,
            y=temperatures,
            title=f"{option} Forecast",
            labels={"x": "Date", "y": option},
        )

        st.plotly_chart(figure, use_container_width=True)
    else:
        images = {
            "Clear": "images/clear.png",
            "Clouds": "images/cloud.png",
            "Rain": "images/rain.png",
            "Snow": "images/snow.png",
        }
        sky_conditions = [dict["weather"][0]["main"] for dict in data]
        image_paths = [images[condition] for condition in sky_conditions]
        st.image(image_paths, width=100)
