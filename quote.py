import requests ## faz a requisição ao endereço da internet e obtem o conteudo da página (html)
from bs4 import BeautifulSoup ## biblioteca que transforma o html em um obejto python

pagina = requests.get('https://quotes.toscrape.com/') ## obtem o conteudo (html) da pgina
dados_pagina = BeautifulSoup(pagina.text, 'html.parser') ## tratar os dados da pagina usando a beatifulsoup(conteudo da pagina, parser=mecanismo de traducao do html pra um objeto python)

todas_frases = dados_pagina.find_all('span', itemprop="text") ## filtra todas as divs da pagina e depois procura todas as classes quote nelas

for div in todas_frases:
    print(div.text) 
