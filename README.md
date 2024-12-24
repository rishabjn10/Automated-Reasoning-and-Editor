# Automated Reasoning and Editor  

## Overview  
This project provides an automated reasoning and editing tool powered by various AI APIs. It leverages Docker for containerization and orchestration.

## Requirements  
- **Docker** (Ensure Docker is installed on your system)  

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

3. **Start the Application:**  
```bash
docker-compose up --force-recreate
```

## Usage  
- The `crewai flow kickoff` command will run automatically.
- Outputs will be saved in the `output/` directory on your local machine.

## 📤 **Output Directory**  
- The `output/` directory inside the container is linked to the same directory on your host machine.  
- After running the workflow, check the results:  
```bash
ls output/
```