# AI Python test Generator

An AI-powered application that generates python tests cases using Large Language Models.

## Tech Stack
- Python
- Claude(Anthropic) API
- Gradio

## Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/MeghaRajpara/python-tests-generator.git
cd python-tests-generator
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
```bash
cp .env.example .env
```
Add your OpenAI API key to .env.

### 5. Run Application
```bash
python main.py
```

### 6. Open Browser
Gradio will start locally at:
```bash
http://127.0.0.1:7860
```
Or Your local URL