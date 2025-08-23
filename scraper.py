from bs4 import BeautifulSoup

with open('pagina.html', 'r', encoding='latin-1') as f:
    conteudo_html = f.read()

soup = BeautifulSoup(conteudo_html, 'html.parser')

lista_produtos = soup.find_all('div', class_='col s12 m4')

print(f"encontrados {len(lista_produtos)} produtos na página.")
print("___")

for produto in lista_produtos:
    try:
        nome_elemento = produto.find('span', class_='card-title tooltipped truncate tb-valor-18')
        preco_elemento = produto.find('p', class_='tb-valor-25 indigo-text text-darken-4 padding10')
        loja_elemento = produto.find('p', class_='truncate tooltipped padding10')

        if nome_elemento and preco_elemento and loja_elemento:
            nome = nome_elemento.text.strip()
            preco = preco_elemento.text.strip()
            loja = loja_elemento.text.strip()

            print(f"Produto: {nome}")
            print(f"Preço: {preco}")
            print(f"Loja: {loja}")
            print("___")
    except Exception as e:
        print(f"Erro ao processar algum produto: {e}")