import re

# Texto de exemplo que contém URLs
texto_html = """..
  Visite o nosso site em https://www.exemplo.com.
  Para mais informações, acesse http://www.outroexemplo.com/pagina.
  Conheça nosso patrocinador oficial https://www.sitedasuaempresa.com.br.
"""

# Expressão Regular para encontrar URLs
padrao = r'https?:\/\/[^\s]+'

# Usando a função findall() para extrair as URLs
urls_encontradas = re.findall(padrao, texto_html)

# Imprime as URLs encontradas
if urls_encontradas:
    print("URLs encontradas:")
    for index, url in enumerate(urls_encontradas, start=1):
        print(f"{index}: {url}")
else:
    print("Nenhuma URL encontrada.")

# Neste código, utilizamos a expressão regular https?:\/\/[^\s]+ para encontrar URLs. Vamos explicar o que cada parte da Expressão Regular faz:

# https? : corresponde ao protocolo "http" ou "https". O ? torna o "s" opcional.
# :\/\/: corresponde aos dois pontos e às duas barras que seguem o protocolo em uma URL.
# [^\s]+: corresponde a um ou mais caracteres que não são espaços em branco. Isso garante que a URL seja capturada até o próximo espaço em branco.
# O modificador g é usado para encontrar todas as correspondências no texto, não apenas a primeira.
# O módulo re é usado para compilar a Expressão Regular e, em seguida, a função findall() é usada para encontrar todas as correspondências no texto.

# Ao executar o código acima, ele imprimirá todas as URLs encontradas no texto de exemplo. Lembre-se que utilizamos uma expressão regular básica e o código não utiliza bibliotecas mais especializadas na extração de dados.

# Os benefícios estão relacionados a redução de tempo, custos e maior produtividade, pois assim as pessoas podem priorizar outras tarefas.