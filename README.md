# 🌧️ Rain Alert System (Python + SMS)

> A simple Python project that checks upcoming weather using the **OpenWeather One Call API** and alerts you via **Twilio SMS** if rain is expected.

---

## 🚀 About the Project

This script:
1. Fetches **hourly forecast data** (next 12 hours) from OpenWeather’s One Call API.
2. Checks the **weather condition codes** to detect rain/cloud events.
3. Sends an **SMS alert** using Twilio if rain is predicted.

It’s a beginner-friendly **cyber-automation project** mixing APIs, Python requests, and SMS notifications.

---

## 🛠️ Requirements

- Python 3.8+
- [OpenWeather One Call API key](https://openweathermap.org/api/one-call-api)
- [Twilio account](https://www.twilio.com/) with:
  - `ACCOUNT_SID`
  - `AUTH_TOKEN`
  - Twilio phone number

---

## 📦 Installation

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/rain-alert.git
   cd rain-alert

Create virtual environment (recommended):

python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate


Install dependencies:

pip install requests twilio
