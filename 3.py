class No:
    def __init__(self, valor=None):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir_em_nivel(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self.inserir_em_nivel_recursivo(valor, self.raiz)

    def inserir_em_nivel_recursivo(self, valor, no):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self.inserir_em_nivel_recursivo(valor, no.esquerda)
        else:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self.inserir_em_nivel_recursivo(valor, no.direita)

    def buscar_valor(self, valor):
        return self.buscar_valor_recursivo(valor, self.raiz)

    def buscar_valor_recursivo(self, valor, no):
        if no is None:
            return False
        if valor == no.valor:
            return True
        if valor < no.valor:
            return self.buscar_valor_recursivo(valor, no.esquerda)
        else:
            return self.buscar_valor_recursivo(valor, no.direita)



arvore = Arvore()
arvore.inserir_em_nivel(5)
arvore.inserir_em_nivel(3)
arvore.inserir_em_nivel(7)
arvore.inserir_em_nivel(2)
arvore.inserir_em_nivel(4)
arvore.inserir_em_nivel(6)
arvore.inserir_em_nivel(10)

print(arvore.buscar_valor(5))  
print(arvore.buscar_valor(3))  
print(arvore.buscar_valor(8)) 
print(arvore.buscar_valor(2)) 
print(arvore.buscar_valor(4)) 
print(arvore.buscar_valor(6)) 
print(arvore.buscar_valor(10)) 