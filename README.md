# 🌦️ Cloudy Aids — Weather App

<p align="center">
  <strong>Your Weather, Simplified.</strong>
</p>

<p align="center">
  A simple and interactive weather application built with Python and Streamlit.
</p>

<p align="center">
  <a href="https://cloudy-aids.streamlit.app/">
    🚀 Live Demo
  </a>
</p>

---

## 📌 About the Project

**Cloudy Aids** is a web-based weather application that allows users to check current weather conditions for a city of their choice. It fetches weather information from the OpenWeatherMap API and presents it through a clean, easy-to-use interface.

## ✨ Features

- 🌍 **City-Based Search** — Get weather information by entering a city name.
- 🌡️ **Temperature** — View the current temperature in Celsius.
- 💧 **Humidity** — Check the current humidity percentage.
- 💨 **Wind Speed** — View wind speed in meters per second.
- 🌤️ **Weather Conditions** — See a weather description and corresponding weather icon.
- 📍 **Location Details** — Display the city and country.
- ⚠️ **Error Handling** — Show an error message when a city cannot be found.
- 🔐 **Secure API Configuration** — Store API credentials using Streamlit secrets.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Web interface |
| OpenWeatherMap API | Weather data |
| Requests | HTTP API calls |
| Git & GitHub | Version control and source code hosting |
| Streamlit Community Cloud | Application deployment |

## 🚀 Live Demo

Try the application here:

👉 **[Open Cloudy Aids](https://cloudy-aids.streamlit.app/)**

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YOUR_REPOSITORY_NAME
```

Replace the placeholders with your actual GitHub repository URL and folder name.

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a file named `.streamlit/secrets.toml` in the project root:

```toml
OPENWEATHER_API_KEY = "your_api_key_here"
```

Replace the placeholder with your OpenWeatherMap API key.

Make sure `.streamlit/secrets.toml` is listed in `.gitignore`. Never commit your actual API key to GitHub.

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🔑 API Configuration

Cloudy Aids uses the OpenWeatherMap Current Weather API to retrieve weather information.

You can obtain an API key from:

[OpenWeatherMap](https://openweathermap.org/api)

Configure the key locally using Streamlit secrets. For deployment, add the same secret through your Streamlit Community Cloud app settings.

## 📁 Project Structure

```text
WeatherApp/
├── .streamlit/
│   └── secrets.toml
├── .gitignore
├── app.py
├── requirements.txt
└── README.md
```

**Note:** The `secrets.toml` file is for local development and should not be committed to GitHub.

## 🎯 Learning Outcomes

Through this project, I practiced:

- Building a web application using Python and Streamlit.
- Integrating a third-party REST API.
- Sending HTTP requests and handling JSON responses.
- Managing API credentials securely.
- Handling invalid user input and API errors.
- Deploying a Python application using Streamlit Community Cloud.
- Managing source code with Git and GitHub.

## 🔮 Future Improvements

- 📅 Add a multi-day weather forecast.
- 🌅 Display sunrise and sunset times.
- 🌍 Support recent searches and favorite cities.
- 📊 Add weather charts and additional weather metrics.
- 🎨 Improve the interface with dynamic weather themes.

## 🤝 Contributing

Suggestions and improvements are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request.

## 📜 License

This project is available for learning and personal use. Add a license file if you intend to distribute it under a specific open-source license.

---

<p align="center">
  🌦️ Built with Python, Streamlit, and OpenWeatherMap
</p>

<p align="center">
  ⭐ If you find this project useful, consider starring the repository!
</p>