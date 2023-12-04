import pandas as pd

url = "FPOO-Formativa-WebScraping_E-commerce.html"
tabela = pd.read_html(url, encoding='utf-8')
type(tabela)
print(tabela)
df = tabela[0]

df.to_csv('historico_pedidos.csv', index=False, encoding='utf-8-sig')
df.to_excel('historico_pedidos.xlsx', index=False)
df.to_json('historico_pedidos.json', orient='records', lines=True, force_ascii=False)
