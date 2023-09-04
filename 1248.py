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



arvore = Arvore()
valores = [5, 3, 7, 2, 4, 6, 8]
for valor in valores:
    arvore.inserir_em_nivel(valor)

altura = arvore.altura()
print(f"Altura da árvore: {altura}")
print("Travessia Inordem:", arvore.travessia_inordem())
print("Travessia Pré-ordem:", arvore.travessia_preordem())
print("Travessia Pós-ordem:", arvore.travessia_posordem())
print("Travessia em Níveis:", arvore.travessia_em_niveis())