import streamlit as st
import requests

# Set the title of the website
st.title("Meme Generator")

st.write("YASH")

# Add a header
st.header("Enjoy Some Random Memes!")

# Function to fetch meme from API
def get_meme():
    url = "https://meme-api.com/gimme"
    response = requests.get(url)
    data = response.json()
    return data['title'], data['url']

# Fetch and display a meme
meme_title, meme_url = get_meme()
st.subheader(meme_title)
st.image(meme_url, caption="Source: Reddit", use_column_width=True)

# Add a button to fetch a new meme
if st.button("Get Another Meme"):
    meme_title, meme_url = get_meme()
    st.subheader(meme_title)
    st.image(meme_url, caption="Source: Reddit", use_column_width=True)

