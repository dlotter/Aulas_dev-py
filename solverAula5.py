class q1():
    def solucao(self):
        print("""Solução: Lembre-se que o return causa a saída da função imediatamente.


def divisivel_por_sete(nums):
    for num in nums:
        if num % 7 == 0:
            return True
    return False
""")

    def dica(self):
        print("Quantas vezes o corpo do loop roda para uma lista de tamanho n? Se você não tem certeza, tente adicionar um print() antes do if")

class q2():
    def solucao(self):
        print("""Uma possível solução:

def elemento_maior_que(L, numero):
    res = []
    for ele in L:
        res.append(ele > numero)
    return res
""")

class q3():
    def solucao(self):
        print("""Solution:

def menu_is_boring(meals):
    # Iterate over all indices of the list, except the last one
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False
        """)


    def dica(self):
        print("Esse é uma caso onde talvez seja preferível iterar sobre os indices da lista (usando o range) do que iterando sobre os elementos da própria lista")


