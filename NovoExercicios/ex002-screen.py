from customtkinter import *

def clique():

    if email.get() == '' or senha.get() == '':
        mensagem_retorno.configure(text='Preencha todos os campos',text_color='white')

    elif email.get() == 'adriano@gmail.com' and senha.get() == 'cavalo':
        if checkbox.get() == 1:
            mensagem_retorno.configure(text='Login Aprovado(Senha Salva)', text_color='green')
        else:
            mensagem_retorno.configure(text='Login Aprovado', text_color='green')

    else:
        mensagem_retorno.configure(text='Login Negado', text_color='red')



janela = CTk()
janela.geometry('350x320')

texto = CTkLabel(janela,text='Fazer Login')
texto.pack(padx=10, pady=10)

email = CTkEntry(janela, placeholder_text='Digite seu Email')
email.pack(padx=10, pady=10)

senha = CTkEntry(janela, placeholder_text='Digite sua Senha',show='*')
senha.pack(padx=10, pady=10)

checkbox = CTkCheckBox(janela,text='Lembrar Senha')
checkbox.pack(padx=10, pady=10)

botao = CTkButton(janela, text='Enter', command=clique)
botao.pack(padx=10, pady=10)

mensagem_retorno = CTkLabel(janela, text='')
mensagem_retorno.pack(padx=10, pady=10)


janela.mainloop()