# 📧 Cold Mail Generator

A Streamlit web application that generates personalized cold emails for job applications using AI. Just input a job posting URL and get a ready-to-send cold email tailored to your skills and projects.

---

## 🚀 Features

- 🔗 Enter any job URL (e.g., Meta Careers, Walmart Careers, etc.)
- 🤖 Extracts job description using LangChain's `WebBaseLoader`
- 🧠 Uses LLMs (Groq + LLaMA3) to understand and extract role, skills, experience
- 📎 Matches required skills with your portfolio using ChromaDB
- 📨 Generates a customized cold email
- 💾 Allows download of the generated email
- 🧪 View extracted job JSON for transparency

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **LLM Backend**: [LangChain](https://www.langchain.com/), Groq API with LLaMA-3
- **Vector DB**: ChromaDB
- **Data Parsing**: BeautifulSoup (under the hood via LangChain)

---

## 📂 Project Structure

```
Cold-Email-Generator/
├── main.py              # Streamlit app entrypoint
│
├── app/
│   ├── chains.py            # LangChain prompts and chains
│   ├── portfolio.py         # Loads and queries personal projects
│   ├── utils.py             # Helper functions (e.g. text cleaning)
│   └── resource/
│       └── my_portfolio.csv # CSV with your project titles, tech stack, and links
│
├── requirements.txt
└── README.md
```

---

## 🔧 Setup Instructions

1. **Clone the repo**  
   ```bash
   git clone https://github.com/vaibhavgaikwad7/Cold-Email-Generator.git
   cd Cold-Email-Generator
   ```

2. **Create virtual environment & activate it**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # on Windows
   source venv/bin/activate  # on Mac/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set your `.env` file**
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. **Run the app**
   ```bash
   streamlit run app/main.py
   ```

---

## ✨ Demo

> Coming soon (optional: you can add a Streamlit Community Cloud link or a GIF demo)

---

## 📄 License

MIT License. Feel free to fork, adapt, and share!

---

## 🙋‍♂️ Author

**Vaibhav Gaikwad**  
[LinkedIn](https://www.linkedin.com/in/vaibhavgaikwad7) · [GitHub](https://github.com/vaibhavgaikwad7)
