from service.gerador_de_calculos import GeradorCalculos

if __name__ == '__main__':
    gerador = GeradorCalculos()
    exercicios = gerador.gerar_exercicios(qtd_exercicios=15)
for exercicio in exercicios:
    print(" ", exercicio.recupera_primeiro_numero_formatado(), end="\n")
    print(exercicio.recupera_operador().value, exercicio.recupera_segundo_numero_formatado(), end="\n")
    print("﹉﹉﹉﹉")
    print("", end="\n")
