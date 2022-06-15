
class Graph():
    
    def __init__(self, vertices):
        self.graph = [[0 for column in range(vertices)]
                        for row in range(vertices)]
        self.V = vertices
        
    #Sprawdzamy, czy ten wierzchołek jest sąsiadującym wierzchołkiem
    #wcześniej dodanego wierzchołka i nie jest on
    #zawarty w ścieżce wcześniej
    def CzySasiad(self, v, pos, path):
        if self.graph[path[pos-1]][v] == 0:
            return False

    #Sprawdzamy czy wierzcholek nie jest w sziezce
        for vertex in path:
            if vertex == v:
                return False        
        return True

    #Rozwiazanie problemu sciezki Hamiltona
    def HamSziezkaRozw(self,path,pos):
        if pos == self.V:
            if self.graph[path[pos-1]][path[0]] == 1:
                return True   
            else:
                return False
        #zaczynamy nie od 0 a od 1 dlatego ze 0 to nasz punkt startowy
        for v in range(1,self.V):
            if self.CzySasiad(v,pos,path) == True:
                path[pos] = v
                if self.HamSziezkaRozw(path,pos+1) == True:
                    return True
        #Usunamy biezacy wierzcholek jesli nie doprowadzi to do rozwiazania
            path[pos] = -1
        
        return False
    
    def HamSciezka(self):
         path = [-1] * self.V
         path[0] = 0
         
    #Oznaczamy wierzholek 0 jako pierwszy na sciezce
    #Jesli istnieje cykl Hamiltona to sciezka moze byc rozpoczeta
    #z dowolnego wierzcholka dlatego ze wykres nieskierowany
         if self.HamSziezkaRozw(path,1) == False:
             print("Solution does not exist\n")
             return False
         self.Wypisz(path)
         return True
     
     
    def Wypisz(self, path):         
        print("Solution Exists: Following",
              "is one Hamiltonian Cycle")
        for vertex in path:
            print(vertex, end = " ")
        print(path[0],"\n")
        
def main():
    #Exmamples:
    g1 = Graph(5)
    g1.graph = [ [0,1,0,1,0],[1,0,1,1,1],
                [0,1,0,0,1],[1,1,0,0,1],
                [0,1,1,1,0],]
    g1.HamSciezka()     

    print("\t-----\n")
    g2= Graph(5)
    g2.graph = [ [0,1,0,1,0],[1,0,1,1,1],
                [0,1,0,0,1],[1,1,0,0,0],[0,1,1,0,0],]
    g2.HamSciezka()

    print("\t-----\n")
    g3 = Graph(4)
    g3.graph = [ [0,1,1,0],[1,0,1,1],[1,1,0,1],
                [0,0,1,1]]
    g3.HamSciezka()
    

if __name__ == "__main__":
    main()
                 
    