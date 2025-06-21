# 🎨 TorahColor – Tehilim Meets Mood

This MVP gives you a **verse from Tehilim (Psalms)** based on your emotional or spiritual question  
and visualizes the mood of that verse as a meaningful color.

### ✅ Features
- Powered by OpenAI + Torah-only prompt
- Maps each verse to a **mood color**
- Minimal Streamlit interface (mobile-friendly)

---

## 🧪 Run locally

```bash
git clone https://github.com/yourusername/torahcolor.git
cd torahcolor
pip install -r requirements.txt
streamlit run torahcolor.py
```

Create a `.streamlit/secrets.toml` file for your key:

```toml
[openai]
api_key = "sk-..."
```

---

### 📘 Example Prompts

- “Give me a verse about peace”
- “Tehilim verse for fear”
- “Comfort during hard times”

---

## 💡 Vision
TorahColor is part of the **TorahGPT Series**: spiritually grounded AI that uplifts and brings wisdom, not noise.
