# Automated Reasoning and Editor  

## Overview  
This project provides an automated reasoning and editing tool powered by various AI APIs.  

## Requirements  
- **Python 3.11+** (Ensure Python is installed on your system)  

## Setup  

1. **Clone the Repository:**  
```bash
git clone https://github.com/rishabjn10/Automated-Reasoning-and-Editor.git
cd Automated-Reasoning-and-Editor
```

2. **Create and Configure Environment Variables:**  
- Copy `.env.example` to `.env` in the root directory:  
```bash
cp .env.example .env
```
- Open `.env` and update the following fields with your API keys:  
```
OPENAI_API_KEY=<your OpenAI API key>
LANGTRACE_API_KEY=<your Langtrace API key>
SERPER_API_KEY=<your Serper API key>
```

3. **Set Up a Virtual Environment:**  
- **For Linux/Mac:**  
```bash
python3 -m venv venv
source venv/bin/activate
```
- **For Windows (Command Prompt):**  
```bash
python -m venv venv
venv\Scripts\activate
```

4. **Install Dependencies:**  
```bash
pip install -r requirements.txt
```

5. **Run the Application:**  
```bash
crewai flow kickoff
```

## 📤 **Output Directory**  
- Outputs will be saved in the `output/` directory.  
- After running the workflow, check the results:  
```bash
ls output/
```  
