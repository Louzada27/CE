import re

with open("transcrição.txt", "r", encoding="utf-8") as f:
    texto = f.read()

# Expressões regulares para identificar início das falas
adriana_inicio = re.compile(r"(candidata professora adriana|professora adriana|adriana, a partir de agora)", re.IGNORECASE)
lodovico_inicio = re.compile(r"(candidato professor ludovico|professor ludovico|ludovico, a partir de agora)", re.IGNORECASE)

# Encontrar todos os pontos de início das falas
indices = []
for match in adriana_inicio.finditer(texto):
    indices.append((match.start(), "adriana"))
for match in lodovico_inicio.finditer(texto):
    indices.append((match.start(), "lodovico"))

# Ordenar por posição no texto
indices.sort()

# Adicionar final do texto como último índice
indices.append((len(texto), None))

# Separar falas
falas_adriana = []
falas_lodovico = []

for i in range(len(indices) - 1):
    inicio, pessoa = indices[i]
    fim = indices[i + 1][0]
    fala = texto[inicio:fim].strip()
    if pessoa == "adriana":
        falas_adriana.append(fala)
    elif pessoa == "lodovico":
        falas_lodovico.append(fala)

# Salvar arquivos
with open("adriana.txt", "w", encoding="utf-8") as f:
    f.write("\n\n".join(falas_adriana))

with open("lodovico.txt", "w", encoding="utf-8") as f:
    f.write("\n\n".join(falas_lodovico))

print("Falas separadas em adriana.txt e lodovico.txt.")