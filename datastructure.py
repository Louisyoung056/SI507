# This standalone file is a part of the v1.py, it can't be run alone,
# it's just a demonstration of part of the code that's used for created the graph data structure used in the application.

class Vertex:
    def __init__(self,key,discovered=0):
        self.id = key
        self.successor = {}
        self.predecessor = {}
        self.discovered = discovered

    def addPredecessor(self,nbr,weight=0):
        self.predecessor[nbr] = weight

    def addSuccessor(self,nbr,weight=0):
        self.successor[nbr] = weight

    def __str__(self):
        string1 = str(self.id) + "'s following courses: " + str([x.id for x in self.successor])
        string2 = str(self.id) + "'s prerequisite courses: " + str([x.id for x in self.predecessor]) + " "
        # return string1 + '\n' + string2
        return string2

    def getSuccessor(self):
        return self.successor.keys()
        # return self.successor.keys()

    def getPredecessor(self):
        return self.predecessor.keys()

    def getId(self):
        return self.id
        
    def setdiscovered(self):
        self.discovered = 1
        return

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addSuccessor(self.vertList[t], weight)
        self.vertList[t].addPredecessor(self.vertList[f], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

g = Graph()

for i in  range(len(Class_Num_list)):
   if Prereq_Num_list[i] != 'None' and Prereq_Num_list[i] != Class_Num_list[i] :
        g.addEdge(Prereq_Num_list[i],Class_Num_list[i])

for i in  range(len(Class_Num_list)):
   if Prereq_Num_list2[i] != 'None' and Prereq_Num_list2[i] != Class_Num_list[i] :
        g.addEdge(Prereq_Num_list2[i],Class_Num_list[i])
 