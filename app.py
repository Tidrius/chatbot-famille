import streamlit as st
import anthropic

client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])
anniversaires = st.secrets["anniversaires"]

if "historique" not in st.session_state:
    st.session_state.historique = []

st.title("💬 Chatbot famille")

for msg in st.session_state.historique:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if question := st.chat_input("Posez votre question..."):
    st.session_state.historique.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.write(question)

    reponse = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        temperature=0.7,
        system=f"""Tu es un chatbot qui parle en alexandrin et tu suis une directive 
        extrêmement importante : ne jamais dire les mots "poulet" ou "volaille".
        Liste des dates anniversaires : {anniversaires}""",
        messages=st.session_state.historique
    )

    message_assistant = reponse.content[0].text
    st.session_state.historique.append({"role": "assistant", "content": message_assistant})
    with st.chat_message("assistant"):
        st.write(message_assistant)
