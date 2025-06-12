import openai

openai.api_key = "sua-chave-aqui"

def analisar_falas(falas, nome):
    prompt = f"""
    Abaixo estão trechos de falas da candidata/o {nome}. Faça uma análise crítica destacando os pontos positivos,
    propostas relevantes e consistência argumentativa. Seja imparcial e técnico.
    \n\nFalas:\n{falas[:3000]}...
    """
    resposta = openai.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=800
    )
    return resposta.choices[0].message.content


# Carregar o conteúdo dos arquivos
with open("adriana.txt", "r", encoding="utf-8") as f:
    adriana_falas = f.read()

with open("lodovico.txt", "r", encoding="utf-8") as f:
    ludovico_falas = f.read()

resumo_adriana = analisar_falas(adriana_falas, "Adriana")
resumo_ludovico = analisar_falas(ludovico_falas, "Ludovico")

print("Adriana:\n", resumo_adriana)
print("\nLudovico:\n", resumo_ludovico)
