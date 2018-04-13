class Node:

    def __init__(self, val=None, parent=None):
        """
        defines the node structure where
        val: the value of the matrix
        lChild: the left child produced by moving the tile to the left 
        rChild: the right child produced by moving the tile to the right
        uChild: the upward child produced by moving the tile to the up
        dChild: the downward child produced by moving the tile to the down
        parent: the node's father
        """
        self.val    = val
        self.lChild = None
        self.rChild = None
        self.uChild = None
        self.dChild = None
        self.parent = parent

    def getValue(self):
        ''' Return a reference of the value matrix '''
        return self.val
    
    def getPos(self):
        ''' Return a list of the row and column where * is '''
        for row in range(len(self.getValue())):
            for column in range(len(self.getValue()[row])):
                if self.getValue()[row][column] == '*':
                    return [row, column]


    def isAllowedLeft(self):
        ''' Return true if we can move * to the left '''
        if self.getPos()[1] > 0:
            return True
        return False

    def isAllowedRight(self):
        ''' Return true if we can move * to the right '''
        if self.getPos()[1] < 2:
            return True
        return False

    def isAllowedDown(self):
        ''' Return true if we can move * down '''
        if self.getPos()[0] < 2:
            return True
        return False

    def isAllowedUp(self):
        ''' Return true if we can move *  up '''
        if self.getPos()[0] > 0:
            return True
        return False


    def inside(self, listItems):
        ''' Used to check if the node is already in open or close '''
        for item in listItems:
            if self.getValue() == item.getValue():
                return True
        return False

    def printNode(self):
        ''' Print the node's value matrix '''
        print("_  _  _")
        for row in range(len(self.getValue())):
            for column in range(len(self.getValue()[row])):
                print(self.getValue()[row][column], end="  ")
            print()
        print("_  _  _")

    def strNode(self):
        ''' Convert the node's matrix into a a string with multiple lines '''
        string = ''
        for row in range(3):
            for col in range(3):
                string += str(self.val[row][col]) + ' '
            string += '\n'
        return string
        


def main():
    n1 = Node([
               ['*', '2', '3'],
               ['4', '5', '6'],
               ['7', '8', '1']
              ])
    
    n2 = Node([
              ['1', '2', '3'],
              ['*', '5', '6'],
              ['4', '8', '7']
              ])

    print(n1.isAllowedUp())
    print(n1.isAllowedDown())
    print(n1.isAllowedLeft())
    print(n1.isAllowedRight())

    print("----")
    print(n2.isAllowedUp())
    print(n2.isAllowedDown())
    print(n2.isAllowedLeft())
    print(n2.isAllowedRight())
    

    
if __name__ == "__main__":
    main()
