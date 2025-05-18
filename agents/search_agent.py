from google.adk.agents import Agent
from google.adk.tools import google_search
from agents.provider import call_agent

def search_agent(model, topic, today):
    
    search = Agent(
        name="search_agent",
        model=model,
        description="Agente que busca informações no Google",
        tools=[google_search],
        instruction="""
        Você é um assistente de pesquisa. A sua tarefa é usar a ferramenta de busca do google (google_search)
        para recuperar as últimas notícias de lançamentos muito relevantes sobre o tópico abaixo.
        Foque em no máximo 5 lançamentos relevantes, com base na quantidade e entusiasmo das notícias sobre ele.
        Se um tema tiver poucas notícias ou reações entusiasmadas, é possível que ele não seja tão relevante assim
        e pode ser substituído por outro que tenha mais.
        Esses lançamentos relevantes devem ser atuais, de no máximo um mês antes da data de hoje.
        """   
    )
    
    request_agent = f"Tópico: {topic}\nData de hoje: {today}"
    return call_agent(search, request_agent)
    
    