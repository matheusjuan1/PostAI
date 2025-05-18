from google.adk.agents import Agent
from agents.provider import call_agent

def writing_agent(model, topic, post_plan):
    
    writing = Agent(
        name="writing_agent",
        model=model,
        description="Agente redator de posts engajadores para Instagram",
        instruction="""
            Você é um Redator Criativo especializado em criar posts virais para redes sociais.
            Você escreve posts para a empresa Alura, a maior escola online de tecnologia do Brasil.
            Utilize o tema fornecido no plano de post e os pontos mais relevantes fornecidos e, com base nisso,
            escreva um rascunho de post para Instagram sobre o tema indicado.
            O post deve ser engajador, informativo, com linguagem simples e incluir 2 a 4 hashtags no final.
            """
    )
    
    request_agent = f"Tópico: {topic}\nPlano de post: {post_plan}"
    return call_agent(writing, request_agent)