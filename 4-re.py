import re

text = "Udemy - uma plataforma com muitos cursos"
# 1 - Indice inicial e final de palavras
# 0 r significa uma raw string ( string Bruta)
match = re.search(r'muitos cursos', text)
print(f"Indice inicial : {match.start()}")
print(f"Indice final : {match.end()}")


# 2 - Buscando o indice que possui o ponto 
site = 'https://udemy.com'
match = re.search(r'\.', site)
print(match)

# 3 - Buscando uma lista de caracteres dentro de uma frase 
pattern = "[a-m]"
result = re.findall(pattern, text)
print(result)

# 4 - verificando o inicio de uma string
rule = r'^A'
phrases = ['A casa esta suja', 'O dia esta lindo ', 'Vamos passear']
for f in phrases:
    if re.match(rule, f):
        print(f"corresponde : {f}")
    else:
        print(f"nao corresponde: {f}")

# 5 - Verificando o final de uma string 
rule_end = r'!$'
phrases2 = "O dia esta lindo!"
match = re.search(rule_end, phrases2)
if match:
    print("sim, corresponde")
else:
    print("nao corresponde")