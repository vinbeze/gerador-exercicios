from model.calculo_simples import CalculoSimples
from enumerator.operador_enum import Operador
from typing import List
import random


class GeradorCalculos:
    def gerar_exercicios(self, qtd_exercicios: int) -> List[CalculoSimples]:
        lista_exercicios = []
        operadores = [Operador.SOMA, Operador.SUBTRACAO]
        while (len(lista_exercicios) <= qtd_exercicios):
            calculo = CalculoSimples(random.randint(0, 999), random.choice(operadores), random.randint(0, 999))
            if self.__valida_dificuldade(calculo):
                lista_exercicios.append(calculo)
            else:
                lista_exercicios.append(self.__inverte_ordem_numeral(calculo))
        return lista_exercicios

    def __valida_dificuldade(self, calculo: CalculoSimples) -> bool:
        if calculo.recupera_operador() is Operador.SUBTRACAO:
            return calculo.recupera_primeiro_numero() > calculo.recupera_segundo_numero()
        return True

    def __inverte_ordem_numeral(self, calculo: CalculoSimples) -> CalculoSimples:
        return CalculoSimples(calculo.recupera_segundo_numero(), calculo.recupera_operador(), calculo.recupera_primeiro_numero())
