import matplotlib.pyplot as plt
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai']
vendas = [1500, 1800, 2200, 3000, 2500]

plt.bar(meses, vendas, color = 'royalblue')
plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.title('Vendas Mensais')
plt.show()