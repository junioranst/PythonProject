from rich import print
from rich.table import Table

tabela = Table(title='Itens')
tabela.add_column('Objeto')
tabela.add_column('Valor', justify='center', style='blue')
tabela.add_row('lapis', '10')
tabela.add_row('caneta', '10')
print(tabela)
