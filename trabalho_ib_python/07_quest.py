aluno=input("nome do aluno: ")
conponenteCuricular=input("materia em questão:  ")
nota1=int(input("primeira nota do bimestre: "))
nota2=int(input("segunda nota dobimestra: "))
media=(nota1+nota2)/2
if media>=6:        
    print(f' o estudante  {aluno}  está aprovado na materia de {conponenteCuricular} com a madia {media}')
else :
    print(f'estudante   {aluno}  está reprovado na materia de {conponenteCuricular} com a media {media}')





