import streamlit as st
import openai
import os

st.set_page_config(page_title="Solomon Bot", layout="centered")

# --- Setup ---
st.title("🦉 Solomon Bot")
st.subheader("Receive wisdom like Solomon, based on your current mood.")

# --- API Key ---
openai_api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    st.warning("Please set your OpenAI API key in Streamlit secrets or as an environment variable.")
    st.stop()

openai.api_key = openai_api_key

# --- Mood Selection ---
moods = [
    "joyful", "sorrowful", "anxious", "angry", "hopeful", "weary", "contemplative",
    "grateful", "confused", "determined", "fearful", "bored"
]
mood = st.selectbox("What is your mood right now?", sorted(moods))

# --- Call OpenAI ---
def get_solomon_question(mood: str) -> str:
    prompt = (
        f"You are King Solomon from the Old Testament. "
        f"Write a single thought-provoking question in poetic, biblical style, "
        f"addressed to someone who is feeling {mood}. "
        f"Your tone should be wise, reflective, and ancient."
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",  # or "gpt-3.5-turbo" if using that
        messages=[
            {"role": "system", "content": "You are the voice of Solomon, the biblical king of wisdom."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.9,
        max_tokens=150
    )

    return response['choices'][0]['message']['content'].strip()

# --- UI Trigger ---
if st.button("Ask Solomon"):
    with st.spinner("Consulting the wisdom of Solomon..."):
        question = get_solomon_question(mood)
        st.markdown("### 📜 A question from Solomon:")
        st.success(question)
