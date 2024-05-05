class Animal:
    def __init__(self, nome, especie, felicidade):
        self.nome = nome
        self.especie = especie
        self.felicidade = felicidade

    def alimentar(self, incremento):
        self.felicidade += incremento

class Recinto:
    def __init__(self, especie, animais=None, bem_cuidado=True):
        self.especie = especie
        self.animais = animais if animais else []
        self.bem_cuidado = bem_cuidado

    def adicionar_animal(self, animal):
        if animal.especie == self.especie:
            self.animais.append(animal)

    def alterar_cuidado(self, estado):
        self.bem_cuidado = estado

class Zoo:
    def __init__(self):
        self.recintos = []
        self.dinheiro = 0

    def adicionar_recinto(self, recinto):
        self.recintos.append(recinto)

    def alimentar_animais(self, recinto, incremento):
        for animal in recinto.animais:
            animal.alimentar(incremento)

    def receber_visitantes(self, num_visitantes):
        taxa_felicidade = sum(animal.felicidade for recinto in self.recintos for animal in recinto.animais)
        taxa_cuidado = sum(1 for recinto in self.recintos if recinto.bem_cuidado)
        self.dinheiro += (taxa_felicidade + taxa_cuidado) * num_visitantes
