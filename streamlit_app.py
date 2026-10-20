import streamlit as st
from datetime import time, datetime

st.header('st.slider')

# Example 1
st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I am ", age, "years old")


# Example 2
st.subheader('Range slider')

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

st.write("Values: ", values, values[1] - values[0])


# Example 3
st.subheader('Range Time slider')

appointment = st.slider(
    'Schedule your appointment',
    value = (time(11,30), time(12,45)))

st.write("Appointment", appointment[0], " - ", appointment[1])


# Example 4
st.subheader('Datetime slider')
start_time = st.slider(
    "When do you start?",
    value = datetime(2020, 1,1,9, 30), 
    format = ("MM/DD/YY - hh:mm")
)

st.write("Start time: ", start_time)

# Example 5

color = st.select_slider(
    "Select a color of the rainbow",
    options = [
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet",
    ]
)

st.write("My Favourite color is ", color)