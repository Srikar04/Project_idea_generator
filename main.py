import streamlit as st
from dotenv import load_dotenv
from agent import get_project_ideas

load_dotenv()

def project_idea_generator():
    st.title("Project Idea Suggester")
    st.write("Enter your preferred technologies and skill level to get project ideas!")

    technologies = st.text_input("Technologies (comma-separated)", placeholder="e.g., Python, React, TensorFlow")
    level = st.selectbox("Skill Level", ["Tutorial", "Beginner", "Intermediate", "Expert"])

    if st.button("Get Project Ideas"):
        ideas = get_project_ideas(technologies, level)
        st.write(ideas)

def trending_technologies():
    st.title("Trending Technologies")
    st.write("Search for trending technologies and view graphs.")

if "page" not in st.session_state:
    st.session_state.page = "Trending Technologies"

st.sidebar.title("Navigation")
if st.sidebar.button("Trending Technologies"):
    st.session_state.page = "Trending Technologies"
if st.sidebar.button("Project Idea Generator"):
    st.session_state.page = "Project Idea Generator"

# Page selection
if st.session_state.page == "Project Idea Generator":
    project_idea_generator()
elif st.session_state.page == "Trending Technologies":
    trending_technologies()