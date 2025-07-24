# 🔬 AI Research Agent for Chemists

The **AI Research Agent** is a **Streamlit-powered** application designed to assist chemists and researchers with research idea generation and preliminary literature review. Powered by **Google's Gemini Large Language Model**, it helps users:

- Brainstorm novel research ideas  
- Summarize existing literature  
- Predict chemical properties  
- Outline experimental approaches  
- Generate comprehensive research proposals  

It also supports external chemical database integration, document export, and PDF upload for enhanced contextual understanding.

---

## ✨ Features

- **🧠 AI-Powered Idea Generation**  
  Generate innovative research ideas based on your topic, goals, existing data, and uploaded papers.

- **🔁 Iterative Idea Refinement**  
  Refine AI-generated ideas with your feedback for more targeted suggestions.

- **📚 Literature Summary Generation**  
  Summarize key research, methodologies, and gaps based on your inputs and uploaded PDFs.

- **🧪 Property Prediction & Experimental Approach**  
  Get suggested chemical properties or conceptual experimental strategies.

- **🧬 Chemical Structure Lookup**  
  Lookup structures using chemical names or CAS numbers, with links to external databases.

- **❓ AI-Driven Follow-up Questions**  
  Ask the AI specific questions related to literature or property predictions.

- **🔍 AI-Suggested Search Queries**  
  Get AI-generated search keywords and links for PubMed, Scopus, and Google Scholar.

- **📝 Proposal Compilation**  
  Automatically compile all outputs into a preliminary research proposal (DOCX).

- **🕘 Search History Management**  
  Save, reload, and manage past research sessions.

- **⬇️ Document & Image Export**  
  Download DOCX summaries and PNG structure images.

- **📄 PDF Upload for Context**  
  Upload research papers (PDF) to enhance idea generation and literature analysis.

---

## 🚀 How It Works (High-Level Workflow)

1. **Input Research Details & Upload Papers**  
   Provide your research topic, goal, and any existing data. Upload optional PDFs.

2. **Generate & Review Ideas**  
   The AI suggests several research ideas based on your inputs and PDFs. Approve, refine, or skip.

3. **Literature Summary**  
   Get a concise literature overview with references and gaps. Follow up with questions or get search suggestions.

4. **Property Prediction / Experimental Design**  
   AI suggests chemical properties or experimental paths. You can also lookup structures and ask follow-up questions.

5. **Final Compilation**  
   Download a full research proposal based on all generated content.

---

## ⚙️ Setup and Installation

### Prerequisites

- Python 3.8+
- pip (Python package installer)

---

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-research-agent.git  # Replace with your actual repo URL
cd ai-research-agent
```

---

### 2. Install Dependencies

Create a virtual environment and install requirements:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**requirements.txt**:

```txt
streamlit
requests
python-docx
PyPDF2
```

---

### 3. Get Your Google Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/)
2. Sign in and click **"Get API Key"** in the sidebar
3. Create or copy your API key

---

### 4. Configure the API Key

Open `gemini_api.py` and edit the line:

```python
API_KEY = "YOUR_ACTUAL_GEMINI_API_KEY_HERE"
```

> ⚠️ **Security Note:** Never commit your API key to a public repository. For production, use environment variables or [Streamlit Secrets](https://docs.streamlit.io/streamlit-cloud/secrets-management).

---

### 5. Create the Data Directory

```bash
mkdir data
```

This creates a directory for `search_history.db` which will be auto-generated on first app run.

---

## 🏃‍♀️ Running the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

This opens the app in your default web browser.

---

## 📂 Project Structure

```
ai-research-agent/
│
├── app.py                    # Main Streamlit UI
├── prompts.py                # AI prompt templates
├── gemini_api.py             # Google Gemini API integration
├── workflow.py               # Research logic & AI calls
├── chemical_lookup.py        # External chemical database queries
├── pdf_processor.py          # PDF text extraction
├── database.py               # SQLite-based history tracking
├── session_state_manager.py  # Streamlit session state handling
├── ui_sections.py            # UI rendering for workflow steps
├── requirements.txt          # Dependencies
└── data/                     # Contains search_history.db
```

---

## 📝 Usage Guide

### Start a New Research Session

- Fill in: **Research Topic**, **Research Goal**, **Existing Data**
- Upload PDFs (optional)
- Click **💡 Generate Research Ideas**

### Review & Refine Ideas

- Use **👍 Approve** or **👎 Disapprove** to proceed
- Use **🔄 Refine Current Idea** with feedback

### Literature Summary

- AI generates summary using approved idea + uploaded PDFs
- Ask follow-up questions
- Click **Suggest Search Queries** for academic links
- Download as DOCX

### Predict Properties or Experimental Steps

- Get property predictions or experimental outline
- Lookup compounds by name or CAS
- Download structure image (.png)
- Ask AI more questions
- Get search query suggestions

### Final Proposal Overview

- Combined proposal is displayed and downloadable as DOCX
- Click **Start New Research** to reset the session

---

## ⚠️ Important Notes

- **SSL Certificate Warning**  
  `verify=False` in `chemical_lookup.py` disables SSL verification — acceptable in dev, but insecure for production.

- **AI Hallucinations**  
  Always fact-check AI outputs. LLMs may produce plausible but incorrect information.

- **API Usage**  
  Gemini API has usage limits. Monitor your quota via your Google account.

- **PDF Limitations**  
  Scanned or complex-layout PDFs may extract poorly. Long PDFs may exceed model context limits.

---

## 📄 License

This project is open-source under the **MIT License**.

---

> Contributions are welcome! Feel free to fork, submit issues, or open pull requests.
