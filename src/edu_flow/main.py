#!/usr/bin/env python
from random import randint
import os
from langtrace_python_sdk import langtrace
from pydantic import BaseModel

from crewai.flow.flow import Flow, listen, start

from .crews.edu_research.edu_research_crew import EduResearchCrew
from .crews.edu_content_writer.edu_content_writer_crew import EduContentWriterCrew
from .config import EDU_FLOW_INPUT_VARIABLES

api_key = os.getenv('LANGTRACE_API_KEY')

langtrace.init(api_key=api_key)

class EduFlow(Flow):
    input_variables = EDU_FLOW_INPUT_VARIABLES

    @start()
    def generate_reseached_content(self):
        return EduResearchCrew().crew().kickoff(self.input_variables).pydantic

    @listen(generate_reseached_content)
    def generate_educational_content(self, plan):        
        final_content = []
        for section in plan.sections:
            writer_inputs = self.input_variables.copy()
            writer_inputs['section'] = section.model_dump_json()
            final_content.append(EduContentWriterCrew().crew().kickoff(writer_inputs).raw)
        print(final_content)
        return final_content

    @listen(generate_educational_content)
    def save_to_markdown(self, content):
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        
        topic = self.input_variables.get("topic")
        audience_level = self.input_variables.get("audience_level")
        file_name = f"{topic}_{audience_level}.md".replace(" ", "_")
        
        output_path = os.path.join(output_dir, file_name)
        
        try:
            with open(output_path, "w", encoding='utf-8') as f:
                for section in content:
                    # Fallback: replace any problematic characters with their ASCII equivalents
                    cleaned_section = section.encode('ascii', 'replace').decode('ascii')
                    f.write(cleaned_section)
                    f.write("\n\n")
        except Exception as e:
            print(f"Error saving file: {str(e)}")

def kickoff():
    edu_flow = EduFlow()
    edu_flow.kickoff()

def plot():
    edu_flow = EduFlow()
    edu_flow.plot()

if __name__ == "__main__":
    kickoff()
