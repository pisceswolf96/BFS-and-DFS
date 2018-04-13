import node
import copy
import pydot

class BFS:

    def __init__(self, initVal, goal):
        self.stateCounter = 0
        self.initVal      = node.Node(initVal)
        self.goal         = node.Node(goal)

        self.found          = False
        self.openStates     = [self.initVal]
        self.closedStates   = []

        self.graph = pydot.Dot(graph_type='graph')

        while self.openStates != []:
            x = self.openStates[0]
            if x.getValue() == self.goal.getValue():
                self.found = True # print x
                break
            self.generateChildren(x)
            self.closedStates.append(x)
            self.openStates.remove(x)
            self._printStates(x)
            self.stateCounter += 1

        if self.found:
            self._printStates(x)
            self.graph.write_png('BFS.png')


    def generateChildren(self, parent):

        parentNodeGraph = pydot.Node(parent.strNode())

        leftNode = self._generateLeft(parent)
        if leftNode is not None and not (leftNode.inside(self.openStates) or leftNode.inside(self.closedStates)):
            leftNodeGraph = pydot.Node(leftNode.strNode())
            parent.lChild = leftNode
            self.openStates.append(leftNode)
            edge = pydot.Edge(parentNodeGraph, leftNodeGraph, label='left')
            self.graph.add_edge(edge)
            
      
        
        rightNode = self._generateRight(parent)        
        if rightNode is not None and not (rightNode.inside(self.openStates) or rightNode.inside(self.closedStates)):
            rightNodeGraph = pydot.Node(rightNode.strNode())
            parent.rChild = rightNode
            self.openStates.append(rightNode)
            edge = pydot.Edge(parentNodeGraph, rightNodeGraph, label='right')
            self.graph.add_edge(edge)


        
        upNode = self._generateUp(parent)        
        if upNode is not None and not (upNode.inside(self.openStates) or upNode.inside(self.closedStates)):
            upNodeGraph = pydot.Node(upNode.strNode())
            parent.uChild = upNode
            self.openStates.append(upNode)
            edge = pydot.Edge(parentNodeGraph, upNodeGraph, label='up')
            self.graph.add_edge(edge)


            
        downNode = self._generateDown(parent)
        if downNode is not None and not (downNode.inside(self.openStates) or downNode.inside(self.closedStates)):
            downNodeGraph = pydot.Node(downNode.strNode())
            parent.dChild = downNode
            self.openStates.append(downNode)
            edge = pydot.Edge(parentNodeGraph, downNodeGraph, label='down')
            self.graph.add_edge(edge)


    def _generateLeft(self, parentNode):
        if parentNode.isAllowedLeft():
            valueList   = copy.deepcopy(parentNode.getValue())
            currentPos  = parentNode.getPos()
            futurePos   = [currentPos[0], currentPos[1] - 1]
            currentChar = valueList[currentPos[0]][currentPos[1]]
            futureChar  = valueList[futurePos[0]][futurePos[1]]
            valueList[currentPos[0]][currentPos[1]] = futureChar
            valueList[futurePos[0]][futurePos[1]]   = currentChar

            leftNode = node.Node(valueList, parentNode)
            return leftNode

    def _generateRight(self, parentNode):
        if parentNode.isAllowedRight():
            valueList   = copy.deepcopy(parentNode.getValue())
            currentPos = parentNode.getPos()
            futurePos  = [currentPos[0], currentPos[1] + 1]
            currentChar = valueList[currentPos[0]][currentPos[1]]
            futureChar  = valueList[futurePos[0]][futurePos[1]]

            valueList[currentPos[0]][currentPos[1]] = futureChar
            valueList[futurePos[0]][futurePos[1]]   = currentChar

            rightNode = node.Node(valueList, parentNode)
            return rightNode

    def _generateUp(self, parentNode):
        if parentNode.isAllowedUp():
            valueList   = copy.deepcopy(parentNode.getValue())
            currentPos = parentNode.getPos()
            futurePos  = [currentPos[0] - 1, currentPos[1]]
            currentChar = valueList[currentPos[0]][currentPos[1]]
            futureChar  = valueList[futurePos[0]][futurePos[1]]

            valueList[currentPos[0]][currentPos[1]] = futureChar
            valueList[futurePos[0]][futurePos[1]]   = currentChar

            upNode = node.Node(valueList, parentNode)
            return upNode

    def _generateDown(self, parentNode):
        if parentNode.isAllowedDown():
            valueList   = copy.deepcopy(parentNode.getValue())
            currentPos = parentNode.getPos()
            futurePos  = [currentPos[0] + 1, currentPos[1]]
            currentChar = valueList[currentPos[0]][currentPos[1]]
            futureChar  = valueList[futurePos[0]][futurePos[1]]

            valueList[currentPos[0]][currentPos[1]] = futureChar
            valueList[futurePos[0]][futurePos[1]]   = currentChar

            downNode = node.Node(valueList, parentNode)
            return downNode

    def _printStates(self, nodeToPrint):
        print("State #{}".format(self.stateCounter))
        nodeToPrint.printNode()
        # print("Open States = {}".format(self.openStates))
        # print("Closed States = {}".format(self.closedStates))
        print("Found = {}".format(self.found))
        print("----------")


def main():
    bfsTree = BFS([ ['1', '4', '3'],
		            ['7', '*', '6'],
		            ['5', '8', '2'] ],

                  
                  [ ['1  ', '4', '3'],
                    ['7',
                     '8', '6'],
                    ['*', '5', '2'],])

if __name__ == "__main__":
    main()
