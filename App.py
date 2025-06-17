import streamlit as st
import os
from openai import OpenAI

# --- Set up OpenAI client ---
api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("Please set your OpenAI API key.")
    st.stop()

client = OpenAI(api_key=api_key)

# --- Define moods ---
moods = [
    "joyful", "sorrowful", "anxious", "angry", "hopeful", "weary", "contemplative",
    "grateful", "confused", "determined", "fearful", "bored"
]

# --- UI ---
st.set_page_config(page_title="Solomon Bot", layout="centered")
st.title("🦉 Solomon Bot")
st.subheader("Receive wisdom like Solomon, based on your current mood.")

mood = st.selectbox("What is your mood right now?", sorted(moods))

# --- Wisdom generation ---
def get_solomon_question(mood: str) -> str:
    prompt = (
        f"You are King Solomon from the Old Testament. "
        f"Write a single thought-provoking question in poetic, biblical style, "
        f"addressed to someone who is feeling {mood}. "
        f"Your tone should be wise, reflective, and ancient."
    )

    response = client.chat.completions.create(
        model="gpt-4",  # or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You are the voice of Solomon, the biblical king of wisdom."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.9,
        max_tokens=150
    )

    return response.choices[0].message.content.strip()

# --- Trigger ---
if st.button("Ask Solomon"):
    with st.spinner("Consulting the wisdom of Solomon..."):
        question = get_solomon_question(mood)
        st.markdown("### 📜 A question from Solomon:")
        st.success(question)
