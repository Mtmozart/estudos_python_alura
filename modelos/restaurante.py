from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self) -> str:
        return f'{self._nome} | {self.categoria}'
    '''Toda vez que for um método da classe, tenho que usar essa anotação
    e por convenção o cls, pois precisa só da classe para acessar
    '''
    @classmethod
    def listar_restaurantes(cls):
       print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'.ljust(25)} |{'Média'}")
       for restaurante in cls.restaurantes:
           print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo.ljust(25)} | {str(restaurante.media_avaliacoes)}')
    '''Modifica o valor que será lido, falando mais amplamente, poderia fazer qualquer coisa aqui
       cool symbols: https://coolsymbol.com/ 
    '''
    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'

    def alternar_estado(self):
        self._ativo = not self._ativo
    
    def receber_avaliacao(self, client, note):
        try:
            if 0 <= note <= 5:
                avaliacao = Avaliacao(client, note)
                self._avaliacao.append(avaliacao)
            else:
                raise ValueError('A nota não pode ser maior que 5.')
        except ValueError as e:
            print(f"Erro de valor: {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")


    @property
    def media_avaliacoes(self):
        if not self._avaliacao: 
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        return round(soma_das_notas / quantidade_de_notas, 1)
       

        