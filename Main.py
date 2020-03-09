import random

class Bloco:
    blocos = ['A','B','C']
    pilha1 = []
    pilha2 = []
    pilha3 = []

    def init(self):
        while(self.blocos):
            i=random.randint(0,2)
            aux=self.blocos.pop(i)
            i=random.randint(1,3)
            if(i==1):
                self.pilha1.append(aux)
            elif(i==2):
                self.pilha2.append(aux)
            elif(i==3):
                self.pilha3.append(aux)
            print(self.pilha1,self.pilha2,self.pilha3)

bl = Bloco()
bl.init()
