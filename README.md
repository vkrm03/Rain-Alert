# 🌧️ Rain Alert System (Python + SMS)

This Python script uses **OpenWeather One Call API** to check the next 12 hours of forecast and sends an **SMS alert via Twilio** if rain is predicted. Perfect for personal automation projects.

## ⚙️ Setup
1. Get an [OpenWeather API key](https://openweathermap.org/api/one-call-api).  
2. Create a [Twilio account](https://www.twilio.com/) and get `ACCOUNT_SID`, `AUTH_TOKEN`, and a Twilio number.  
3. Install deps:
   ```bash
   pip install requests twilio
