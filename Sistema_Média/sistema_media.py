print("\n\n==== VERIFICAÇÃO DE NOTAS DOS ESTUDANTES ==== \n")


def cad_nota():
    nome = input("Digite o nome do Aluno: ")
    while nome.isnumeric():
        print("\n\nOPS, OCORREU UM ERRO TENTE NOVAMENTE, O nome deve conter apenas letras! Tente novamente.\n\n")
        cad_nota()
        continue
    nota1 = float((input(f"Digite o Valor da primeira nota do(a) {nome}: ")))
    nota2 = float((input(f"Digite o valor da segunda nota do(a) {nome}: ")))
    nota3 = float((input(f"Digite o valor da terceira nota do(a) {nome} ")))
    nota4 = float((input(f'Digite o valor da quarta nota do(a) {nome} ')))
    media = float((nota1 + nota2 + nota3 + nota4) / 4)
    while (media > 10) or (media < 0):
        print("\nOPS, ALGO DEU ERRADO, Verifique os valores e tente novamente, A média não pode ser menor que 0 ",
              end=" ")
        print("e nem maior que 10. Tente novamente!\n\n")
        cad_nota()
        continue

    if (media >= 0) and (media <= 4.5):
        print(f"\n As notas do(a) {nome} são: Primeira: {nota1:.2f}, Segunda: {nota2:.2f}, Terceira: {nota3:.2f} e ",
              end=" ")
        print(f"Quarta {nota4:.2f}.")
        print(f" A média dele(a) é: {media:.2f}")
        print(f" O(A) Aluno(a) está reprovado!")
        exit()
    else:
        print(f"\n As notas do(a) {nome} são: Primeira: {nota1:.2f}, Segunda: {nota2:.2f}, Terceira: {nota3:.2f} e ",
              end=" ")
        print(f"Quarta {nota4:.2f}.")
        print(f" A média dele(a) é: {media:.2f}")
        print(f" O(A) Aluno(a) foi Aprovado!")

    print('\nObrigado por usar nosso Sistema, Buscaremos sempre nos aperfeiçoar!')
    exit()


cad_nota()
