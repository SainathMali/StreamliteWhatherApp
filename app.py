import streamlit as st
import requests

API_KEY = st.secrets["API_KEY"]

st.set_page_config(page_title="WeatherApp", page_icon="🌤️")
st.title("🌤️ WeatherApp")

city = st.text_input("🔍 Enter city name")

if st.button("Get Weather"):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    data = requests.get(url).json()

    if data["cod"] != 200:
        st.error("❌ City not found")
    else:
        # Weather logo from OpenWeather (changes with sun, rain, clouds...)
        icon = data["weather"][0]["icon"]
        st.image(f"https://openweathermap.org/img/wn/{icon}@2x.png", width=100)

        st.subheader(f"📍 {data['name']}, {data['sys']['country']}")
        st.write(f"☁️ {data['weather'][0]['description'].title()}")

        col1, col2 = st.columns(2)
        col1.metric("🌡️ Temperature", f"{data['main']['temp']} °C")
        col2.metric("💧 Humidity", f"{data['main']['humidity']} %")

        col3, col4 = st.columns(2)
        col3.metric("💨 Wind Speed", f"{data['wind']['speed']} m/s")
        col4.metric("🌍 Country", data["sys"]["country"])