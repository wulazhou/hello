import PySimpleGUI as sg

layout = [[sg.Text('some text on row 1')], [sg.Text('Enter something on row 2'), sg.InputText()],
          [sg.Button('ok'), sg.Button('cancel')]]
window =sg.Window('window title',layout)
while True:
    event,values =window.read()
    if event in (None,'cancel'):
        break
    print('you entered ',values[0])

window.close()