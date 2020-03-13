import random

class Estado:
    pilha1 = []
    pilha2 = []
    pilha3 = []
    #pai = 

    def __init__(self):
        print(self.pilha1,self.pilha2,self.pilha3)
    
    #Move um bloco
    def p1top2(self):
        if(self.pilha1):
            aux=self.pilha1.pop()
            print("Bloco", aux, "removido da pilha 1")
            self.pilha2.append(aux)
            print("Bloco", aux, "movido para a pilha 2")
    
    def p1top3(self):
        if(self.pilha1):
            aux=self.pilha1.pop()
            print("Bloco", aux, "removido da pilha 1")
            self.pilha3.append(aux)
            print("Bloco", aux, "movido para a pilha 3")

    def p2top1(self):
        if(self.pilha2):
            aux=self.pilha2.pop()
            print("Bloco", aux, "removido da pilha 2")
            self.pilha1.append(aux)
            print("Bloco", aux, "movido para a pilha 1")

    def p2top3(self):
        if(self.pilha2):
            aux=self.pilha2.pop()
            print("Bloco", aux, "removido da pilha 2")
            self.pilha3.append(aux)
            print("Bloco", aux, "movido para a pilha 3")

    def p3top1(self):
        if(self.pilha3):
            aux=self.pilha3.pop()
            print("Bloco", aux, "removido da pilha 3")
            self.pilha1.append(aux)
            print("Bloco", aux, "movido para a pilha 1")

    def p3top2(self):
        if(self.pilha3):
            aux=self.pilha3.pop()
            print("Bloco", aux, "removido da pilha 3")
            self.pilha2.append(aux)
            print("Bloco", aux, "movido para a pilha 2")


#Criando o Estado Inicial
blocos = ['A','B','C']
eI = Estado()
while(blocos):
    i = random.randint(0,(len(blocos)-1))
    aux = blocos.pop(i)
    i = random.randint(1,3)
    if(i==1):
        eI.pilha1.append(aux)
        print("Bloco", aux, "movido para a pilha 1")
    elif(i==2):
        eI.pilha2.append(aux)
        print("Bloco", aux, "movido para a pilha 2")
    elif(i==3):
        eI.pilha3.append(aux)
        print("Bloco", aux, "movido para a pilha 3")
eI.__init__

abertos = []
fechados = []
abertos.append(eI)
f1 = Estado()
f1 = eI
f1.opr()
f1.__init__
abertos.append(f1)
print(abertos)

#ef = Estado()
#ef1 = eI.opr()
#ef2
#print(abertos)
