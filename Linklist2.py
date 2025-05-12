class node:
    def __init__(self,data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def insertArtTheBeggining(self,new_data):
        new_node = node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data, end = ' ')

            temp = temp.next
        print()

    def insertAtTheEnd(self, new_data):
        new_node = node(new_data)

        if self.head is None:
            self.head = new_node
            return None

        last = self.head

        while last.next:
            last = last.next

        last.next = new_node



if __name__ == '__main__':
    llist = linkedlist()

    llist.insertArtTheBeggining("fox")
    llist.insertArtTheBeggining("brown")
    llist.insertArtTheBeggining("quick")
    llist.insertArtTheBeggining("The")

    llist.printLinkedList()

    llist.insertAtTheEnd("node")
    llist.printLinkedList()