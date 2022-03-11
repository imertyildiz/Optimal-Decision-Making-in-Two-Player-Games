# Node class (state)
class Node:
    def __init__(self, name, parent, parentWayName):
        self.parent = parent
        self.parentWayName = parentWayName
        self.children = []
        self.name = name
        self.path = []
        self.depth = 0
        self.cost = 0
        self.type = ""
        self.isLeaf = False


# Node Finder in given list
def findNode(nodeList, nodeName):
    for i in nodeList:
        if i.name == nodeName:
            return i
    return None


# min function of gameTree for Minimax
def gameTreeMin(node, trace):
    minvalue = 999999999999
    path = ""
    if node.isLeaf:
        return node.cost, node.parentWayName
    for i in node.children:
        trace.append(i.name)
        x = gameTreeMax(i, trace)
        if minvalue > x[0]:
            minvalue = x[0]
            path = i.parentWayName
    return (minvalue, path)


# max function of gameTree for Minimax
def gameTreeMax(node, trace):
    maxvalue = -999999999999
    path = ""
    if node.isLeaf:
        return node.cost, node.parentWayName
    for i in node.children:
        trace.append(i.name)
        x = gameTreeMin(i, trace)
        if maxvalue < x[0]:
            maxvalue = x[0]
            path = i.parentWayName
    return (maxvalue, path)


# whole function of gameTree for Minimax
def gameTreeMinimax(allNodes):
    root = allNodes[0]
    trace = []
    if root.type == "MAX":
        ret = gameTreeMax(root, trace)
        return ret[0], ret[1], trace
    else:
        ret = gameTreeMin(root, trace)
        return ret[0], ret[1], trace


# min function of gameTree for AlphaBeta
def gameTreeMinAlphaBeta(node, trace, alpha, beta):
    minvalue = 99999999999
    path = ""
    if node.isLeaf:
        return node.cost, node.parentWayName
    for i in node.children:
        trace.append(i.name)
        x = gameTreeMaxAlphaBeta(i, trace, alpha, beta)
        if minvalue > x[0]:
            minvalue = x[0]
            path = i.parentWayName
        if minvalue <= alpha:
            return minvalue, path
        beta = min(beta, minvalue)
    return minvalue, path


# max function of gameTree for AlphaBeta
def gameTreeMaxAlphaBeta(node, trace, alpha, beta):
    maxvalue = -99999999999
    path = ""
    if node.isLeaf:
        return node.cost, node.parentWayName
    for i in node.children:
        trace.append(i.name)
        x = gameTreeMinAlphaBeta(i, trace, alpha, beta)
        if maxvalue < x[0]:
            maxvalue = x[0]
            path = i.parentWayName
        if maxvalue >= beta:
            return maxvalue, path
        alpha = max(alpha, maxvalue)
    return maxvalue, path


# whole function of gameTree for AlphaBeta
def gameTreeAlphaBeta(allNodes):
    root = allNodes[0]
    trace = []
    if root.type == "MAX":
        ret = gameTreeMaxAlphaBeta(root, trace, -99999999999, 99999999999)
        return ret[0], ret[1], trace
    else:
        ret = gameTreeMinAlphaBeta(root, trace, -99999999999, 99999999999)
        return ret[0], ret[1], trace


# construction function of children states for "X"
def constructStatesX(state):
    for i in [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]:
        if state.name[i[0] + i[1] * 3] == " ":
            child = Node(state.name[:i[0] + i[1] * 3] + "X" + state.name[i[0] + i[1] * 3 + 1:], state, i)
            child.depth = state.depth + 1
            state.children.append(child)
            if isTerminal(child):
                child.isLeaf = True
                child.cost = calculateUtility(child)
            else:
                constructStatesO(child)


# construction function of children states for "O"
def constructStatesO(state):
    for i in [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]:
        if state.name[i[0] + i[1] * 3] == " ":
            child = Node(state.name[:i[0] + i[1] * 3] + "O" + state.name[i[0] + i[1] * 3 + 1:], state, i)
            child.depth = state.depth + 1
            state.children.append(child)
            if isTerminal(child):
                child.isLeaf = True
                child.cost = calculateUtility(child)
            else:
                constructStatesX(child)


# function of whether given node is terminal or not
def isTerminal(node):
    if " " not in node.name:
        return True
    elif node.name[0] == "O" and node.name[1] == "O" and node.name[2] == "O":
        return True
    elif node.name[3] == "O" and node.name[4] == "O" and node.name[5] == "O":
        return True
    elif node.name[6] == "O" and node.name[7] == "O" and node.name[8] == "O":
        return True
    elif node.name[0] == "O" and node.name[3] == "O" and node.name[6] == "O":
        return True
    elif node.name[1] == "O" and node.name[4] == "O" and node.name[7] == "O":
        return True
    elif node.name[2] == "O" and node.name[5] == "O" and node.name[8] == "O":
        return True
    elif node.name[0] == "O" and node.name[4] == "O" and node.name[8] == "O":
        return True
    elif node.name[2] == "O" and node.name[4] == "O" and node.name[6] == "O":
        return True
    elif node.name[0] == "X" and node.name[1] == "X" and node.name[2] == "X":
        return True
    elif node.name[3] == "X" and node.name[4] == "X" and node.name[5] == "X":
        return True
    elif node.name[6] == "X" and node.name[7] == "X" and node.name[8] == "X":
        return True
    elif node.name[0] == "X" and node.name[3] == "X" and node.name[6] == "X":
        return True
    elif node.name[1] == "X" and node.name[4] == "X" and node.name[7] == "X":
        return True
    elif node.name[2] == "X" and node.name[5] == "X" and node.name[8] == "X":
        return True
    elif node.name[0] == "X" and node.name[4] == "X" and node.name[8] == "X":
        return True
    elif node.name[2] == "X" and node.name[4] == "X" and node.name[6] == "X":
        return True
    return False


# Function of calculation utility
def calculateUtility(node):
    if node.name[0] == "O" and node.name[1] == "O" and node.name[2] == "O":
        return -5
    elif node.name[3] == "O" and node.name[4] == "O" and node.name[5] == "O":
        return -5
    elif node.name[6] == "O" and node.name[7] == "O" and node.name[8] == "O":
        return -5
    elif node.name[0] == "O" and node.name[3] == "O" and node.name[6] == "O":
        return -5
    elif node.name[1] == "O" and node.name[4] == "O" and node.name[7] == "O":
        return -5
    elif node.name[2] == "O" and node.name[5] == "O" and node.name[8] == "O":
        return -5
    elif node.name[0] == "O" and node.name[4] == "O" and node.name[8] == "O":
        return -5
    elif node.name[2] == "O" and node.name[4] == "O" and node.name[6] == "O":
        return -5
    elif node.name[0] == "X" and node.name[1] == "X" and node.name[2] == "X":
        return 5 - 0.01 * (node.depth - 1)
    elif node.name[3] == "X" and node.name[4] == "X" and node.name[5] == "X":
        return 5 - 0.01 * (node.depth - 1)
    elif node.name[6] == "X" and node.name[7] == "X" and node.name[8] == "X":
        return 5 - 0.01 * (node.depth - 1)
    elif node.name[0] == "X" and node.name[3] == "X" and node.name[6] == "X":
        return 5 - 0.01 * (node.depth - 1)
    elif node.name[1] == "X" and node.name[4] == "X" and node.name[7] == "X":
        return 5 - 0.01 * (node.depth - 1)
    elif node.name[2] == "X" and node.name[5] == "X" and node.name[8] == "X":
        return 5 - 0.01 * (node.depth - 1)
    elif node.name[0] == "X" and node.name[4] == "X" and node.name[8] == "X":
        return 5 - 0.01 * (node.depth - 1)
    elif node.name[2] == "X" and node.name[4] == "X" and node.name[6] == "X":
        return 5 - 0.01 * (node.depth - 1)
    else:
        return 0


# min function of TicTacToe for Minimax
def ticTacToeMin(node, trace):
    minvalue = 999999999999
    path = ""
    if node.isLeaf:
        return node.cost, node.parentWayName
    for i in node.children:
        trace.append(i.name)
        x = ticTacToeMax(i, trace)
        if minvalue > x[0]:
            minvalue = x[0]
            path = i.parentWayName
    return (minvalue, path)


# max function of TicTacToe for Minimax
def ticTacToeMax(node, trace):
    maxvalue = -999999999999
    path = ""
    if node.isLeaf:
        return node.cost, node.parentWayName
    for i in node.children:
        trace.append(i.name)
        x = ticTacToeMin(i, trace)
        if maxvalue < x[0]:
            maxvalue = x[0]
            path = i.parentWayName
    return (maxvalue, path)


# whole function of TicTacToe for Minimax
def ticTacToeMinimax(state):
    stateNode = Node(state, None, "")
    constructStatesX(stateNode)
    trace = []
    ret = ticTacToeMax(stateNode, trace)
    return ret[0], ret[1], trace


# min function of TicTacToe for AlphaBeta
def ticTacToeMinAlphaBeta(node, trace, alpha, beta):
    minvalue = 99999999999
    path = ""
    if node.isLeaf:
        return node.cost, node.parentWayName
    for i in node.children:
        trace.append(i.name)
        x = ticTacToeMaxAlphaBeta(i, trace, alpha, beta)
        if minvalue > x[0]:
            minvalue = x[0]
            path = i.parentWayName
        if minvalue <= alpha:
            return minvalue, path
        beta = min(beta, minvalue)
    return minvalue, path


# max function of TicTacToe for AlphaBeta
def ticTacToeMaxAlphaBeta(node, trace, alpha, beta):
    maxvalue = -99999999999
    path = ""
    if node.isLeaf:
        return node.cost, node.parentWayName
    for i in node.children:
        trace.append(i.name)
        x = ticTacToeMinAlphaBeta(i, trace, alpha, beta)
        if maxvalue < x[0]:
            maxvalue = x[0]
            path = i.parentWayName
        if maxvalue >= beta:
            return maxvalue, path
        alpha = max(alpha, maxvalue)
    return maxvalue, path


# whole function of TicTacToe for AlphaBeta
def ticTacToeAlphaBeta(state):
    stateNode = Node(state, None, "")
    constructStatesX(stateNode)
    trace = []
    ret = ticTacToeMaxAlphaBeta(stateNode, trace, -99999999999, 99999999999)
    return ret[0], ret[1], trace


# WHOLE funciton
def SolveGame(method_name, problem_file_name, player_type):
    with open(problem_file_name) as f:
        lines = f.read().splitlines()
    if len(lines[0]) < 3:
        #  Game-Tree
        allNodes = []
        root = Node(lines.pop(0), None, "")
        root.type = player_type
        allNodes.append(root)
        line = lines.pop(0).split(' ')
        while len(line) == 3:
            nodeX = Node(line[1], findNode(allNodes, line[0], ), line[2])
            if nodeX.parent is not None:
                nodeX.depth = nodeX.parent.depth + 1
            if nodeX.parent.type == "MAX":
                nodeX.type = "MIN"
            else:
                nodeX.type = "MAX"
            allNodes.append(nodeX)
            line = lines.pop(0).split(' ')
        line = line[0]
        line = line.split(':')
        while line:
            x = findNode(allNodes, line[0])
            x.cost = int(line[1])
            x.isLeaf = True
            if len(lines) == 0:
                break
            line = lines.pop(0).split(':')
        for i in allNodes:
            if i.parent is not None:
                i.parent.children.append(i)
        if method_name == "Minimax":
            return gameTreeMinimax(allNodes)
        elif method_name == "AlphaBeta":
            return gameTreeAlphaBeta(allNodes)
    else:
        #  Tic-Tac-Toe
        state = ""
        for i in lines:
            state = state + i
        state = state.replace("#", "")
        if method_name == "Minimax":
            return ticTacToeMinimax(state)
        elif method_name == "AlphaBeta":
            return ticTacToeAlphaBeta(state)
print(SolveGame("Minimax","gametree5.txt","MAX"))
