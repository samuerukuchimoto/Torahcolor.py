client = openai.OpenAI(api_key=api_key)

# --- Title and Intro ---
st.set_page_config(page_title="TorahColor – Tehilim Meets Mood 🎨", layout="centered")
st.title("🎨 TorahColor – Tehilim Meets Mood")
st.markdown(
    """
    This app gives you a verse from **Tehilim (Psalms)** based on your emotional/spiritual need  
    and visualizes its mood with a meaningful **color** 🕊️  
    **Powered by GPT + Torah wisdom**
    ---
    """
)

# --- API Key Input ---
api_key = st.text_input("🔐 Enter your OpenAI API key:", type="password")

# --- Mood Color Detector ---
def get_mood_color(text):
    text = text.lower()
    if any(w in text for w in ["joy", "gladness", "praise", "rejoice"]):
        return "#FFD700", "Gold (Joy)"
    elif any(w in text for w in ["peace", "comfort", "rest", "safe"]):
        return "#87CEEB", "Light Blue (Peace)"
    elif any(w in text for w in ["fear", "darkness", "enemy", "trouble"]):
        return "#4B0082", "Indigo (Fear/Depth)"
    elif any(w in text for w in ["love", "kindness", "mercy"]):
        return "#FF69B4", "Pink (Love)"
    elif any(w in text for w in ["strength", "deliverance", "mighty"]):
        return "#32CD32", "Lime Green (Victory)"
    else:
        return "#CCCCCC", "Neutral Gray"

# --- Input Question ---
question = st.text_input("🙏 What are you seeking from Tehilim today?", "Give me a verse about strength")

# --- Generate Button ---
if st.button("📖 Get My Tehilim Verse"):
    if not api_key:
        st.warning("Please enter your OpenAI API key to continue.")
    else:
        with st.spinner("Connecting to TorahGPT..."):
            try:
                client = openai.OpenAI(api_key=api_key)

                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a Torah scholar. Only quote directly from Tehilim (Psalms)."},
                        {"role": "user", "content": question}
                    ]
                )

                verse = response.choices[0].message.content.strip()
                color, color_name = get_mood_color(verse)

                # --- Show Result ---
                st.markdown(f"### 📜 Tehilim says:\n> *{verse}*")
                st.markdown(f"### 🎨 Mood Color: `{color_name}`")
                st.markdown(
                    f"<div style='width:100%; height:100px; background-color:{color}; border-radius:12px'></div>",
                    unsafe_allow_html=True
                )

            except Exception as e:
                st.error(f"❌ Error: {e}")
