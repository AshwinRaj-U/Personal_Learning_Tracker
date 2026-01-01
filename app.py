import streamlit as st
import pandas as pd
import datetime as dt
import time
import plotly.express as px
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Connect to Google Sheets
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(
    st.secrets["gcp_service_account"], scope
)
client = gspread.authorize(creds)
sheet = client.open("Learning_Tracker_2026").sheet1

# Session state
if "session_active" not in st.session_state:
    st.session_state.session_active = False
if "start_ts" not in st.session_state:
    st.session_state.start_ts = None

def start_session():
    st.session_state.session_active = True
    st.session_state.start_ts = time.time()
    st.info("✅ Study session started")

def stop_session():
    end_ts = time.time()
    duration_minutes = int((end_ts - st.session_state.start_ts) / 60.0)
    if duration_minutes <= 0:
        duration_minutes = 1
    today = dt.date.today().isoformat()

    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    if df.empty:
        df = pd.DataFrame(columns=["session_date", "duration_minutes"])

    if not df.empty:
        last_date = pd.to_datetime(df["session_date"]).max().date()
        gap_days = (dt.date.today() - last_date).days
        for i in range(1, gap_days):
            gap_date = (last_date + dt.timedelta(days=i)).isoformat()
            if gap_date not in df["session_date"].values:
                sheet.append_row([gap_date, 0])

    if today in df["session_date"].values:
        idx = df[df["session_date"] == today].index[0] + 2
        current_val = int(sheet.cell(idx, 2).value)
        sheet.update_cell(idx, 2, current_val + duration_minutes)
    else:
        sheet.append_row([today, duration_minutes])

    st.session_state.session_active = False
    st.session_state.start_ts = None
    st.success(f"📘 Session saved: {today} (+{duration_minutes} min)")
    st.info(f"⏱ Study time: {duration_minutes} minutes")

# --- UI ---
st.title("📘 Yearly Learning Tracker")

# Dashboard
data = sheet.get_all_records()
df = pd.DataFrame(data)
if not df.empty:
    df["session_date"] = pd.to_datetime(df["session_date"]).dt.date.astype(str)
    df["hours"] = df["duration_minutes"] / 60.0
    fig = px.line(df, x="session_date", y="hours", title="Daily Learning Hours")
    fig.update_xaxes(title="Date", type="category")
    fig.update_yaxes(range=[0, df["hours"].max() + 1])
    st.plotly_chart(fig, use_container_width=True)

    total_days = (dt.date.today() - dt.date(dt.date.today().year, 1, 1)).days + 1
    learned_days = (df["duration_minutes"] > 0).sum()
    percent = round((learned_days / total_days) * 100, 2)
    st.metric("Consistency %", f"{percent}%")

# Buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Start session"):
        start_session()
with col2:
    if st.button("Stop session"):
        stop_session()