#trocando palavra dentro de um texto 
texto = "RUTH PERES"
troca_palavra = texto.replace("PERES", "VIEIRA")
print(troca_palavra)

#trocando os caracteres para maiúsculo
texto = "RuPeres.sp@gmail.Com"
texto_maiusculo = texto.upper()
print(texto_maiusculo)

#trocando os caracteres para minusculo
texto = "RUpeRes.sp@gmail.COM"
texto_minusculo = texto.lower()
print(texto_minusculo)

#trocar a primeira letra de cada palavra em Maiúsculo
texto = "meu primeiro curso no senai"
primeira_letra = texto.title()
print(primeira_letra)

#trocar a primeira letra do texto para Maiúsculo
texto = "meu primeiro curso no senai"
primeira_l = texto.capitalize()
print(primeira_l)

#elimina espaços inúteis
texto = "     senai   "
print(f"A palavra {texto} tem {len(texto)} caracteres")

texto_strip = texto.strip()
print(f"A palavra {texto} tem {len(texto_strip)} caracteres")