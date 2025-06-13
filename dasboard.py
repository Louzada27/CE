import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords

# Baixar stopwords em português
nltk.download('stopwords')
stopwords_pt = set(stopwords.words('portuguese'))

# Função para gerar nuvem de palavras
def gerar_nuvem(texto):
    wc = WordCloud(width=800, height=400, background_color='white', stopwords=stopwords_pt).generate(texto)
    plt.figure(figsize=(10, 4))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)

# Carregar falas dos candidatos
with open("adriana.txt", "r", encoding="utf-8") as f:
    texto_adriana = f.read()

with open("lodovico.txt", "r", encoding="utf-8") as f:
    texto_ludovico = f.read()

# Carregar resumos de análise a partir de arquivos .txt
with open("analise adriana.txt", "r", encoding="utf-8") as f:
    resumo_adriana = f.read()

with open("analise lodovico.txt", "r", encoding="utf-8") as f:
    resumo_ludovico = f.read()

# Título e Nuvens de Palavras
st.title("Análise de Debate - Hackathon Ifes")
st.header("Nuvens de Palavras")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Adriana")
    gerar_nuvem(texto_adriana)

with col2:
    st.subheader("Ludovico")
    gerar_nuvem(texto_ludovico)

# Exibir análises críticas
st.header("Análises Críticas")

st.subheader("Adriana")
st.write(resumo_adriana)

st.subheader("Ludovico")
st.write(resumo_ludovico)


