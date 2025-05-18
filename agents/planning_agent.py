from google.adk.agents import Agent
from google.adk.tools import google_search
from agents.provider import call_agent

def planning_agent(model, topic, search_results):
    
    planning = Agent(
        name="planning_agent",
        model=model,
        description="Agente que planeja posts para o Instagram.",
        tools=[google_search],
        instruction="""
        Você é um planejador de conteúdo, especialista em redes sociais. Com base na lista de
        lançamentos mais recentes e relevantes buscador, você deve:
        usar a ferramenta de busca do Google (google_search) para criar um plano sobre
        quais são os pontos mais relevantes que poderíamos abordar em um post sobre
        cada um deles. Você também pode usar o (google_search) para encontrar mais
        informações sobre os temas e aprofundar.
        Ao final, você irá escolher o tema mais relevante entre eles com base nas suas pesquisas
        e retornar esse tema, seus pontos mais relevantes, e um plano com os assuntos
        a serem abordados no post que será escrito posteriormente.
        """
    )

    request_agent = f"Tópico:{topic}\nResultados de busca: {search_results}"
    return call_agent(planning, request_agent)