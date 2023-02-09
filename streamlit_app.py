import openai
import streamlit as st

# Initialize the OpenAI API client
openai.api_key = "<88>"
headers = {
    "Authorization": "Bearer {}".format(openai.api_key)
}

# Create a text input field for the user to enter the keyword for the viral social media posts
keyword_input = st.text_input("Enter a keyword for viral social media posts:")

# Use the GPT-3 API to generate 20 viral social media posts for the given keyword
model_engine = "text-davinci-002"
prompt = (f"generate 20 viral social media posts about {keyword_input}")

try:
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=20,
        stop=None,
        temperature=0.5,
    )
    # Extract the generated viral social media posts from the API response
    messages = [choice.text for choice in completions.choices]
    # Display the generated viral social media posts in the Streamlit app
    st.write("Viral Social Media Posts:")
    for message in messages:
        st.write("-", message)
except Exception as e:
    st.write("An error occurred while generating the viral social media posts:", e)
