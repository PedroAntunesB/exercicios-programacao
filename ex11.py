class Produto:
    def __init__(self, codigo, nome, preco, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def adicionar_estoque(self, quantidade):
        self.quantidade += quantidade

    def retirar_estoque(self, quantidade):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
        else:
            print("Quantidade maior que o estoque disponível.")

    def alterar_preco(self, novo_preco):
        self.preco = novo_preco

    def valor_total(self):
        return self.preco * self.quantidade


produto1 = Produto(1, "Teclado", 100, 10)
produto2 = Produto(2, "Mouse", 50, 20)
produto3 = Produto(3, "Monitor", 800, 5)

produto1.adicionar_estoque(5)
produto2.retirar_estoque(3)
produto3.alterar_preco(750)

print(produto1.nome, produto1.quantidade, produto1.valor_total())
print(produto2.nome, produto2.quantidade, produto2.valor_total())
print(produto3.nome, produto3.quantidade, produto3.valor_total())