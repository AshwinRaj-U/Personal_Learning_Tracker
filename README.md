# 📘 Yearly Learning Tracker

A Streamlit app to track daily study sessions, visualize progress, and measure consistency.  
This project integrates with **Google Sheets** as a backend to store session data, making it lightweight, cloud‑friendly, and easy to maintain.

## 🚀 Features
- **Start/Stop study sessions** with a single click.
- **Automatic duration calculation** (in minutes).
- **Google Sheets integration** for persistent storage.
- **Daily gap filling**: ensures missing days are logged with `0` minutes.
- **Interactive dashboard**:
  - Line chart of daily learning hours.
  - Consistency percentage metric (days studied ÷ total days).
- **Simple UI** built with Streamlit.


## 🛠️ Tech Stack
- [Streamlit](https://streamlit.io/) – UI framework
- [Pandas](https://pandas.pydata.org/) – data manipulation
- [Plotly Express](https://plotly.com/python/plotly-express/) – interactive charts
- [gspread](https://github.com/burnash/gspread) – Google Sheets API client
- [oauth2client](https://github.com/googleapis/oauth2client) – service account authentication


## 📂 Project Structure
```
personal_learning_tracker/
│
├── app.py              # Main Streamlit app
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/personal_learning_tracker.git
cd personal_learning_tracker
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Google Sheets
- Create a Google Cloud project and enable the **Google Sheets API** + **Google Drive API**.
- Generate a **Service Account** and download the JSON key.
- Add the JSON key to your Streamlit secrets (`.streamlit/secrets.toml`):
  ```toml
  [gcp_service_account]
  type = "service_account"
  project_id = "your-project-id"
  private_key_id = "..."
  private_key = "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
  client_email = "your-service-account@project-id.iam.gserviceaccount.com"
  client_id = "..."
  ```
- Share your Google Sheet (`Learning_Tracker_2026`) with the service account email.

### 4. Run locally
```bash
streamlit run app.py
```

### 5. Deploy on Streamlit Cloud
- Push your repo to GitHub.
- Go to [Streamlit Cloud](https://streamlit.io/cloud) and deploy the app.
- Set secrets in the Streamlit Cloud dashboard under **App Settings → Secrets**.

---

## 📊 Usage
1. Click **Start session** to begin tracking.
2. Click **Stop session** to log study time into Google Sheets.
3. View your progress in the dashboard:
   - Line chart of hours studied.
   - Consistency percentage.

---

## 🔮 Future Improvements
- Add weekly/monthly summary charts.
- Export data to CSV.
- Add notifications/reminders.
- Support multiple users with separate sheets.

---

