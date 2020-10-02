import PySimpleGUI as sg

class App:
    def __init__(self):
        layout = [
            [sg.Text('Primeiro número:' ), sg.Input(key='num1')],
            [sg.Text('Segundo número: '), sg.Input(key='num2')],
            [sg.Button('OK'), sg.Button('Cancel')]
        ]
        self.win = sg.Window('EXE-003', layout)

    def gerador(self)

        while True:

            events, values = self.win.read()

            if events in (sg.WINDOW_CLOSED, 'Cancel'):
                break

            elif events == 'OK':
                num1 = int(values['num1'])
                num2 = intgoog(values['num2'])
                sg.popup(f'A Soma dos valores {num1} + {num2} = {num1 + num2}')

        self.win.close()        

aplic = App()
aplic.gerador()

