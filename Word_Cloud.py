import streamlit as st
from wordcloud import WordCloud
import numpy as np
from PIL import Image

def generate_word_cloud(phrase):
    # Generate a word cloud image
    wordcloud = WordCloud(width = 800, height = 400).generate(phrase)
    return wordcloud.to_array()

def st_wordcloud_app():
    st.title("Word Cloud Generator")
    
    # Text input for the phrase
    user_input = st.text_area("Enter your phrase here:", "Type Here")

    if st.button("Generate Word Cloud"):
        # Generate the word cloud from the input phrase
        wordcloud_image = generate_word_cloud(user_input)
        
        # Convert to image and display
        st.image(wordcloud_image, use_column_width=True)

if __name__ == '__main__':
    st_wordcloud_app()
