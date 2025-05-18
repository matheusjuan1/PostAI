from datetime import date
from dotenv import load_dotenv
from agents import search_agent, planning_agent, writing_agent, review_agent
from rich import print
import os
import warnings

load_dotenv()
warnings.filterwarnings("ignore")

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL_ID = os.getenv("MAIN_MODEL_ID")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is not set in the environment variables.")

if not MODEL_ID:
    raise ValueError("MAIN_MODEL_ID is not set in the environment variables.")

if __name__ == "__main__":
    today = date.today().strftime("%d/%m/%Y")
    
    print("🚀 Iniciando o Sistema de Criação de Posts para Instagram com 4 Agentes 🚀\n")
    
    topic = input("📝 Qual o tema do post? ")
    
    if not topic:
        print("\nVocê esqueceu de digitar o tópico!")
    else:
        print(f"\nMaravilha! Vamos então criar o post sobre novidades em {topic}")
        
        search_results = search_agent(MODEL_ID, topic, today)
        print("\n--- 📝 Resultado do Agente 1 (Buscador) ---\n")
        print(search_results)
        print("--------------------------------------------------------------")

        post_plan = planning_agent(MODEL_ID, topic, search_results)
        print("\n--- 📝 Resultado do Agente 2 (Planejador) ---\n")
        print(post_plan)
        print("--------------------------------------------------------------")

        draft = writing_agent(MODEL_ID, topic, post_plan)
        print("\n--- 📝 Resultado do Agente 3 (Redator) ---\n")
        print(draft)
        print("--------------------------------------------------------------")

        final_post = review_agent(MODEL_ID, topic, draft)
        print("\n--- 📝 Resultado do Agente 4 (Revisor) ---\n")
        print(final_post)
        print("--------------------------------------------------------------")
        
        