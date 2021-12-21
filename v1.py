html_Absolute_Path= "C:/Users/Youth/Documents/UMich/Courses/21FA/507/Week12_examples/Week12/finalproj/Electrical Engineering and Computer Science Courses – Bulletin.html"
png_Absolute_Path = "C:/Users/Youth/Documents/UMich/Courses/21FA/507/Week12_examples/Week12/finalproj/static/foo.png"
data_Absolute_Path = "C:/Users/Youth/Documents/UMich/Courses/21FA/507/Week12_examples/Week12/finalproj/data.json"

from bs4 import BeautifulSoup
f = open(html_Absolute_Path, encoding ='ISO-8859-1')
html_text = f.read()
soup = BeautifulSoup(html_text, 'html.parser')
all_p_items = soup.find_all('p')

import json
with open(data_Absolute_Path) as fp:
    Results_Dictionary = json.load(fp)
    res_list = Results_Dictionary["getSOCCtlgNbrsResponse"]["ClassOffered"]
    num = len(res_list)
    Course_Number = [res_list[i]["CatalogNumber"] for i in range(num)]
    Course_Name = [res_list[i]["CourseDescr"] for i in range(num)]

class_list = []
for item in all_p_items[1:225]:
    class_list.append(item.find_all('strong')[0].contents[0])

Class_Num_list = []
for str0 in class_list[0:211]:
    if(str0.find('EECS')>=0):
        start = str0.find('EECS')+5
        end = str0.find('EECS')+8
        Class_Num_list.append(int(str0[start:end]))

descr_list = []
for item in all_p_items[1:212]:
    descr_list.append(str(item))

Class_Desrc_list = []
for str0 in descr_list[0:211]:
    start = str0.rfind('br')+4
    end = str0.find('<a href')
    Class_Desrc_list.append(str0[start:end])

Course_FullName = []
for str0 in descr_list[0:211]:
    start = str0.find('EECS')+9
    end = str0.find('</strong>')
    Course_FullName.append(str0[start:end])

Prereqs = []
for item in all_p_items[1:225]:
    descr_list = item.find_all('em')[0].contents
    res = [i for i in descr_list if 'Prereq' in i]
    if len(res) != 0:
        Prereqs.append(res[0])
    else:
        Prereqs.append('None')

Prereq_Num_list = [] 
for str0 in Prereqs[0:211]:
    if(str0.find('EECS')>0):
        start = str0.find('EECS')+5
        end = str0.find('EECS')+8
        Prereq_Num_list.append(str0[start:end])
    else:
        str0 = 'None'
        Prereq_Num_list.append(str0)
a=0
for i in Prereq_Num_list:
    if i == ' (1':
        Prereq_Num_list[a]='None'
    a = a+1
for i in range(len(Prereq_Num_list)):
    if Prereq_Num_list[i] != 'None':
        Prereq_Num_list[i] = int(Prereq_Num_list[i])

def find_nth(string, sub, n):
    start = string.find(sub)
    while start >= 0 and n > 1:
        start = string.find(sub, start+len(sub))
        n -= 1
    return start
Prereq_Num_list2 = [] 
for str0 in Prereqs[0:211]:
    eecs2 = find_nth(str0, "EECS", 2)
    if(eecs2>0):
        start = eecs2+5
        end = eecs2+8
        Prereq_Num_list2.append(str0[start:end])
    else:
        str0 = 'None'
        Prereq_Num_list2.append(str0)
for i in range(len(Prereq_Num_list2)):
    if Prereq_Num_list2[i] != 'None':
        Prereq_Num_list2[i] = int(Prereq_Num_list2[i])

class Course():
    def __init__(self,key):
        self.number = key
        self.name = None
        self.descr = None

    def setName(self,name):
        self.name = name
    
    def setDescr(self,descr):
        self.descr = descr

    def show(self):
        print(self.number, self.name, self.descr)

C_list = []
for i in range(len(Class_Num_list)):
    # print({i},":", Class_Num_list[i])
    C_list.append(Course(Class_Num_list[i]))
    C_list[i].setName(Course_FullName[i])
    C_list[i].setDescr(Class_Desrc_list[i])
    # C.show()

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

    # def getWeight(self,nbr):
    #     return self.connectedTo[nbr]

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

import networkx as nx
import matplotlib.pyplot as plt

DG = nx.DiGraph()
visual1=[]
for i in  range(len(Class_Num_list)):
   if Prereq_Num_list[i] != 'None' and Prereq_Num_list[i] != Class_Num_list[i] :
        g.addEdge(Prereq_Num_list[i],Class_Num_list[i])
        visual1.append([Prereq_Num_list[i],Class_Num_list[i]])

DG.add_edges_from(visual1)
visual2=[]
for i in  range(len(Class_Num_list)):
   if Prereq_Num_list2[i] != 'None' and Prereq_Num_list2[i] != Class_Num_list[i] :
        g.addEdge(Prereq_Num_list2[i],Class_Num_list[i])
        visual2.append([Prereq_Num_list2[i],Class_Num_list[i]])
DG.add_edges_from(visual2)


nx.draw_networkx(DG,pos=nx.spring_layout(DG), node_size=60, arrowsize=5, font_size=6)
plt.savefig(png_Absolute_Path)

from collections import deque 
def getPrepath(course_number):
    Prestring = " "
    Prepath = deque()
    if g.getVertex(course_number) != None:
        Prepath.append(g.getVertex(course_number))
        while Prepath:
            currentVert = Prepath.popleft()
            # print(currentVert)
            x = list(currentVert.getPredecessor())
            for i in x:
                if not i.discovered:
                    i.setdiscovered()
                    Prepath.append(i)
            Prestring = "".join([Prestring, currentVert.__str__()])
            Prestring = Prestring + "      "
        return Prestring

def Courseoffered(course_number):
    if g.getVertex(course_number) != None:
        offered = "is offered"
    else:
        offered = "isn't offered"
    return offered

def Coursename(course_number):
    for i in range(len(Class_Num_list)):
        if C_list[i].number == course_number:
            return C_list[i].name

def Coursedescription(course_number):
    for i in range(len(Class_Num_list)):
        if C_list[i].number == course_number:
            return C_list[i].descr

def Courseprerequisite(course_number):
    # pre_list = []
    string = " "
    if g.getVertex(course_number) != None:
        for i in list(g.getVertex(course_number).predecessor):
            # pre_list.append(i.id)
            string = string + " " + str(i.id)
    return string

def Coursesuccessor(course_number):
    # pre_list = []
    string = " "
    if g.getVertex(course_number) != None:
        for i in list(g.getVertex(course_number).successor):
            # pre_list.append(i.id)
            string = string + " " + str(i.id)
    return string

    # for i in range(len(Class_Num_list)):
    #     if C_list[i].number == course_number:
    #         return C_list[i].prereq


# if __name__ == "__main__":
    # print(type(Visualization()))