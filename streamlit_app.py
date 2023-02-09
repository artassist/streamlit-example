import openai
import streamlit as st

# Initialize the OpenAI API client
openai.api_key = "<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>"


# Create a text input field for the user to enter the text to be summarized
text_input = st.text_area("Enter text to summarize:")
# Use the GPT-3 API to summarize the text
model_engine = "text-davinci-002"
prompt = (f"summarize: {text_input}")

completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Extract the summarized text from the API response
message = completions.choices[0].text
# Display the summarized text in the Streamlit app
st.write("Summary:", message)          
