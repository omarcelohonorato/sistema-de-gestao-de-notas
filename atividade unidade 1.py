# Sistema de Gestão de Notas de Alunos
# Funções em Python

def cadastrar_notas():
    notas = []
    while True:
        try:
            nota = float(input("Digite a nota do aluno (ou -1 para encerrar): "))
            if nota == -1:
                break
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida! Digite entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Digite um número.")
    return notas

def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def exibir_relatorio(notas, media, situacao):
    print("\n===== RELATÓRIO FINAL =====")
    print(f"Notas inseridas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")

def main():
    print("=== Sistema de Gestão de Notas ===")
    notas = cadastrar_notas()
    media = calcular_media(notas)
    situacao = verificar_situacao(media)
    exibir_relatorio(notas, media, situacao)

main()