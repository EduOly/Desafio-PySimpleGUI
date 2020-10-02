import PySimpleGUI as sg 

class App:
    def __init__(self):
        layout = [
            [sg.Text('Digite seu nome:')],
            [sg.Input(key='-IN-')],
            [sg.Button('Enviar')]
        ]

        self.windows = sg.Window('EXE-002', layout)

    def iniciar(self):
        win = self.windows
        while True:
            events, values = win.read()
            if events == sg.WINDOW_CLOSED:
                break
            nome = values['-IN-']

            sg.popup(f'Seja bém vindo {nome} !')

aplicativo = App()
aplicativo.iniciar()            