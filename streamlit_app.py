import openai
import streamlit as st

# Initialize the OpenAI API client
openai.api_key = "<your OpenAI API key>"

# Create a text input field for the user to enter the keyword
keyword = st.text_input("Enter the keyword to generate viral social media posts:")

# Use the GPT-3 API to generate the social media posts
model_engine = "text-davinci-002"
prompt = (f"generate 20 viral social media posts about {keyword}")

completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Extract the generated social media posts from the API response
posts = completions.choices[0].text

# Display the generated social media posts in the Streamlit app
st.write("Viral Social Media Posts:", posts)
