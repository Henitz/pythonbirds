from unittest import TestCase
from oo.carro import Motor


class CarroTestCase(TestCase):
    def test_velocidade_inicial(selfself):
        motor = Motor()
        self.assertEqual(0,motor.velocidade)