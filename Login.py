from PySimpleGUI import PySimpleGUI as sg
# Layout
sg.theme('DarkPurple')
layout = [
    [sg.Text('Usuário'),sg.Input(key='Usuário', size=(20,1))],
    [sg.Text('Senha '),sg.Input(key='Senha ',password_char='*',size=(21,1))],
    [sg.Checkbox('Salvar o Login?')],
    [sg.Button('Entrar')]
]

# Janela
janela = sg.Window('LOGIN', layout)

# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['Usuário'] == 'Sant' and valores['Senha '] == '123456':
            print('Bem vindo ao programa!')
