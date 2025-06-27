# streamlit_app.py

import streamlit as st

# Perguntas e categorias
preguntas = [
    ("I am conscious of the cultural knowledge I use when interacting with people with different cultural backgrounds.", "Metacognitive CQ"),
    ("I adjust my cultural knowledge as I interact with people from a culture that is unfamiliar to me.", "Metacognitive CQ"),
    ("I am conscious of the cultural knowledge I apply to cross-cultural interactions.", "Metacognitive CQ"),
    ("I check the accuracy of my cultural knowledge as I interact with people from different cultures.", "Metacognitive CQ"),
    ("I know the legal and economic systems of other cultures.", "Cognitive CQ"),
    ("I know the rules (e.g. vocabulary, grammar) or other languages.", "Cognitive CQ"),
    ("I know the cultural values and religious beliefs of other cultures.", "Cognitive CQ"),
    ("I know the marriage systems of other cultures.", "Cognitive CQ"),
    ("I know the arts and crafts of other cultures.", "Cognitive CQ"),
    ("I know the rules for expressing nonverbal behaviors in other cultures.", "Cognitive CQ"),
    ("I enjoy interacting with people from different cultures.", "Motivational CQ"),
    ("I am confident that I can socialize with locals in a culture that is unfamiliar to me.", "Motivational CQ"),
    ("I am sure I can deal with the stresses of adjusting to a culture that is new to me.", "Motivational CQ"),
    ("I enjoy living in cultures that are unfamiliar to me.", "Motivational CQ"),
    ("I am confident that I can get accustomed to the shopping conditions in a different culture.", "Motivational CQ"),
    ("I change my verbal behavior (e.g., accent, tone) when a cross-cultural interaction requires it.", "Behavioral CQ"),
    ("I use pause and silence differently to suit different cross-cultural situations.", "Behavioral CQ"),
    ("I vary the rate of my speaking when a cross-cultural situation requires it.", "Behavioral CQ"),
    ("I alter my facial expressions when a cross-cultural interaction requires it.", "Behavioral CQ"),
    ("I change my non-verbal behavior when a cross-cultural interaction requires it.", "Behavioral CQ")
]

# Escala Likert
opcoes = ["Strongly Disagree", "Disagree", "Somewhat Disagree", "Neutral", "Somewhat Agree", "Agree", "Strongly Agree"]
valores = [1, 2, 3, 4, 5, 6, 7]

st.title("Cultural Intelligence (CQ) Questionnaire")

respostas = []
for i, (pergunta, _) in enumerate(preguntas):
    resposta = st.radio(f"{i+1}. {pergunta}", opcoes, index=3, key=f"q_{i}")
    respostas.append(resposta)

if st.button("Ver resultado"):
    resultados = {
        "Metacognitive CQ": 0,
        "Cognitive CQ": 0,
        "Motivational CQ": 0,
        "Behavioral CQ": 0,
    }

    for i, resposta in enumerate(respostas):
        categoria = preguntas[i][1]
        valor = valores[opcoes.index(resposta)]
        resultados[categoria] += valor

    st.subheader("Resultado por categoria:")
    for categoria, total in resultados.items():
        st.write(f"**{categoria}**: {total}")
