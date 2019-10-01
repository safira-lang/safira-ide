# Exibir conteúdo na tela
# nova mudança
def mostre(conteudo): # "string" ou numero {tem que ser algo definido}
    try:
        print(conteudo)
    except Exception as erro:
        print(erro)
        print("Reporte esse bug aos desenvolvedores.")

# retorna True ou False
def condicional(valor1,operacao,valor2): # O valor tem que estar tratado ( valor,operacao,valor )
    operacao = operacao.strip()

    if operacao == "==":  # igualdade
        try:
            if valor1 == valor2:
                return True
            else:
                return False
        except Exception as erro:
            return "[Erro] {}".format(erro)

    elif operacao == "<": # menor que 
        try:
            if valor1 < valor2:
                return True
            else:
                return False
        except Exception as erro:
            return "[Erro] {}".format(erro)

    elif operacao == ">": # maior que
        try:
            if valor1 > valor2:
                return True
            else:
                return False
        except Exception as erro:
            return "[Erro] {}".format(erro)

    elif operacao == "!=":# diferente de
        try:
            if valor1 != valor2:
                return True
            else:
                return False
        except Exception as erro:
            return "[Erro] {}".format(erro)

    else:
        return "[Erro] uma operação inválida foi repassada ao interpretador"


print(condicional(1,'==',1),'\n\n')

# Realiza contas
def operacoes(valor1,operacoes,valor2):

    if str(valor1).isnumeric() == False or str(valor2).isnumeric() == False:
        return "[Erro] caracteres inválidos foram repasados ao interpretador. ({}) e ({}) deveriam ser numéricos".format(valor1,valor2)

    if operacoes == "+":
        try:
            retorno = valor1 + valor2
        except Exception as erro:
            return "[Erro] Não foi possivel somar {} por {}. Erro = {}".format(valor1,valor2,erro)
        else:
            return retorno

    elif operacoes == "-":
        try:
            retorno = valor1 - valor2
        except Exception as erro:
            return "[Erro] Não foi possivel subtrair {} por {}. Erro = {}".format(valor1,valor2,erro)
        else:
            return retorno

    elif operacoes == "/":
        try:
            retorno = valor1 / valor2
        except ZeroDivisionError:
            return "[Erro] Você não pode dividir um número por 0"

        except Exception as erro:
            return "[Erro] Não foi possivel dividir {} por {}. Erro = {}".format(valor,valor2,erro)

        else:
            return retorno

    elif operacoes == "//":
        try:
            retorno = valor1 // valor2
        except Exception as erro:
            return "[Erro] Não foi possivel obter o resto de {} pelo valor {}. Erro = {}".format(valor1,valor2,erro)
        else:
            return retorno

    elif operacoes == "*":
        try:
            retorno = valor1 * valor2
        except Exception as erro:
            return "[Erro] Não foi possivel multiplicar {} pelo {}. Erro = {}".format(valor1,valor2,erro)
        else:
            return retorno

    elif operacoes == "**":
        try:
            retorno = valor1 ** valor2
        except Exception as erro:
            return "[Erro] Não foi possivel elevar {} ao {}. Erro = {}".format(valor1,valor2,erro)
        else:
            return retorno

    else:
        return "Nenhuma operacoes válida foi repadassada. O interpretador Falhou"

print('01',operacoes(10,"+",222))
print('02',operacoes(10,"-",222))
print('03',operacoes(10,"/",222))
print('04',operacoes(0,"/",0))
print('05',operacoes(0,"//",22))
print('06',operacoes(10,"*",222))
print('07',operacoes(10,"**",2))
print('08',operacoes(10,"",222),'\n\n')

def operacoes_fatorial(valor):
    if str(valor).isnumeric() == False:
        return "[Erro] É necessário passar valores numéricos ao interpretador! foi passado ({})".format(valor)
    
    try:
        for andante in range(valor-1):
            valor = valor * (andante+1)

    except Exception as erro:
        return "[Erro] Erro {}".format(erro)
    else:
        return valor

print('a',operacoes_fatorial(5))
print('b',operacoes_fatorial("5"))
print('c',operacoes_fatorial("A"),'\n\n')
