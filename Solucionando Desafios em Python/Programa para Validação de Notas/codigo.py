def notas_media(x, y):
    media = (x + y) / 2
    media = '%.2f' % media
    print('media =',media)


def notas_validas():
    x = float(input())
    if 0  <= x <= 10:
        return x
    else:
        print('nota invalida')
        return -1   # chamar a função de forma recursiva pode levar a um estouro de pilha se muitos valores inválidos forem digitados, 
                    # melhor retornar -1 direto e deixar o while chamar a função de novo

choice = 1
while choice == 1:
    j = -1
    k = -1
    while k==-1:
        k = notas_validas()
    while j==-1:
        j = notas_validas()
    notas_media(k,j)
    choice =3
    while choice<1 or choice>2:
        choice = int(input('novo calculo (1-sim 2-nao)\n')) # eval roda código válido em python que for digitado, 
                                                              # é um grande risco de segurança rodar em input do usuário