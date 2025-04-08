import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

TIME_ZONE = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Shanghai",
    "America/Chicago",
    "Asia/Kolkata",
    "Europe/Paris",
    "America/Toronto",
    "Asia/Singapore",
    "Europe/Moscow",
    "Asia/Dubai",
    "Asia/Seoul",
]

st.title("Time Zone APP")

selected_timezone = st.multiselect("Select Time Zones", TIME_ZONE, default=["UTC", "Asia/Karachi"])

st.subheader("Selected Timezones")

for tz in selected_timezone:

    curreent_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I %H:%M:%S %p" )
    st.write(f"**{tz}**: is {curreent_time}")

st.subheader("Convert time b/w timezones")
curreent_time = st.time_input("Current Time", value=datetime.now().time())

from_tz = st.selectbox("From Timezone", TIME_ZONE, index=0)
to_tz = st.selectbox("To Timezone", TIME_ZONE, index=1)

if st.button("Convert time"):

    dt = datetime.combine(datetime.today(), curreent_time, tzinfo=ZoneInfo(from_tz))

    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")

    st.success(f"Converted time {to_tz} : {converted_time}") 