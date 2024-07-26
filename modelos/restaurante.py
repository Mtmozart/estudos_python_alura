class Restaurante:
    restaurantes = []
    
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self) -> str:
        return f'{self._nome} | {self.categoria}'
    '''Toda vez que for um método da classe, tenho que usar essa anotação
    e por convenção o cls, pois precisa só da classe para acessar
    '''
    @classmethod
    def listar_restaurantes(cls):
       print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}")
       for restaurante in cls.restaurantes:
           print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')
    '''Modifica o valor que será lido, falando mais amplamente, poderia fazer qualquer coisa aqui
       cool symbols: https://coolsymbol.com/ 
    '''
    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'

    def alternar_estado(self):
        self._ativo = not self._ativo


restaurate_praca = Restaurante('Praça', 'Gourmet');
restaurate_praca.alternar_estado()
restaurate_pizza = Restaurante('Pizza', 'Podrão');


Restaurante.listar_restaurantes()


