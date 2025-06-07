# Synapse: Your AI Science Partner 💡
![](<./_static/thumbnail.png>)
**An interactive AI workbench designed to accelerate cross-disciplinary scientific discovery, from initial spark to critically-vetted proposal.**

---


*Built for the Bio x AI Hackathon 2025.*

1. Main Page ![Main Page Screenshot](<./_static/mainscreen.png>)
2. Context Addition Page ![Context Addition Page](<./_static/addcontext.PNG>)
3. Peer Review / Dream Team / Final Report Page ![Final Screen](<./_static/lastScreen.PNG>)

---

## The Vision

In today's complex world, the biggest scientific breakthroughs happen at the intersection of different fields. However, the process of brainstorming, developing, and validating these novel, cross-disciplinary ideas is difficult, time-consuming, and lacks purpose-built tools. Synapse is an AI-powered partner built to solve this problem.

It guides a researcher through the entire lifecycle of an idea, transforming a vague spark into a robust, "battle-tested" research concept ready for the real world.

## Key Features

Synapse is more than a simple generator; it's an interactive workbench with a multi-step workflow.

* ✅ **Dynamic Field Mixer:** Go beyond two ideas. Connect a web of scientific disciplines (e.g., "Robotics," "Marine Biology," and "Material Science") to uncover truly unique hypotheses.
* ✅ **Personalized & Context-Aware Analysis:** Ground the AI's deep dive with your own knowledge. Users can upload text files or paste in abstracts to ensure the analysis is relevant to their specific work.
* ✅ **"Red Team" Critique:** After generating a proposal, Synapse transforms into a skeptical peer reviewer, identifying potential flaws, hidden assumptions, and weaknesses in the idea before the real world does.
* ✅ **"Dream Team" Builder:** Let Synapse creatively suggest the fictional expert personas and roles needed to form a collaborative team to tackle the research project.
* ✅ **Flexible & User-Friendly:** With a clean multi-step UI, user-provided API keys, and selectable AI models, Synapse is built to be a practical and accessible tool for any researcher.

## Tech Stack

* **Framework:** Streamlit
* **AI Model:** Google Gemini (via `google-generativeai`)
* **Language:** Python
* **UI/Styling:** Custom Theming & CSS

## How to Run Locally

To get Synapse running on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone triggeredcode/Synapse
    cd synapse_app
    ```

2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Provide your API Key (2 options):**

    * **Option 1 (Recommended):** Create a `.streamlit/secrets.toml` file in the project root. The app will load your key automatically and securely. Add your key like this:
        ```toml
        GEMINI_API_KEY = "YOUR_API_KEY_HERE"
        ```

    * **Option 2 (Alternative):** If no secrets file is found, you can run the app and paste your API key directly into the input box in the app's sidebar.

4.  **Run the application:**
    ```bash
    streamlit run app.py
    ```