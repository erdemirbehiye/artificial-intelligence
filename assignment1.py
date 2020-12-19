#Assignmen 1
#CENG 461
#Behiye Erdemir
#240206013

def getList(dict): 
    list = [] 
    for key in dict.keys(): 
        list.append(key) 
          
    return list

def numeric_plus(board,newlist):
    attr=getList(attr_d)
    index1=attr.index(newlist[0])
    index2=attr.index(newlist[2])

    value=""
    value2=""

    for i in range(len(board)):
        if (board[i][index1]) == (newlist[1]) :
            value=int(board[i][0])
            
        if (board[i][index2]) == (newlist[3]) :
            value2=int(board[i][0])
        
        if (value != "")and(value2 != ""):
            if ((int(value)-int(value2))!=int(newlist[4])):
                
                return False
    return True

def numeric_minus(board,newlist):
    attr=getList(attr_d)
    index1=attr.index(newlist[0])
    index2=attr.index(newlist[2])

    value=""
    value2=""

    for i in range(len(board)):
        if (board[i][index1]) == (newlist[1]) :
            value=int(board[i][0])

        if (board[i][index2]) == (newlist[3]) :
            value2=int(board[i][0])

        if (value != "")and(value2 != ""):
            if ((int(value)-int(value2))!=int(newlist[4])):
                return False
    return True

def then_not(board,newlist):
    attr=getList(attr_d)
    index1=attr.index(newlist[0])
    index2=attr.index(newlist[2])
    for i in range(len(board)):
        if (board[i][index1]) == (newlist[1]) :
            if (board[i][index2]) == newlist[3]:
                return False    
    return True

def then_either(board,newlist):
    attr=getList(attr_d)
    index1=attr.index(newlist[0])
    index2=attr.index(newlist[2])
    index3=attr.index(newlist[4])

    for i in range(len(board)):
        if (board[i][index1]) == (newlist[1]) :
            first=((board[i][index3]) != newlist[5])and((board[i][index2]) == newlist[3])
            second=((board[i][index3]) == newlist[5])and((board[i][index2]) != newlist[3])
            if (first or second)==False:
                return False
    return True

def then(board,newlist):
    value=""
    attr=getList(attr_d)
    index1=attr.index(newlist[0])
    index2=attr.index(newlist[2])
    for i in range(len(board)):
        if((board[i][index1]) == (newlist[1])):
            value=board[i][index2]
            if (value!=""):
                if (board[i][index2] != newlist[3]):
                    return False
    return True

def greater(board,newlist):
    attr=getList(attr_d)
    index1=attr.index(newlist[0])
    index2=attr.index(newlist[2])

    value=""
    value2=""

    for i in range(len(board)):
        if (board[i][index1]) == (newlist[1]) :
            value=int(board[i][0])

        if (board[i][index2]) == (newlist[3]) :
            value2=int(board[i][0])
    if (value != "")and(value2 != ""):
        if (int(value)<int(value2)):
            return False
    return True

def less(board,newlist):
    attr=getList(attr_d)
    index1=attr.index(newlist[0])
    index2=attr.index(newlist[2])

    value=""
    value2=""

    for i in range(len(board)):
        if (board[i][index1]) == (newlist[1]) :
            value=int(board[i][0])

        if (board[i][index2]) == (newlist[3]) :
            value2=int(board[i][0])
    if (value != "")and(value2 != ""):
        if (int(value)>int(value2)):
            return False
    return True
    
def corresponds(board,newlist):
    attr=getList(attr_d)
    index1=attr.index(newlist[0])
    index2=attr.index(newlist[2])
    index3=attr.index(newlist[4])
    index4=attr.index(newlist[6])
    
    for i in range(len(board)):

        if (board[i][index1])==newlist[1]:
            if(board[i][index3])!= "":
                notp=(board[i][index3] != newlist[5])
                notq=(board[i][index4] != newlist[7])
                if (not notp or notq) and  (notp or not notq):
                    return False
            
        else:
            if (board[i][index2])==newlist[3]:
                if(board[i][index4])!= "":
                    notp=(board[i][index3] != newlist[5])
                    notq=(board[i][index4] != newlist[7])
                    if (not notp or notq) and  (notp or not notq):
                        return False
        
    return True

def equal(board,newlist):
    attr=getList(attr_d)
    index1=attr.index(newlist[0])
    index2=attr.index(newlist[2])

    for i in range(len(board)):
        if (board[i][index1]) == (newlist[1]) :
            if (board[i][index2]) != (newlist[3]) :
                return False
    return True

def all_different(board,newlist):
    attr=getList(attr_d)
    index1=attr.index(newlist[0])
    index2=attr.index(newlist[2])
    index3=attr.index(newlist[4])
    value=""
    value2=""
    value3=""

    for i in range(len(board)):
        if (board[i][index1]) == (newlist[1]) :
            value=int(board[i][0])

        if (board[i][index2]) == (newlist[3]) :
            value2=int(board[i][0])

        if (board[i][index3]) == (newlist[5]) :
            value3=int(board[i][0])

    if (value != "")and(value2 != ""):
        if ((value==value2) or (value == value3) or (value2==value3)):
            return False
    return True
    
def last_check(board,clue):
    result=[]
    attr=getList(attr_d)
    for i in range(len(clue)):
        sline=clue[i]
        if (" = " in sline) and (" - " in sline):
            text = sline.replace("=","*").replace(") ","*").replace(attr[0]+"(","*").replace(" ","").replace("\n","*")
            list = text.split("*")
            newlist = [x for x in list if x ]
            result.append(numeric_minus(board,newlist))

        elif (" = " in sline) and (" + " in sline):
            text = sline.replace("=","*").replace(") ","*").replace(attr[0]+"(","*").replace(" ","").replace("\n","*")
            list = text.split("*")
            newlist = [x for x in list if x ]
            result.append(numeric_plus(board,newlist))
        

        elif ("then not" in sline):
            text = sline.replace("if ","*").replace("=","*").replace(" then not ","*").replace("\n","*")
            list = text.split("*")
            newlist = [x for x in list if x ]
            result.append(then_not(board,newlist))
        

        elif ("then either" in sline):
            text = sline.replace("if ","*").replace("=","*").replace(" then either ","*").replace(" or ","*").replace("\n","*")
            list = text.split("*")
            newlist = [x for x in list if x ]
            result.append(then_either(board,newlist))

        elif (" > " in sline):
            text = sline.replace("=","*").replace(")","*").replace(attr[0]+"(","*").replace(">","").replace(" ","").replace("\n","*")
            list = text.split("*")
            newlist = [x for x in list if x ]
            result.append(greater(board,newlist))

        elif (" < " in sline):
            text = sline.replace("=","*").replace(")","*").replace(attr[0]+"(","*").replace(">","").replace(" ","").replace("\n","*")
            list = text.split("*")
            newlist = [x for x in list if x ]
            result.append(greater(board,newlist))

        elif("correspond" in sline):
            text = sline.replace("=","*").replace("one of {","*").replace(",","*").replace("} corresponds to ","*").replace(" other ","*").replace(" ","").replace("\n","*")
            list = text.split("*")
            newlist = [x for x in list if x ]
            result.append(corresponds(board,newlist))

        
        elif (" then " in sline):
            text = sline.replace("if ","*").replace("=","*").replace(" then ","*").replace("\n","*")
            list = text.split("*")
            newlist = [x for x in list if x ]
            result.append(then(board,newlist))

        elif (" different" in sline):
            text = sline.replace("{","*").replace("=","*").replace(",","*").replace("} are all different","*").replace("\n","*")
            list = text.split("*")
            newlist = [x for x in list if x ]
            result.append(all_different(board,newlist))

        if False in result:
            return False

        
    return True

def valid(board, value, pos,clue):

    result=[]
    for i in range(len(board)):
        if board[i][pos[1]] == value and pos[0] != i:
            return False
    attr=getList(attr_d)
    for i in range(len(clue)):
        sline=clue[i]
        if (" = " in sline) and (" - " in sline):
            text = sline.replace("=","*").replace(") ","*").replace(attr[0]+"(","*").replace(" ","").replace("\n","*")
            list = text.split("*")
            newlist = [x for x in list if x ]
            result.append(numeric_minus(board,newlist))

        elif (" = " in sline) and (" + " in sline):
            text = sline.replace("=","*").replace(") ","*").replace(attr[0]+"(","*").replace(" ","").replace("\n","*")
            list = text.split("*")
            newlist = [x for x in list if x ]
            result.append(numeric_plus(board,newlist))
        

        elif ("then not" in sline):
            text = sline.replace("if ","*").replace("=","*").replace(" then not ","*").replace("\n","*")
            list = text.split("*")
            newlist = [x for x in list if x ]
            result.append(then_not(board,newlist))
        

        elif ("then either" in sline):
            text = sline.replace("if ","*").replace("=","*").replace(" then either ","*").replace(" or ","*").replace("\n","*")
            list = text.split("*")
            newlist = [x for x in list if x ]
            result.append(then_either(board,newlist))

        elif (" > " in sline):
            text = sline.replace("=","*").replace(")","*").replace(attr[0]+"(","*").replace(">","").replace(" ","").replace("\n","*")
            list = text.split("*")
            newlist = [x for x in list if x ]
            result.append(greater(board,newlist))

        elif (" < " in sline):
            text = sline.replace("=","*").replace(")","*").replace(attr[0]+"(","*").replace(">","").replace(" ","").replace("\n","*")
            list = text.split("*")
            newlist = [x for x in list if x ]
            result.append(greater(board,newlist))

        elif("correspond" in sline):
            text = sline.replace("=","*").replace("one of {","*").replace(",","*").replace("} corresponds to ","*").replace(" other ","*").replace(" ","").replace("\n","*")
            list = text.split("*")
            newlist = [x for x in list if x ]
            result.append(corresponds(board,newlist))

        
        elif (" then " in sline):
            text = sline.replace("if ","*").replace("=","*").replace(" then ","*").replace("\n","*")
            list = text.split("*")
            newlist = [x for x in list if x ]
            result.append(then(board,newlist))

        elif (" different " in sline):
            text = sline.replace("{","*").replace("=","*").replace(",","*").replace("} are all different","*").replace("\n","*")
            list = text.split("*")
            newlist = [x for x in list if x ]
            result.append(all_different(board,newlist))

        if False in result:
            return False

        
    return True

def solve(board,clue):
    pos = empty(board)
    if not pos:
        if last_check(board,clue)==False:
            return False
        return True
    else:
        row, col = pos
    for i in range(len(board)):
        if valid(board, attributes[col][i], (row, col),clue):
            board[row][col] = attributes[col][i]
            if solve(board,clue):
                return True
            board[row][col] = ""
    return False

def print_board(atr_dict, board):
    for key in atr_dict.keys():
        print(key ,"\t|\t", end="")
    print()
    print("---------------------------------------------")
    for row in board:
        for cell in row:
            print((cell if cell!="" else "    ") ,"\t|\t", end="")
        print()

def empty(board):
    for i in range(len(board)):
        for j in range(1,len(board[0])):
            if board[i][j] == "":
                return (i, j) 
    return None 


print("The problems are available in this directoryL 1 2 3")
choose=int(input())
print("Here is the solution to the problem defined in data-{}.txt and clues-{}.txt".format(choose,choose))

attributes=[]
attr_d= {}

#load data
infile = open("./data-"+str(choose)+".txt", 'r') 
lines = infile.readlines() 

#save data as list and dict
for line in lines:
    sline = line.strip()
    split=sline.split(',')
    
    if not len(split):
        continue
    attr_d[split[0]]=split[1:]
    attributes.append(split[1:])
    
infile.close()

#load clues
with open ("clues-"+str(choose)+".txt", 'r') as f:
    clue = f.readlines()

#create board
board=[]
for val in attributes[0]:
    temp=[val]
    temp.extend(3*[""])
    board.append(temp)


solve(board,clue)
print_board(attr_d, board)