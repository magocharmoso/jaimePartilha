from searchPlus import *
linha1= "  ##### \n"
linha2= "###...# \n"
linha3= "#o@$..# \n"
linha4= "###.$o# \n"
linha5= "#o##..# \n"
linha6= "#.#...##\n"
linha7= "#$.....#\n"
linha8= "#......#\n"
linha9= "########\n"
mundoStandard=linha1+linha2+linha3+linha4+linha5+linha6+linha7+linha8+linha9


class Sokoban(Problem):
    changeLineChar = "\n"
    wallChar = "#"
    boxChar = "$"
    goalChar = "o"
    sokobanChar = "@"
    sokobanOnGoalChar = "+"
    outsideChar = " "
    emptyChar = "."
    occupiedGoalChar = "*"
    
    
    #possivel erro nas funcoes linha e coluna por não saber se self.atribute funciona
    

    def __init__(self, situacaoInicial=mundoStandard):
        self.map = situacaoInicial
        self.rows = howManyRows()
        self.lines = howManyLines()
        self.matriceMap = matriceMap()
        self.walls = setWalls()
        self.goals = setGoals()
        self.boxes = setBoxes()
        self.outside = setOutside()
        self.playerPosition = setPlayerPosition(matriceMap)
        self.occupiedGoals = setOccupiedGoals()

        def howManyRows(self):
            acc = 0
            while True:
                character = self.map[acc]
                
                if character == self.changeLineChar :
                    break
                acc += 1
            return acc
    
        def howManyLines(self):
            acc = 0
            for i in range(len(self.map)):
                if map[i] == self.changeLineChar:
                    acc += 1
            return acc
        #torna a lista mapa numa matriz
        def matriceMap(self): 
            newMap = [[]]
            acc = 0
            for i in range(self.lines):
                newMap.append([])
                for j in range(self.rows):
                    newMap[i].append(self.map[acc])
                    acc+=1
                acc+=1 #salta o \n
            return newMap
        
        def setWalls(self):
            m = [[]]
            for i in range(self.lines):
                m.append([])
                for j in range(self.rows):
                    m[i].append(self.matriceMap[i][j]==self.wallChar)
            return m
        
        def setGoals(self):
            m = [[]]
            for i in range(self.lines):
                m.append([])
                for j in range(self.rows):
                    m[i].append(self.matriceMap[i][j]==self.goalChar or self.matriceMap[i][j]==self.sokobanOnGoalChar)
            return m
                
        def setBoxes(self):
            m = [[]]
            for i in range(self.lines):
                m.append([])
                for j in range(self.rows):
                    m[i].append(self.matriceMap[i][j]==self.boxChar)
            return m             
        
        def setOutside(self):
            m = [[]]
            for i in range(self.lines):
                m.append([])
                for j in range(self.rows):
                    m[i].append(self.matriceMap[i][j]==self.outsideChar)
            return m    
    
        def setPlayerPosition(self):
            for i in range(self.lines):
                for j in range(self.rows):
                    if(self.matriceMap[i][j]==self.sokobanChar or self.matriceMap[i][j]==self.sokobanOnGoalChar ):
                        x = i
                        y = j
            return (x,y)
        
        
        def setOccupiedGoals(self):
            m = [[]]
            for i in range(self.lines):
                m.append([])
                for j in range(self.rows):
                    m[i].append(self.matriceMap[i][j]==self.occupiedGoalChar)
            return m    

    
        
    def isWall(self, x, y):
        return self.walls[x][y]
    
    def isGoal(self, x, y):
        return self.goals[x][y]
    
    def isBox(self,x,y):
        return self.boxes[x][y]
    
    def isOccupiedGoal(self,x,y):
        return self.occupiedGoals[x][y]
    
    def isOutside(self,x,y):
        return self.outsideChar[x][y]
    
    def isEmpty(self,x,y):
        return not(self.isBox(x,y))and not(self.isGoal(x,y)) and not(self.isWall(x,y)) and not(self.isOccupiedGoal(x,y)) and not(self.isOutside(x,y))


    def actions(self, state):
        pass
    
    def result(self, state, action):
        pass
        
    def result(self, state, action):
        pass
        
    def path_cost(c,s1,action,s2):
        pass
        
    def goal_test(self,state):
        boolean = True
        return
        
    def executa(self,state,actions):
        """Partindo de state, executa a sequência (lista) de acções (em actions) e devolve o último estado"""
        nstate=state
        for a in actions:
            nstate=self.result(nstate,a)
        return nstate
    
    def display(self, state):
        displayMatrix = [[]]
        for i in range(self.lines):
            displayMatrix.append([])
            for j in range(self.rows):
                if(self.isWall(i,j)): displayMatrix.append(self.wallChar)
                elif(self.isGoal(i,j)): displayMatrix.append(self.goalChar)
                elif(self.isBox(i,j)): displayMatrix.append(self.boxChar)
                elif(self.isOutside(i,j)): displayMatrix.append(self.outsideChar)
                elif(self.isOccupiedGoal(i,j)): displayMatrix.append(self.occupiedGoalChar)
                elif(self.isEmpty(i,j)): displayMatrix.append(self.emptyChar)
        
        #colocar o jogador
        x = self.playerPosition[0]
        y = self.playerPosition[1]
        if(self.isGoal(x,y)): displayMatrix[x][y] = self.sokobanOnGoalChar
        else: displayMatrix[x][y] = self.sokobanChar
        
        #formatar a string
        display = []
        for i in range(self.lines):   
            for j in range(self.rows):
                display.append[i][j]
        return display
        