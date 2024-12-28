import streamlit as st
from dotenv import load_dotenv
from agent import get_project_ideas

load_dotenv()

st.title("Project Idea Suggester")
st.write("Enter your preferred technologies and skill level to get project ideas!")

technologies = st.text_input("Technologies (comma-separated)", placeholder="e.g., Python, React, TensorFlow")
level = st.selectbox("Skill Level", ["Tutorial", "Beginner", "Intermediate", "Expert"])

if st.button("Get Project Ideas"):
    ideas = get_project_ideas(technologies, level)
    st.write(ideas)