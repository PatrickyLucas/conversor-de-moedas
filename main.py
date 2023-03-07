import PySimpleGUI as sg
from cotacao import pegar_cotacao

moedas = [['USD'], ['EUR'], ['BTC']]

layout = [
    [sg.Text('Pegar Cotação da Moeda', font=('Bold', 18), justification='CENTER')],
    [sg.Text('Escolha a moeda:', justification='left', font=('', 12), size=23),sg.OptionMenu(values=moedas, key='nome_cotacao', background_color='lightblue', text_color='blue')],
    [sg.Text('Qual valor para conversão: R$', font=('', 12)), sg.InputText(key='valor_para_conversao', size=10)],
    [sg.Button('Pegar Cotação', button_color="green", size=(20,2)), sg.Button('Cancelar', button_color="red", size=(10,2))],
    [sg.Text('', key='texto_cotacao', font=('', 12))],
    [sg.Text('', key='texto_conversao', font=('', 14))]
]



janela = sg.Window('Conversor de Moedas', layout=layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == 'Cancelar':
        break
    if evento == 'Pegar Cotação':
        codigo_cotacao = valores['nome_cotacao']
        codigo_cotacao = codigo_cotacao.replace("('", '')
        codigo_cotacao = codigo_cotacao.replace("',)", '')
        cotacao = pegar_cotacao(codigo_cotacao)
        cotacao = float(cotacao)
        valor_para_conversao = valores['valor_para_conversao']
        valor_para_conversao = float(valor_para_conversao.replace(',', '.')) / cotacao
        janela['texto_cotacao'].update(f'A cotação do {codigo_cotacao} é de R${cotacao:.2f}')
        janela['texto_conversao'].update(f'O valor convertido é de $ {valor_para_conversao:.2f} {codigo_cotacao}')


janela.close()