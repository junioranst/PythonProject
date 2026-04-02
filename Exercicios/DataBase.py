import matplotlib.pyplot as plt

class perfil:
    def __init__(self, name, country, birth, fgun):
        self.name = name
        self.country = country
        self.birth = birth
        self.fgun = fgun

    def __str__(self):
        return f'{self.name} {self.country} {self.birth} {self.fgun}'

    def __repr__(self):
        return f'{self.name} {self.country} {self.birth} {self.fgun}'

library = []

def add_perfil():
    name = input('Nome do perfil: ')
    country = input('Country do perfil: ')
    birth = int(input('Birth do perfil: '))
    fgun = input('FGUN do perfil: ')
    library.append(perfil(name, country, birth, fgun))
    print('Perfil added successfully!')

def list_profiles():
    for perfil in library:
        print(perfil)

def list_profiles():
    if not library:
        print("Nenhum perfil cadastrado!")
    for perfil in library:
        print(perfil)

def gun_grafic():
    if not library:
        print('Profile on database not found!')
        return
    gunchoice = {}
    for perfil in library:
        if perfil.fgun in gunchoice:
            gunchoice[perfil.fgun] += 1
        else:
            gunchoice[perfil.fgun] = 1

    guns = list(gunchoice.keys())
    quantity = list(gunchoice.values())

    plt.bar(guns, quantity, color='royalblue')
    plt.xlabel("Guns")
    plt.ylabel("Quantities")
    plt.title(" Guns preferences graphic")
    plt.show()

while True :
    print('\nMain Menu')
    print('Press 1 - to add a new perfil')
    print('Press 2 - to list all perfils')
    print('Press 3 - to Open a graphical profile')
    print('Press 4 - to quit\n')
    option = int(input('Enter your choice: '))

    if option == 1:
        add_perfil()

    elif option == 2:
        list_profiles()

    elif option == 3:
        gun_grafic()

    elif option == 4:
        break





