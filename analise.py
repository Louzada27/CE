from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords

# Baixar stopwords
nltk.download('stopwords')
stopwords_pt = set(stopwords.words('portuguese'))

# Função para gerar nuvem de palavras
def gerar_nuvem(texto, titulo):
    wordcloud = WordCloud(
        width=800, height=400,
        background_color='white',
        stopwords=stopwords_pt
    ).generate(texto)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(titulo)
    plt.show()

# Lendo as falas dos arquivos
with open("adriana.txt", "r", encoding="utf-8") as f:
    texto_adriana = f.read()

with open("lodovico.txt", "r", encoding="utf-8") as f:
    texto_ludovico = f.read()

# Texto completo
texto_total = texto_adriana + " " + texto_ludovico

# Gerar as nuvens
gerar_nuvem(texto_total, "Nuvem de Palavras - Geral")
gerar_nuvem(texto_adriana, "Nuvem de Palavras - Adriana")
gerar_nuvem(texto_ludovico, "Nuvem de Palavras - Ludovico")
