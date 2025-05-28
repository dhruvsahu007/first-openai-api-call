# First OpenAI API Call

## 🚀 What This Script Does

This Python script sends a prompt to OpenAI's GPT-3.5-turbo model using the official API and prints:
- The assistant's response
- Token usage stats (prompt, completion, total)

It uses:
- A **fixed system prompt**
- A **user input prompt from the console**

## ⚙️ How to Run

### 1. Clone the Repo

```bash
git clone https://github.com/dhruvsahu007/first-openai-api-call.git
cd first-openai-api-call
## 2. Set Up Virtual Environment

```
## 2. Set Up Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # For Windows
# or use `source venv/bin/activate` on Mac/Linux

```
## 3. Install Dependencies
```bash
pip install -r requirements.txt
```
## 4. Add Your OpenAI API Key
Create a .env file in the root of your project folder and add your key like this:
```bash
OPENAI_API_KEY=sk-your-api-key-here
```

## 5. Run the Script
```bash
python first_call.py
```

## 🧪 Example Interaction
```
Enter your prompt: list 3 AI engineer roles

Assistant's Reply:
1. Machine Learning Engineer
2. Data Scientist
3. AI Research Scientist

Token Usage:
Prompt Tokens: 23
Completion Tokens: 16
Total Tokens: 39
```
