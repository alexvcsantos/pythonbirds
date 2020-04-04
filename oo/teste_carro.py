#para projetos complexos é melhor usar esta forma de test, o doctest é pra projetos pequenos
from unittest import TestCase

from oo.carro import Motor


class CarroTestCase(TestCase):
    def teste_velocidade_inicial(self):#sempre começar o teste com palavra test
        motor = Motor()
        self.assertEqual(0,motor.velocidade)

    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)
