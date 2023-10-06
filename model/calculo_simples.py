from enumerator.operador_enum import Operador


class CalculoSimples:
    def __init__(self, primeiro_numero: int, operador: Operador, segundo_numero: int):
        self.__primeiro_numero = primeiro_numero
        self.__operador = operador
        self.__segundo_numero = segundo_numero

    def recupera_tamanho_maior_numero(self) -> int:
        if self.__primeiro_numero > self.__segundo_numero:
            return len(str(self.__primeiro_numero))
        return len(str(self.__segundo_numero))

    def recupera_primeiro_numero(self):
        return self.__primeiro_numero

    def recupera_segundo_numero(self):
        return self.__segundo_numero

    def recupera_operador(self):
        return self.__operador

    def recupera_primeiro_numero_formatado(self) -> str:
        return self.__formata_numero(self.__primeiro_numero)

    def recupera_segundo_numero_formatado(self) -> str:
        return self.__formata_numero(self.__segundo_numero)

    def __formata_numero(self, numero: int) -> str:
        return str(numero).rjust(self.recupera_tamanho_maior_numero(), " ")
