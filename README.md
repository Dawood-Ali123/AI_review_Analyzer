For your AI Review Analyzer Pro project, here are professional versions of both files.

1. .gitignore

Create a file named:

.gitignore

Paste this into it:

# Environment Variables
.env

# Virtual Environment
venv/
.venv/

# Python Cache
__pycache__/
*.pyc

# VS Code
.vscode/

# Streamlit
.streamlit/

# Operating System Files
.DS_Store
Thumbs.db

This ensures that your API keys, virtual environment, cache files, and editor settings are not uploaded to GitHub.

2. README.md

Create a file named:

README.md

Paste the following:

# ⭐ AI Review Analyzer Pro

An AI-powered Review Analyzer built using **LangChain**, **Google Gemini**, and **Streamlit**.

The application analyzes customer reviews and returns structured information using **LangChain Structured Output (TypedDict)**.

---

## 🚀 Features

- 📝 Review Summary
- 😊 Sentiment Analysis
- ⭐ Rating Prediction (1–5)
- 📊 Confidence Score
- ✅ Positive Points Extraction
- ❌ Negative Points Extraction
- 👍 Recommendation (Recommended / Not Recommended)
- 🤖 Structured Output using TypedDict
- 🎨 Interactive Streamlit UI

---

## 🛠 Technologies Used

- Python
- LangChain
- Google Gemini API
- Streamlit
- TypedDict
- Prompt Engineering
- Python-dotenv

---

## 📂 Project Structure

```text
AI_Review_Analyzer/
│
├── app.py
├── llm.py
├── prompts.py
├── schema.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## ⚙️ Installation

### Clone the repository

```bash
git cone https://github.com/Dawood-Ali123/AI_review_Analyzer.git
```

### Move into the project folder

```bash
cd AI-Review-Analyzer-Pro
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create a `.env` file

```text
GOOGLE_API_KEY=YOUR_GOOGLE_GEMINI_API_KEY
```

### Run the application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

### Home Page

(Add screenshot here)

### Review Analysis

(Add screenshot here)

### Structured Output

(Add screenshot here)

---

## 📄 Example Input

```text
I bought this phone last week.

The camera is amazing.

The battery lasts all day.

The display is beautiful.

However, the charging speed is slow.
```

---

## 📄 Example Output

```json
{
  "summary": "The customer is satisfied with the phone. They like the camera, battery, and display but dislike the charging speed.",
  "sentiment": "Positive",
  "rating": 4,
  "confidence": 0.97,
  "positive_points": [
    "Excellent Camera",
    "Long Battery Life",
    "Beautiful Display"
  ],
  "negative_points": [
    "Slow Charging"
  ],
  "recommendation": "Recommended"
}
```

---

## 📚 Concepts Practiced

- LangChain Chat Models
- Prompt Engineering
- Structured Output
- TypedDict
- Streamlit
- Google Gemini API

---

## 🔮 Future Improvements

- PDF Review Analysis
- Batch Review Processing
- Sentiment Charts
- Review Statistics Dashboard
- Pydantic Structured Output
- Database Integration
- RAG-based Product Review Search

---

## 👨‍💻 Author

**Dawood Ali**

AI & Machine Learning Student

Currently Learning:

- Machine Learning
- Deep Learning
- PyTorch
- LangChain
- Generative AI
- Agentic AI

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.