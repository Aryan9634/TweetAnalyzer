from dotenv import load_dotenv
load_dotenv() #loading all the env variables

import pandas as pd
import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to load Gemini Pro model and get responses

model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text


st.set_page_config(page_title="Sentiment Analysis",
                   layout="wide")
st.title("Sentiment Complete Analysis")
st.subheader("Tweet Insight: Decoding Emotions, Identifying Issues, and Offering Aid")
st.divider()

input_tweet = st.text_input("Input Tweet:", key="input")
submit = st.button("Analyze Tweet")
 
if submit:

    # Sentiment Analysis
    sentiment = get_gemini_response(f"What is the sentiment of this tweet: {input_tweet}? (Positive, Negative, or Neutral)")
    if sentiment=="Positive":
        st.subheader(f"Sentiment : {sentiment} 🟢")
    elif sentiment=="Neutral":
        st.subheader(f"Sentiment : {sentiment} 🟡")
    elif sentiment=="Negative":
        st.subheader(f"Sentiment : {sentiment} 🔴")
        
    st.divider()

    left, right = st.columns(2)  
    with left:
        # Possible Reasons
        st.subheader("Possible Reasons Behind the Tweet")
        reasons = get_gemini_response(f"What are three possible reasons behind the following tweet, give only three points and keep it under 250 words: {input_tweet}?")
        st.write(reasons)

        st.divider()

        l1, r1 = st.columns(2)
        with l1:
            # Polarity scores
            st.subheader("Polarity scores")
            reasons = get_gemini_response(f"what are the scores, like positive, negative, neutral and compound score following tweet, give in tabular format: {input_tweet}?")
            st.write(reasons)

        with r1:
            # Emotional Variance
            st.subheader("Emotional Variance")
            reasons = get_gemini_response(f"Generate a table with two rows and six columns. In the first row, list six human emotions: \
                                            Happiness, Sadness, Anger, Fear, Surprise, Disgust. In the second row, provide their respective \
                                            values in decimal format based on the sentiment expressed in the input text. Use values between \
                                            0 and 1, where 0 represents absence of the emotion and 1 represents maximum intensity of the emotion.: {input_tweet}?")
            st.write(reasons)

    with right: 
        # How to Help
        st.subheader("How We Can Help")
        help_text = get_gemini_response(f"What can we do to help based on the following tweet, give only three points and keep it under 250 words: {input_tweet}?")
        st.write(help_text)

