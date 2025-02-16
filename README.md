
# **SMU FAQ Chatbot: AI vs. Rules-Based Comparison**

Developed for CSCI 3482 - Artificial Intelligence (Fall 2024), this project compares two different approaches for building a university FAQ chatbot:

1.  **AI-Based Chatbot** – Uses retrieval-augmented generation (RAG) with MiniLM-L6-V2 for embedding retrieval and OpenAI GPT-3.5 for response generation.
2.  **Rules-Based Chatbot** – A manually defined chatbot that matches user input to predefined responses.

This project includes a full implementation of both chatbots and a comparative analysis of their performance in terms of accuracy, usability, scalability, and response time.

----------

## **📑 Table of Contents**
- [Project Overview](#project-overview)
- [Team Members](#team-members-team-5)
- [Repository Contents](#repository-contents)
- [How to Run the Chatbots](#how-to-run-the-chatbots)
  - [Option 1: Running the AI Chatbot (Google Colab & Anvil Deployment)](#option-1-running-the-ai-chatbot-google-colab--anvil-deployment)
  - [Option 2: Running the Rules-Based Chatbot (Localhost Server)](#option-2-running-the-rules-based-chatbot-localhost-server)
- [Comparative Analysis](#comparative-analysis-summary)
- [Dataset Information](#dataset-information)
- [Future Improvements](#future-improvements)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Questions? Contributions?](#questions-contributions)

## **Project Overview**

### **Objective**

The goal of this project is to evaluate how well an AI-powered chatbot performs compared to a traditional rules-based chatbot when answering Saint Mary’s University (SMU) FAQs.

### **Key Features**

-   AI Chatbot: Uses semantic search and GPT-3.5 to generate responses dynamically.
-   Rules-Based Chatbot: Matches user queries to predefined responses.
-   Comparative Analysis: Evaluates complexity, accuracy, response time, usability, and user experience.

### **Team Members (Team 5)**

-   **Zachary Ivanoff** (Project Leader, AI Chatbot Frontend, Comparative Analysis)
-   **Tooba Javed** (AI Model Development, Data Collection & Cleaning, Comparative Analysis)
-   **Abhishek Basnet** (Initial AI Model Prototyping)
-   **Sohrab Gill** (Rules-Based Model Development)
-   **Youssef Lakhal** (Rules-Based Model Development)

----------

## **Repository Contents**

This project includes the following files:

-   [**README.md**](https://github.com/toobajaved/SMU-FAQ-Chatbot/blob/main/readme.md) – Overview of the project, setup, and instructions.
-   [**aibot.ipynb**](https://github.com/toobajaved/SMU-FAQ-Chatbot/blob/main/aibot.ipynb) – AI chatbot implementation using MiniLM-L6-V2, FAISS, and GPT-3.5.
-   [**server.py**](https://github.com/toobajaved/SMU-FAQ-Chatbot/blob/main/server.py) – Python server for the rules-based chatbot.
-   [**SMUlibrarybot.html**](https://github.com/toobajaved/SMU-FAQ-Chatbot/blob/main/SMUlibrarybot.html) – Frontend for the rules-based chatbot.
-   [**Comparative_Analysis.pdf**](https://github.com/toobajaved/SMU-FAQ-Chatbot/blob/main/Comparative_Analysis.pdf) – A detailed comparison between the two chatbot approaches.

----------

## **How to Run the Chatbots**

### **Option 1: Running the AI Chatbot (Google Colab & Anvil Deployment)**

1.  **Clone the repository**
    
    -   Open a terminal and run:
```bash
git clone https://github.com/yourusername/SMU-FAQ-Chatbot.git
cd SMU-FAQ-Chatbot
```
2. **aibot.ipynb in Google Colab**

-   Download and open `AI_Chatbot.ipynb` in Google Colab.
-   Install the required dependencies by running:
```
!pip install datasets faiss-cpu transformers openai anvil-uplink
```

-    Replace `openai.api_key` with your **OpenAI API key**.
-   **Run All Cells**
    
    -   Execute all cells to load the dataset, initialize FAISS, and deploy the chatbot.
    -   The chatbot will be accessible via **Anvil** at:  
        **[https://bountiful-qualified-vehicle.anvil.app/](https://bountiful-qualified-vehicle.anvil.app/)**
        
----------

### **Option 2: Running the Rules-Based Chatbot (Localhost Server)**

1.  **Install Python Dependencies**
    -   Run the following command in the terminal:
   ```
   pip install http.server
   ```
  2.  **Run the Server**

-   Start the chatbot by running:
   ```
   `python server.py
   ```
   3. **Access the Chatbot**

-   Open your web browser and go to **[http://localhost:8000/](http://localhost:8000/)**
-   The chatbot will be available for interaction.## **Comparative Analysis Summary**

### **Comparison Between AI-Based and Rules-Based Chatbot**



**Complexity**

AI: High – Uses retrieval-augmented generation with FAISS & GPT-3.5

Rules-based: Low – Uses string matching and predefined responses

**Accuracy**

AI: High – Handles variations in user queries

Rules-based: High – If user input matches predefined rules

**Response Time**

AI: 1.5–3 sec (slower due to embedding retrieval & generation)

Rules-based: 50 ms (instantaneous)

**Usability**

AI: High – Handles typos, synonyms, and context

Rules-based: Low – Requires exact keyword matching

**User Experience**

AI: More natural responses but slower

Rules-based: Fast but rigid and repetitive

For a **detailed breakdown**, check out the **Comparative_Analysis.pdf** file in this repository.

----------

## **Dataset Information**

The FAQ dataset was **curated by Tooba Javed**, who collected and cleaned over **260+ FAQs** from SMU’s website.

-   **Dataset Available on Hugging Face**:  
    **[https://huggingface.co/datasets/tootooba/SMU_FAQDataset](https://huggingface.co/datasets/tootooba/SMU_FAQDataset)**

----------

## **Future Improvements**

-   **Expand Dataset**: Add more question-answer pairs to improve AI chatbot accuracy.
-   **Optimize Response Time**: Experiment with more efficient retrieval techniques.
-   **Enhance Rules-Based Chatbot**: Implement NLP-based intent detection for more flexible responses.

----------

## **License**

This project is licensed under the [**MIT License**](https://github.com/toobajaved/SMU-FAQ-Chatbot/blob/main/LICENSE).

----------

## **Acknowledgments**

Special thanks to **Saint Mary’s University (SMU)** for the resources and inspiration behind this project.

----------

## **Questions? Contributions?**

If you have any questions, feel free to **open an issue** or **submit a pull request** on GitHub.
   
