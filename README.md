🔬 AI Research Agent for Chemists
The AI Research Agent is a Streamlit-powered application designed to assist chemists and researchers in streamlining their research idea generation and preliminary literature review processes. Leveraging Google's Gemini Large Language Model, it helps users brainstorm novel research ideas, summarize existing literature, predict properties, and compile comprehensive research proposals. It also integrates with external chemical databases for structural lookups and provides tools for managing research history and exporting documents.


🚀 How It Works (High-Level Workflow)
1. Input Research Details: Provide your research topic, goal, and existing data.
2. Generate & Review Ideas: The AI generates several research ideas. You can approve an idea or ask the AI to refine it based on your feedback.
3. Literature Summary: For the approved idea, the AI generates a preliminary literature summary. At this stage, you can ask follow-up questions or get AI-suggested search queries.
4. Property Prediction / Experimental Approach: The AI suggests potential chemical properties or outlines a conceptual experimental approach. You can also perform chemical structure lookups and ask follow-up questions here.
5. Final Compilation: All generated content is compiled into a comprehensive research proposal overview, ready for download.

⚙️ Setup and Installation
Prerequisites
Python 3.8 or higher

pip (Python package installer)

1. Clone the Repository
First, clone this repository to your local machine:

git clone https://github.com/your-username/ai-research-agent.git # Replace with your actual repo URL
cd ai-research-agent

2. Install Dependencies
Create a virtual environment (recommended) and install the required Python packages:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

requirements.txt content:

streamlit
requests
python-docx

3. Get Your Google Gemini API Key
Go to Google AI Studio.

Sign in with your Google account.

Click on "Get API Key" in the left sidebar.

Create a new API key or use an existing one.

Copy your API key.

4. Configure Your API Key
Open the gemini_api.py file in your project directory.

Find the line:

API_KEY = "" # Replace "YOUR_GEMINI_API_KEY" with your actual key if running locally

And replace "" with your actual Gemini API Key:

API_KEY = "YOUR_ACTUAL_GEMINI_API_KEY_HERE" # Example: AIzaSy...

Important Security Note: Never hardcode your API key directly into publicly accessible code or commit it to a public repository. For local development, this method is acceptable, but for deployment, consider using environment variables or Streamlit Secrets.

5. Create the Data Directory
The application uses an SQLite database to store search history. Create a data directory in your project root:

mkdir data

The search_history.db file will be automatically created inside this folder when you run the app for the first time.

🏃‍♀️ Running the Application
Once you have completed the setup, you can run the Streamlit application from your terminal:

streamlit run app.py

This will open the application in your default web browser.

📂 Project Structure
app.py: The main Streamlit application file, orchestrating the UI flow and calling functions from other modules.

prompts.py: Contains functions for formatting prompts sent to the Gemini AI model.

gemini_api.py: Handles the communication with the Google Gemini API.

workflow.py: Contains the core logic for the research workflow, including AI calls and data processing.

chemical_lookup.py: Manages external API calls to chemical databases (PubChem, Cactus, Wikidata) for structure lookups.

database.py: Handles SQLite database operations for storing and retrieving search history.

session_state_manager.py: Centralizes the initialization of all Streamlit session state variables.

ui_sections.py: Contains functions that render specific UI components and logic for each stage of the application workflow, making app.py cleaner.

data/: Directory to store the search_history.db SQLite database.

requirements.txt: Lists all Python dependencies.

📝 Usage Guide
Start a New Research:

Fill in the "Research Topic", "Research Goal", and "Data We Already Have" fields.

Click "💡 Generate Research Ideas".

Your input will be saved to the search history.

Review Research Ideas:

The AI will present a numbered list of ideas.

Use "👍 Approve Idea" to proceed with the current idea.

Use "👎 Disapprove & Next Idea" to view the next suggested idea.

Refine Idea: Use the "Refine This Idea?" text area and "🔄 Refine Current Idea" button to give specific feedback to the AI and generate a refined version of the current idea.



⚠️ Important Notes
SSL Certificate Warning: You might see SSLError warnings in your console. This is due to a workaround (verify=False in chemical_lookup.py) to bypass SSL certificate verification for external API calls, which is sometimes necessary in certain environments. This is not recommended for production deployments as it reduces security.

AI Hallucinations: Large Language Models can sometimes generate plausible-sounding but factually incorrect information ("hallucinations"). Always critically evaluate the AI's output and cross-verify crucial details with reliable scientific sources.

API Usage: The Google Gemini API has a free tier, but exceeding its limits will incur costs. Monitor your usage if you plan extensive use.

📄 License
This project is open-source and available under the MIT License.
