import streamlit as st
import datetime
import google.generativeai as genai
from google.generativeai import types


st.title("Your Favourite Travel Companion!")
st.write("Welcome to the ultimate travel companion app. Here, you can find tips, recommendations, and tools to make your travel experience unforgettable!")

td = st.date_input("Select your travel date", datetime.date.today())
st.write("Your selected travel date is:", td)
d = st.date_input("Select your return date", datetime.date.today())
st.write("Your selected return date is:", d)
title = st.text_input("Enter your travel destination", "Paris")
st.write("Your travel destination is:", title)
special_requests = st.text_input("Enter any special requests or preferences", "Include christmas markets, local cuisine")
if st.button("Generate travel itinerary..."):
    st.write(f"Generating travel itinerary for {title}...")
    # Here you would add the logic to generate the itinerary
    st.write(f"Your itinerary for {title} is ready!")
    prompt = """Create a detailed travel itinerary for a trip to {title}  from {td} to {d} including activities, dining options, and sightseeing spots based on the following special requests: {special_requests}.  itimerary to go to melbourne. Also reccommend tips and packing list, including which day should go to which attraction. Dont ask customers for extra info work with what you have)
 do not mention special requests. Make it fun and engaging."""

    client = genai.Client(api_key=st.secrets["genai_key"])
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt)
    with st.spinner("Generating your personalized travel itinerary..."):
        st.write(response.text)
        st.write("Thank you for using the travel companion app. Safe travels!")