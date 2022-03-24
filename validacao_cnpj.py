fim = 'https://www.google.com/search?q=answer+to+life+the+universe+and+everything&oq=answer+&aqs=chrome.5.69i57j0i433i512j0i512j0i131i433i512l2j0i512j0i131i433i512j0i512l3.8595j0j4&sourceid=chrome&ie=UTF-8'

while fim != 'fim':
    # Variaveis
    parametros = ".-qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_=+{}[]|'';:/?>,<`~"
    indice = 0
    conta = 10
    cnpj_separado = []
    num_valida = []
    num = 0
    conta = 10
    resultado = 0
    pergunta_fim = 0
    certo = 'not ok'

    #Funcoes
    def conta(cnpj):
        global cnpj_separado
        resultado = 0
        if len(cnpj_separado) == 13:
            valor = 6
            for z in cnpj:
                resultado += int(z) * valor
                if valor == 2:
                    valor = 9
                else:
                    valor -= 1
        else:
            valor = 5
            for z in cnpj:
                resultado += int(z) * valor
                if valor == 2:
                    valor = 9
                else:
                    valor -= 1

        num = 11 - (resultado % 11)
        if num > 9:
            cnpj_separado.append(0)
        else:
            cnpj_separado.append(num)

    #Validar se o usuario vai digitar certo
    while certo != 'ok':

        #Receber o cnpj
        cnpj = input("digite o seu cnpj: ")

        #Remover os pontos e o traco do cnpj
        for x in range(len(parametros)):
            cnpj = cnpj.replace(parametros[x],"")

        if len(cnpj) == 14:
            certo = 'ok'
        else:
            pass
    #Separar os numeros
    for valor in cnpj:
        if indice < 12:
            cnpj_separado.insert(indice, cnpj[indice])
            indice += 1
        else:
            num_valida.insert(num, cnpj[indice])
            indice += 1
            num += 1
    #Contas
    conta(cnpj_separado)
    conta(cnpj_separado)

    #Validacao
    if int(num_valida[0]) == cnpj_separado[-2]:
        if int(num_valida[1]) == cnpj_separado[-1]:
            print('Tudo certo, este cnpj esta certo')
        else:
            print('Cnpj invalido')
    else:
        print('Cnpj invalido')

    #Perguntar se o usuario vai querer fazer outra validacao
    while pergunta_fim == 0:
        outra_vez = input('Voce quer validar outro Cnpj? ')
        if outra_vez[0] == 'S' or outra_vez[0] == 's':
            pergunta_fim = 1
        elif outra_vez[0] == 'N' or outra_vez[0] == 'n':
            pergunta_fim = 1
            fim = 'fim'
        else:
            pass

print('Obrigado por usar o nosso programa')