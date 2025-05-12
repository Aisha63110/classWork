class Linklist:
    def __init__ (self,value,nextNode = None):
        self.value = value
        self.nextNode = nextNode


node1 = Linklist("1")
node2 = Linklist("2")
node3 = Linklist("3")
node4 = Linklist("4")
node5 = Linklist("5")
node6 = Linklist("6")
node7 = Linklist("7")
node8 = Linklist("8")
node9 = Linklist("9")
node10 = Linklist("10")

node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4
node4.nextNode = node5
node5.nextNode = node6
node6.nextNode = node7
node7.nextNode = node8
node8.nextNode = node9
node9.nextNode = node10

currentNode = node1
while True:
    print(currentNode.value,">>>", end='')

    if currentNode.nextNode is None:
        print("None")
        break
    currentNode = currentNode.nextNode







