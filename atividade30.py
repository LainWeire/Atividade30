# crie uma duncao que calcule a nota a media de 3 notas em seguida verifique se ele esta aprovado ou reprovado para notas acima de 7
def media(nota1, nota2, nota3):
    med = ((nota1 + nota2 + nota3) / 3)
    if med > 7:
        print (f"Com a média de {med}, o aluno está APROVADO.")
    elif med < 7:
        print (f"Com a média de {med}, o aluno está REPROVADO.")
    else:
        print ("Uff referencias 🔥🔥")
    return med


def verificar_resultados(media):
    if media >= 7:
        return 'Aprovado'
    else:
        return 'Reprovado'


nota1 = float(input("Digite a 1° nota: "))
nota2 = float(input("Digite a 2° nota: "))
nota3 = float(input("Digite a 3° nota: "))



resultado_media = media(nota1, nota2, nota3)
print(resultado_media)

resultado_final = verificar_resultados(resultado_media)
print(resultado_final)