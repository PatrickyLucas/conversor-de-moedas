import requests

def pegar_cotacao(codigo_moeda):
    try:
        requisicao = requests.get(f'http://economia.awesomeapi.com.br/last/{codigo_moeda}-BRL')
        requisicao_dic = requisicao.json()
        cotacao = requisicao_dic[f'{codigo_moeda}BRL']['bid']
        return cotacao
    except:
        print('Código da moeda inválido!')
        return None

