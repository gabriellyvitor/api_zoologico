import unittest

class TestZoo(unittest.TestCase):
    def test_criar_animal(self):
        animal = Animal("Simba", "Leão", 5)
        self.assertEqual(animal.nome, "Simba")
        self.assertEqual(animal.especie, "Leão")
        self.assertEqual(animal.felicidade, 5)

    def test_alimentar_animal(self):
        animal = Animal("Simba", "Leão", 5)
        animal.alimentar(3)
        self.assertEqual(animal.felicidade, 8)

    def test_adicionar_animal_recinto(self):
        recinto = Recinto("Leão")
        animal = Animal("Simba", "Leão", 5)
        recinto.adicionar_animal(animal)
        self.assertIn(animal, recinto.animais)

    def test_receber_visitantes(self):
        zoo = Zoo()
        recinto = Recinto("Leão")
        animal = Animal("Simba", "Leão", 5)
        recinto.adicionar_animal(animal)
        zoo.adicionar_recinto(recinto)
        zoo.receber_visitantes(100)
        self.assertGreater(zoo.dinheiro, 0)

if __name__ == '__main__':
    unittest.main()
