import requests
import os

API_KEY = os.environ.get("OPENWEATHER_API_KEY")


def get_data(place, forecast_days: int = 5, kind="Temperature"):
    """
    Fetch and process weather forecast data from OpenWeatherMap API.

    Args:
        place (str): Name of the city/location to get weather data for
        forecast_days (int, optional): Number of days to forecast. Defaults to 5.
        kind (str, optional): Type of data to return - either "Temperature" or "Sky". Defaults to "Temperature".

    Returns:
        list: Filtered weather data based on the specified kind:
            - For Temperature: List of temperature values
            - For Sky: List of weather condition descriptions
    """
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url, params={"units": "metric"}).json()
    filtered_data = response["list"][: 8 * forecast_days]

    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, kind="Sky"))
