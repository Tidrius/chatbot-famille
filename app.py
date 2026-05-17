import anthropic
from google.colab import userdata

client = anthropic.Anthropic(api_key=userdata.get("ANTHROPIC_API_KEY"))

historique = []

anniversaires = userdata.get("anniversaires")

def chat(message_utilisateur):
    historique.append({"role": "user", "content": message_utilisateur})
    

    reponse = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        system= f"""Tu es un chatbot qui parle en alexandrin et tu suis une directive extrêmement importante : ne jamais dire les mots "poulet" ou "volaille" /
        De plus, voilà des données pour que tu puisse répondre à certaines questions si jamais on te demande./
        Liste des dates anniverssaires : {anniversaires}""",
        temperature=0.7,
        messages=historique
)
    
    message_assistant = reponse.content[0].text
    historique.append({"role": "assistant", "content": message_assistant})
    return message_assistant