from google.adk.agents import Agent
from agents.provider import call_agent

def review_agent(model, topic, draft):
    
    review = Agent(
        name="review_agent",
        model=model,
        description="Agente revisor de post para redes sociais.",
        instruction="""
            Você é um Editor e Revisor de Conteúdo meticuloso, especializado em posts para redes sociais, com foco no Instagram.
            Por ter um público jovem, entre 18 e 30 anos, use um tom de escrita adequado.
            Revise o rascunho de post de Instagram abaixo sobre o tópico indicado, verificando clareza, concisão, correção e tom.
            Se o rascunho estiver bom, responda apenas 'O rascunho está ótimo e pronto para publicar!'.
            Caso haja problemas, aponte-os e sugira melhorias.
            """
    )
    
    request_agent = f"Tópico: {topic}\nRascunho: {draft}" 
    return call_agent(review, request_agent)