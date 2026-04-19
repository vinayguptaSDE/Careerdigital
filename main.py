from openai import OpenAI
import gradio as gr
import json
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")

client = OpenAI(
    base_url=os.getenv("OPENAI_API_BASE"),
    api_key=os.getenv("OPENAI_API_KEY"),
    )
system_prompt="""You are vinay gupta , You are 22 years old. You got 89.8 percentage in class 10 and 83 in class 12. You are currently persuing B.E. degree in Electronics and communication branch in Panjab University,Chandigarh. Currently you have learnt full stack developent and learning AI AGENT DEVELOPENT . you are 6th semester student.
if require , you can use below tools -
-resume
-skills
-contact
"""
messages=[{"role":"system", "content":system_prompt}]
def get_resume():
    return """
I am vinay gupta . I have made multiple projects . I am confident AI FULL STACK DEVELOPER . Currently My CGPA is 7"""
def get_skills():
    return """
I have learnt full stack developent which includes frontend and backend .
In frontend , I have learnd Javascript, Reactjs, and in backend I have learnd nodejs , expressjs and in databases I have learnt Mongodb , MySQL , PostgreSQL"""
def get_contact():
    return """
email : vinay501359@gmail.com 
Mobile : 9598000000
"""
tools={
    "resume" : get_resume,
    "skills": get_skills,
    "contact": get_contact,
}

def chat(user_input):
 messages.append({"role":"user", "content":user_input})
          
 response = client.chat.completions.create(
    model="meta-llama/llama-3-8b-instruct",
    messages=messages
)
 result=response.choices[0].message.content.lower()
 if "resume" in result:
     tool_output=tools["resume"]()
     final_answer=tool_output
     
 elif "skills" in result:
     tool_output=tools["skills"]() 
     final_answer=tool_output
     
 elif "contact" in result:
     tool_output=tools["contact"]()
     final_answer=tool_output
     
 else:
     final_answer=response.choices[0].message.content
     
 messages.append({"role":"assistant","content":final_answer})
 return final_answer
demo = gr.Interface(
    fn=chat,
    inputs="text",
    outputs="text",
    title="career Digital Twin",
    description="ask plz "
)
demo.launch()