import random
import copy

class Estado:
    pilha1 = []
    pilha2 = []
    pilha3 = []
    pai = None

    #def __init__(self):

    def seestacks(self):
        print(self.pilha1,self.pilha2,self.pilha3)
    
    def gerafilhos(self):
        f1 = Estado()
        f2 = Estado()
        f3 = Estado()
        f4 = Estado()
        f5 = Estado()
        f6 = Estado()

        f1 = copy.copy(self)
        f2 = copy.copy(self)
        f3 = copy.copy(self)
        f4 = copy.copy(self)
        f5 = copy.copy(self)
        f6 = copy.copy(self)

        f1.seestacks()
        f1.p1top2()
        abertos.append(f1)

        f2.seestacks()
        f2.p1top3()

        abertos.append(f2)

        f3.seestacks()
        f3.p2top1()

        abertos.append(f3)

        f4.seestacks()
        f4.p2top3()

        abertos.append(f4) 

        f5.seestacks()
        f5.p3top1()

        abertos.append(f5)

        f6.seestacks()
        f6.p3top2()

        abertos.append(f6)

    #Move um bloco
    def p1top2(self):
        if(self.pilha1):
            aux=self.pilha1.pop()
            print("Bloco", aux, "removido da pilha 1")
            self.pilha2.append(aux)
            print("Bloco", aux, "movido para a pilha 2")
        else:
            print("Movimento impossível")
        print(self.pilha1,self.pilha2,self.pilha3)
    
    def p1top3(self):
        if(self.pilha1):
            aux=self.pilha1.pop()
            print("Bloco", aux, "removido da pilha 1")
            self.pilha3.append(aux)
            print("Bloco", aux, "movido para a pilha 3")
        else:
            print("Movimento impossível")
        print(self.pilha1,self.pilha2,self.pilha3)

    def p2top1(self):
        if(self.pilha2):
            aux=self.pilha2.pop()
            print("Bloco", aux, "removido da pilha 2")
            self.pilha1.append(aux)
            print("Bloco", aux, "movido para a pilha 1")
        else:
            print("Movimento impossível")
        print(self.pilha1,self.pilha2,self.pilha3)

    def p2top3(self):
        if(self.pilha2):
            aux=self.pilha2.pop()
            print("Bloco", aux, "removido da pilha 2")
            self.pilha3.append(aux)
            print("Bloco", aux, "movido para a pilha 3")
        else:
            print("Movimento impossível")
        print(self.pilha1,self.pilha2,self.pilha3)

    def p3top1(self):
        if(self.pilha3):
            aux=self.pilha3.pop()
            print("Bloco", aux, "removido da pilha 3")
            self.pilha1.append(aux)
            print("Bloco", aux, "movido para a pilha 1")
        else:
            print("Movimento impossível")
        print(self.pilha1,self.pilha2,self.pilha3)

    def p3top2(self):
        if(self.pilha3):
            aux=self.pilha3.pop()
            print("Bloco", aux, "removido da pilha 3")
            self.pilha2.append(aux)
            print("Bloco", aux, "movido para a pilha 2")
        else:
            print("Movimento impossível")
        print(self.pilha1,self.pilha2,self.pilha3)


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
eI.seestacks()

abertos = []
fechados = []
abertos.append(eI)
eI.gerafilhos()
print(abertos)

#ef = Estado()
#ef1 = eI.opr()
#ef2
#print(abertos)
