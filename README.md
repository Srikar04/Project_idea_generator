# Project Idea Suggester and Trending Technologies

This project is a **Generative AI** web application that provides project ideas based on user input and displays trending technologies. It demonstrates the usage of Agentic AI, which autonomously generates project ideas based on user input. The application leverages the PhiData API for creating agents and uses the llama-3.3-70b-versatile freely available in Groq playground and Github and Wikipedia agent tools available in phidata

## Features

- **Project Idea Suggester**: Enter your preferred technologies and skill level to get project ideas.
- **Trending Technologies**: View the top 5 trending technologies and languages currently being used by computer scientists.

## Screenshots

![](/images/1.png)
![](/images/2.png)

## Technologies Used

- **Streamlit**: For building the web application.
- **Python**: The programming language used for the backend.
- **Phidata**: For creating and managing agents.
- **dotenv**: For managing environment variables.

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Srikar04/Project_idea_generator.git
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages**:
    ```bash
    pip install streamlit dotenv wikipedia phidata PyGithub
    ```

4. **Create a `.env` file**:
    ```bash
    touch .env
    ```

5. **Add your API keys to the `.env` file**:
    ```
    GROQ_API_KEY=your_groq_api_key
    GITHUB_ACCESS_TOKEN=your_github_access_token
    ```

6. **Run the application**:
    ```bash
    streamlit run  main.py
    ```

## Usage

- **Project Idea Suggester**:
    1. Enter the technologies you are interested in (comma-separated).
    2. Select your skill level.
    3. Click on "Get Project Ideas" to see the suggestions.

- **Trending Technologies**:
    1. Navigate to the "Trending Technologies" page using the sidebar.
    2. View the top 5 trending technologies and languages.
    3. Click on "Reload Trending Technologies" to refresh the data.

## Note

The results are generated using the LLama 3.3 model which is open source in Groq playground and may vary from request to request. They may also take some time to load.


## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [GROQ Model](https://groq.com/)
- [dotenv](https://pypi.org/project/python-dotenv/)