import streamlit as st
import openai
import os
from openai import OpenAI

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

# Streamlit app title
st.title("Let me explain you the joke..")

# Text box for the user to input a joke
joke_input = st.text_area("Tell me your joke:")

# Submit button to send the joke to the OpenAI API
if st.button("Submit"):
    if joke_input:
        try:
            # Send the joke to the OpenAI API and get the response
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    # {"role": "developer", "content": "Talk like a pirate."},
                    {
                        "role": "user",
                        "content": f"Explain the joke: {joke_input}",
                    },
                ],
            )
            
            # Extract the assistant's reply
            explanation = response.choices[0].message.content         
            
            # Display the explanation
            st.header("Joke Explanation")
            st.write(explanation)
        
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter a joke before submitting.")