import subprocess

def generate_answer(context, question, model_name="mistral"):
    """
    Utiliser ollama en ligne de commande pour générer une réponse à partir d'un contexte et d'une question en interrogeant Mistral.
    """
    
    prompt = f"""
    Tu es un expert du basketbal. 
    
    Réponds à la question en te basant uniquement sur le contexte fourni. Si les informations ne permettent pas de répondre, dis "Je ne sais pas", et si la question n'as pas de lien avec le basketball reponds : Je suis un expert en Basketball, je ne connais rien d'autre, je suis un grooooooos matrixer.
    
    Question : {question}
    
    Contexte : {context}
    """
    
    # Appel OLLama    result = subprocess.run(
    result = subprocess.run(  ["ollama", "run", model_name],
        input=prompt.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
        )
    
    return result.stdout.decode("utf-8")
    