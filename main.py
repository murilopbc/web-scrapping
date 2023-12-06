# Importar a biblioteca pandas

import pandas as pd


# Declarar variável armazenando o caminho da página html

url = "FPOO-Formativa-WebScraping_E-commerce.html"

# Declarar uma variável 'tabela' para armazenar/ler as informações contidas

tabela = pd.read_html(url, encoding='utf-8')

# Especificar o que deseja buscar da página html

type(tabela)

# Exibir na tela

print(tabela)

# Assume que o primeiro elemento 'tabela' contém os dados desejados e o atribui à variável df

df = tabela[0]

# Salvar as informações em csv, xlsx e json

df.to_csv('historico_pedidos.csv', index=False, encoding='utf-8-sig')
df.to_excel('historico_pedidos.xlsx', index=False)
df.to_json('historico_pedidos.json', orient='records', lines=True, force_ascii=False)
