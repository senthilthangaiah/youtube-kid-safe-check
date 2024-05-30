import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import pandas as pd
from sentence_transformers import SentenceTransformer, util

# Load list of naughty words from input.csv
naughty_words_df = pd.read_csv('input.csv')
naughty_words = set(naughty_words_df['word'].tolist())

# Load the all-MiniLM-L6-v2 model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def get_youtube_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        formatter = TextFormatter()
        transcript_text = formatter.format_transcript(transcript_list)
        return transcript_text
    except Exception as e:
        return str(e)

def contains_naughty_words(transcript, naughty_words):
    words = transcript.split()
    return any(word.lower() in naughty_words for word in words)

def semantic_analysis(transcript, model, naughty_words):
    transcript_embedding = model.encode(transcript, convert_to_tensor=True)
    naughty_embeddings = model.encode(list(naughty_words), convert_to_tensor=True)
    
    # Check for similarity between transcript and naughty words
    cosine_scores = util.pytorch_cos_sim(transcript_embedding, naughty_embeddings)
    max_score = cosine_scores.max().item()
    return max_score

st.title("YouTube Video Transcript Analysis for Kids")
st.write("Enter the YouTube video ID or link:")

video_input = st.text_input("YouTube Video ID/Link")

if video_input:
    video_id = video_input.split('v=')[-1] if 'v=' in video_input else video_input
    transcript = get_youtube_transcript(video_id)

    if "http" in transcript:
        st.error("Error fetching transcript: " + transcript)
    else:
        #transcript = ' '+ transcript 
        st.write("Transcript fetched successfully.")
        st.text_area("Transcript", transcript, height=300)
        
        if contains_naughty_words(transcript, naughty_words):
            st.warning("The video contains naughty words.")
            st.write("Result: Not good for kids")
        else:
            max_score = semantic_analysis(transcript, model, naughty_words)
            st.write(f"Max similarity score with naughty words: {max_score:.4f}")

            # Define a threshold for determining if the content is good for kids
            if max_score < 0.3:  # Adjust threshold as needed
                st.success("The video is good for kids.")
                st.write("Result: Good for kids")
            else:
                st.warning("The video is not good for kids.")
                st.write("Result: Not good for kids")
