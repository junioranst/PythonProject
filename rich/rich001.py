from rich import print
from rich.panel import Panel
print('Ola [red]mundo[/] :earth_americas:')
print('You are male :male_sign:')
print(':+1:')
caixa = Panel('[white]Error you did it wrong![/]', title='Message', width=50, style='red')
print(caixa)

caixa1 = Panel('Error you did it wrong!', title='Message', width=50, style='green')
print(caixa1)