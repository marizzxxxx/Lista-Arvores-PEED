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

    def altura(self):
        return self.altura_recursiva(self.raiz)

    def altura_recursiva(self, no):
        if no is None:
            return 0
        altura_esquerda = self.altura_recursiva(no.esquerda)
        altura_direita = self.altura_recursiva(no.direita)
        return max(altura_esquerda, altura_direita) + 1

    def travessia_inordem(self):
        valores = []
        self.travessia_inordem_recursiva(self.raiz, valores)
        return valores

    def travessia_inordem_recursiva(self, no, valores):
        if no is not None:
            self.travessia_inordem_recursiva(no.esquerda, valores)
            valores.append(no.valor)
            self.travessia_inordem_recursiva(no.direita, valores)

    def travessia_preordem(self):
        valores = []
        self.travessia_preordem_recursiva(self.raiz, valores)
        return valores

    def travessia_preordem_recursiva(self, no, valores):
        if no is not None:
            valores.append(no.valor)
            self.travessia_preordem_recursiva(no.esquerda, valores)
            self.travessia_preordem_recursiva(no.direita, valores)

    def travessia_posordem(self):
        valores = []
        self.travessia_posordem_recursiva(self.raiz, valores)
        return valores

    def travessia_posordem_recursiva(self, no, valores):
        if no is not None:
            self.travessia_posordem_recursiva(no.esquerda, valores)
            self.travessia_posordem_recursiva(no.direita, valores)
            valores.append(no.valor)

    def travessia_em_niveis(self):
        valores = []
        if self.raiz is not None:
            fila = [self.raiz]
            while fila:
                no = fila.pop(0)
                valores.append(no.valor)
                if no.esquerda is not None:
                    fila.append(no.esquerda)
                if no.direita is not None:
                    fila.append(no.direita)
        return valores

    def contar_nos(self):
        return self.contar_nos_recursivo(self.raiz)

    def contar_nos_recursivo(self, no):
        if no is None:
            return 0
        return 1 + self.contar_nos_recursivo(no.esquerda) + self.contar_nos_recursivo(no.direita)

    def encontrar_maximo(self):
        if self.raiz is None:
            return None
        no_atual = self.raiz
        while no_atual.direita is not None:
            no_atual = no_atual.direita
        return no_atual.valor

    def e_arvore_de_busca(self):
        return self.e_arvore_de_busca_recursiva(self.raiz, float('-inf'), float('inf'))

    def e_arvore_de_busca_recursiva(self, no, min_valor, max_valor):
        if no is None:
            return True
        if no.valor <= min_valor or no.valor >= max_valor:
            return False
        return (self.e_arvore_de_busca_recursiva(no.esquerda, min_valor, no.valor) and
                self.e_arvore_de_busca_recursiva(no.direita, no.valor, max_valor))

    def remover_valor(self, valor):
        self.raiz = self.remover_valor_recursivo(self.raiz, valor)

    def remover_valor_recursivo(self, no, valor):
        if no is None:
            return no

        if valor < no.valor:
            no.esquerda = self.remover_valor_recursivo(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self.remover_valor_recursivo(no.direita, valor)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            no.valor = self.encontrar_minimo_valor(no.direita)
            no.direita = self.remover_valor_recursivo(no.direita, no.valor)

        return no

    def encontrar_minimo_valor(self, no):
        while no.esquerda is not None:
            no = no.esquerda
        return no.valor

    def nos_no_nivel(self, nivel):
        nos = []
        self.nos_no_nivel_recursivo(self.raiz, nivel, nos)
        return nos

    def nos_no_nivel_recursivo(self, no, nivel, nos):
        if no is None:
            return
        if nivel == 0:
            nos.append(no.valor)
        else:
            self.nos_no_nivel_recursivo(no.esquerda, nivel - 1, nos)
            self.nos_no_nivel_recursivo(no.direita, nivel - 1, nos)

    def caminho_ate_no(self, valor):
        caminho = []
        if self.caminho_ate_no_recursivo(self.raiz, valor, caminho):
            return caminho
        return None

    def caminho_ate_no_recursivo(self, no, valor, caminho):
        if no is None:
            return False
        caminho.append(no.valor)
        if no.valor == valor:
            return True
        if (self.caminho_ate_no_recursivo(no.esquerda, valor, caminho) or
                self.caminho_ate_no_recursivo(no.direita, valor, caminho)):
            return True
        caminho.pop()
        return False

    def nos_filhos_do_no(self, valor):
        no_pai = self.encontrar_no(self.raiz, valor)
        if no_pai is not None:
            filhos = []
            if no_pai.esquerda is not None:
                filhos.append(no_pai.esquerda.valor)
            if no_pai.direita is not None:
                filhos.append(no_pai.direita.valor)
            return filhos
        return []

    def encontrar_no(self, no, valor):
        if no is None:
            return None
        if no.valor == valor:
            return no
        no_esquerda = self.encontrar_no(no.esquerda, valor)
        if no_esquerda is not None:
            return no_esquerda
        return self.encontrar_no(no.direita, valor)



arvore = Arvore()
valores = [5, 3, 7, 2, 4, 6, 8]
for valor in valores:
    arvore.inserir_em_nivel(valor)

print("\nAltura da árvore:", arvore.altura())
print("\nTravessia Inordem:", arvore.travessia_inordem())
print("Travessia Pré-ordem:", arvore.travessia_preordem())
print("Travessia Pós-ordem:", arvore.travessia_posordem())
print("Travessia em Níveis:", arvore.travessia_em_niveis())
print("\nNúmero total de nós:", arvore.contar_nos())
print("Valor máximo na árvore:", arvore.encontrar_maximo())
print("É uma árvore de busca válida?", arvore.e_arvore_de_busca())

arvore.remover_valor(3)
print("\nTravessia Inordem após remover o valor 3:", arvore.travessia_inordem())
print("Nós no nível 2:", arvore.nos_no_nivel(2))
print("Caminho até o valor 6:", arvore.caminho_ate_no(6))
print("Nós filhos do valor 7:", arvore.nos_filhos_do_no(7))