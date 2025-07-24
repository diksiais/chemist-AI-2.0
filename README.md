# 🔬 AI Research Agent for Chemists

The **AI Research Agent** is a Streamlit-powered application designed to assist chemists and researchers with idea generation, literature review, and early-stage research planning. Leveraging Google’s **Gemini Large Language Model**, it streamlines brainstorming, property prediction, literature summarization, and research proposal generation. It also integrates with external chemical databases for structural lookups and includes research history and export tools.

---

## 🚀 How It Works

### High-Level Workflow

1. **Input Research Details**  
   Provide your research topic, goal, and any existing data.

2. **Generate & Review Ideas**  
   The AI generates multiple novel research ideas. You can approve, reject, or refine ideas based on feedback.

3. **Literature Summary**  
   For the approved idea, the AI generates a preliminary literature overview. Ask follow-up questions or get search queries.

4. **Property Prediction / Experimental Approach**  
   The AI suggests chemical properties or experimental outlines. You can also perform structure lookups here.

5. **Final Compilation**  
   All content is compiled into a ready-to-download research proposal overview.

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

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**`requirements.txt` includes:**

```txt
streamlit
requests
python-docx
```

---

### 3. Get Your Google Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com).
2. Sign in with your Google account.
3. Click **"Get API Key"** from the sidebar.
4. Create or copy your API key.

---

### 4. Configure the API Key

Open `gemini_api.py` and update the API key line:

```python
API_KEY = "YOUR_ACTUAL_GEMINI_API_KEY_HERE"
```

> ⚠️ **Security Tip:** Never commit API keys to a public repo. For production, use environment variables or [Streamlit Secrets](https://docs.streamlit.io/streamlit-cloud/secrets-management).

---

### 5. Create Data Directory

The app uses SQLite to store search history. Create the folder:

```bash
mkdir data
```

`search_history.db` will be auto-created inside when the app runs.

---

## 🏃‍♀️ Running the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

This will open the app in your browser.

---

## 📂 Project Structure

```
ai-research-agent/
│
├── app.py                    # Main Streamlit UI and app logic
├── prompts.py                # Prompt templates for Gemini API
├── gemini_api.py             # Handles Gemini API communication
├── workflow.py               # Research workflow logic
├── chemical_lookup.py        # Chemical database integration (PubChem, CACTUS, Wikidata)
├── database.py               # SQLite DB operations
├── session_state_manager.py  # Streamlit session state management
├── ui_sections.py            # Renders UI components per workflow step
├── requirements.txt          # Python dependencies
└── data/                     # Stores `search_history.db`
```

---

## 📝 Usage Guide

### Start a New Research

- Fill in:
  - **Research Topic**
  - **Research Goal**
  - **Data We Already Have**
- Click **💡 Generate Research Ideas**

### Review Research Ideas

- Approve an idea with **👍 Approve Idea**
- View next with **👎 Disapprove & Next Idea**
- Refine with **🔄 Refine Current Idea** and optional feedback text

### Literature Summary & Property Prediction

- View a summary and suggested papers
- Ask follow-up questions
- View predicted properties or experimental outline
- Lookup chemical structures

### Final Step

- Download the compiled research overview document

---

## ⚠️ Important Notes

- **SSL Certificate Warning:**  
  The app disables SSL verification for some external API calls (`verify=False` in `chemical_lookup.py`). This is useful in dev environments but not secure for production.

- **AI Hallucinations:**  
  Large Language Models can generate incorrect or fabricated information. Always verify critical scientific details independently.

- **API Usage Limits:**  
  Google Gemini has a free tier, but charges may apply if you exceed limits. Monitor your usage via your Google Cloud console.

---

## 📄 License

This project is open-source under the **MIT License**.

---

Feel free to contribute or suggest improvements!
