# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class Nodo:
    def __init__(self, valor, f, c):
        self.visita = False
        self.f, self.c = f, c
        self.vesinos=[]
        self.valor=valor
        
    def get_cantidadVesinos(self):
        return len(self.vesinos)
    
    def get_vesinoN(self,posicion):
        return self.vesinos[posicion]
    
    def get_coodernadas(self):
        return self.f,self.c
    
    def get_visita(self):
        return self.visita
    
    def set_visita(self,valor):
        self.visita=valor
        
    def set_vesinos(self,nodo):
        f,c=nodo.get_coodernadas()
        if len(self.vesinos)==0:
            self.vesinos.append(nodo)
        else:
            bandera=True
            for no in self.vesinos:
                if no.f==f and no.c==c:
                    bandera=Flase
                    break
            if bandera:
                vesinos.append(nodo)
                    

