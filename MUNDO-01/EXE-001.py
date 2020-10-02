import PySimpleGUI as sg

class App:
    def __init__(self):
        layout = [
            [sg.Text('Olá, Mundo!')]
        ]   

        self.windows = sg.Window('Primeiro Programa', layout)

    def iniciar(self):
        win = self.windows
        while True:
            events, values = win.read()

            if events == sg.WINDOW_CLOSED:
                break

        win.close()

aplicativo = App()
aplicativo.iniciar()
    