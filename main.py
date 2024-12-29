import streamlit as st
from dotenv import load_dotenv
from agent import get_project_ideas,get_trending_technologies

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
    st.write("Here are the top 5 trending technologies and languages currently being used by computer scientists.")
    with st.spinner("Fetching data..."):
        info = get_trending_technologies()
    st.write(info)

if "page" not in st.session_state:
    st.session_state.page = "Trending Technologies"

st.sidebar.title("Navigation")
if st.sidebar.button("Trending Technologies"):
    st.session_state.page = "Trending Technologies"
if st.sidebar.button("Project Idea Generator"):
    st.session_state.page = "Project Idea Generator"

st.write("Note: The results are generated using the GROQ model and may vary from request to another. They may also take to load")
# Page selection
if st.session_state.page == "Project Idea Generator":
    project_idea_generator()
elif st.session_state.page == "Trending Technologies":
    trending_technologies()