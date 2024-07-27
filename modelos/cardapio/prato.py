from modelos.cardapio.item_cardapio import ItemCardapio

class Prato:
  def __init__(self, nome, preco, descricao):
      super().__init__(nome, preco)
      self.descricao = descricao  