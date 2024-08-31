texto = "CursO de Python"

setima_posicao_texto = texto[6]
print(setima_posicao_texto)

texto_curso = texto[:5]
print(texto_curso)

texto_python = texto[9:]
print(texto_python)

#Contar o número de caracteres dentro do texto
qtd_char = len(texto)
print(f"Na frase temos {qtd_char} caracteres")

#Contar um número específico de letras dentro do texto
letra = "o"
qtd_letras_o = texto.count("o")
print(f"Na frase temos {qtd_letras_o} letras {letra}")

#Identifica a posição onde inicia uma palavra
palavra = "Python"
posicao_palavra = texto.find(palavra)
print(f"A palavra {palavra} inicia na posição {posicao_palavra}")

#Identifica se existe a palavra no texto
verifica_palavra = palavra in texto  
print(f"A palavra {palavra} esta no texto ? {verifica_palavra}")








