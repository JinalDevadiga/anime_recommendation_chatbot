# Anime Recommender Chatbot

## Table of Contents

- [Anime Recommender Chatbot](#anime-recommender-chatbot)
  - [Overview](#overview)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
  - [Usage](#usage)
  - [Project Structure](#project-structure)
  - [References](#references)


## Overview

This project implements a simple chatbot using Flask and the OpenAI GPT-3.5-turbo model. The chatbot has knowledge about different genres of anime with their ratings and can suggest anime based on the provided genre. Users can interact with the chatbot by asking questions related to anime genres.

## Prerequisites

Ensure you have the following requirements installed:

- Flask
- openai

You can install them using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Setup

1. Obtain an OpenAI API key and replace 'Enter your API key' with your actual API key in the `app.py` file.

2. Run the Flask application:

   ```bash
   flask --app app run
   ```
3. Access the chatbot interface by opening a web browser and navigating to http://127.0.0.1:5000/

## Usage

- Upon accessing the chatbot interface, you will see a chat container with a system message explaining the bot's capabilities.
- Enter your questions related to anime genres in the input field and click "Submit" or press Enter to get recommendations.
- The chatbot will respond with anime suggestions based on the input.

## Project Structure

- **app.py:** Contains the Flask application code with routes for the home page and anime recommendation. It interacts with the OpenAI GPT-3.5-turbo model to generate responses.

- **index.html:** The HTML template for the chatbot interface. It includes styles and JavaScript for handling user input and bot responses.

- **requirements.txt:** Lists the Python packages required for running the application.


## References

- Flask Documentation: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- OpenAI API Documentation: [https://beta.openai.com/docs/](https://beta.openai.com/docs/)
- Bootstrap Documentation: [https://getbootstrap.com/docs/5.3/getting-started/introduction/](https://getbootstrap.com/docs/5.3/getting-started/introduction/)



