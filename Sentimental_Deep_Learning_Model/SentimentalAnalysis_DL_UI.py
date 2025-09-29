
import streamlit as st
from langdetect import detect
import os
from langchain_groq import ChatGroq
os.environ["GROQ_API_KEY"] = "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"
from langchain.prompts import PromptTemplate


model_path = "Sentimental_DL.h5"

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

st.title("Sentiment Analysis")
# Load model
model = load_model(model_path , compile=False)

try :
    new_texts = st.text_input("Enter your review:")

    if isinstance(new_texts, tuple):
        new_texts = " ".join(new_texts)


    # Now safe
    new_texts = new_texts.lower()
    lang = detect(new_texts)

    lang = detect(new_texts.lower())
    
    if lang == 'en':    
        new_texts = new_texts
   
    else:
        
        prompt = PromptTemplate(
        input_variables=["new_texts"],
        template="""
            You are a helpful assistant that translate messages.
            translate the following messages to English.
            {new_texts}
            """)

        llm = ChatGroq(
        model="deepseek-r1-distill-llama-70b",
        max_tokens=None,
        reasoning_format="parsed",
        timeout=None,)
        chain = prompt | llm

        ai_message = chain.invoke({"new_texts": new_texts})
        new_texts = ai_message.content  # Extract the string from the AIMessage object
        
    
except Exception as e:
    st.error(f"{e}")        
        

try:     
        
    tokenizer = Tokenizer(num_words=10000, oov_token="<OOV>")
    tokenizer.fit_on_texts([new_texts])
    seqs = tokenizer.texts_to_sequences([new_texts])
    padded = pad_sequences(seqs, maxlen=16, padding="post")
    if padded.shape[0] == 0:
        raise ValueError("No input data to predict on! Check your preprocessing/tokenizer.")

    preds = model.predict(padded)

    for text, p in zip(new_texts, preds):
        

        predicted_rating = p.argmax()+1

    def predict_Sentiment(predicted_rating):
        if predicted_rating == 1:
            return "Negative"
        elif predicted_rating == 2:
            return "Negative"
        elif predicted_rating == 3:
            return "Neutral"
        elif predicted_rating == 4:
            return "Positive"
        else:
            return "Positive"
        
        
    st.subheader(f"Rating : {predicted_rating}")

    st.subheader(predict_Sentiment(predicted_rating))

except Exception as e:
    st.error(f"{e}")

