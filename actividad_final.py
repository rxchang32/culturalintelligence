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

# Título e instruções
st.title("Cultural Intelligence (CQ) Questionnaire")
st.write("Please answer each question based on how much you agree or disagree.")

# Sessão de estado para reset
if "show_results" not in st.session_state:
    st.session_state["show_results"] = False

if "respostas" not in st.session_state:
    st.session_state["respostas"] = [opcoes[3]] * len(preguntas)

# Formulário de perguntas
with st.form("cq_form"):
    for i, (pergunta, _) in enumerate(preguntas):
        st.session_state["respostas"][i] = st.radio(
            f"{i+1}. {pergunta}",
            opcoes,
            index=opcoes.index(st.session_state["respostas"][i]),
            key=f"q_{i}"
        )
    
    col1, col2 = st.columns([1, 1])
    with col1:
        enviar = st.form_submit_button("✅ Ver resultado")
    with col2:
        reiniciar = st.form_submit_button("🔄 Reiniciar")

# Processamento
if enviar:
    st.session_state["show_results"] = True

if reiniciar:
    st.session_state["respostas"] = [opcoes[3]] * len(preguntas)
    st.session_state["show_results"] = False
    st.experimental_rerun()

# Resultados
if st.session_state["show_results"]:
    resultados = {
        "Metacognitive CQ": 0,
        "Cognitive CQ": 0,
        "Motivational CQ": 0,
        "Behavioral CQ": 0,
    }

    for i, resposta in enumerate(st.session_state["respostas"]):
        categoria = preguntas[i][1]
        valor = valores[opcoes.index(resposta)]
        resultados[categoria] += valor

    st.subheader("Resultado por categoria:")
    for categoria, total in resultados.items():
        st.write(f"**{categoria}**: {total}")
