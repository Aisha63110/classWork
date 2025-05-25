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
    def deleteFromBeginning(self):
        if self.head is None:
            return "List is Empty"
        self.head = self.head.next

    def deleteFromEnd(self):
        if self.head is None:
            return "List is Empty"
        if self.head.next is None:
            self.head =None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def serch(self, value):
        current = self.head
        position = 0
        while current:
            if current.data == value:
                return f"value '{value}' found at position {position}"
            current = current.next
            position +=1
        return f"Value '{value}' not found in the list"



if __name__ == '__main__':
    llist = linkedlist()

    llist.insertArtTheBeggining("fox")
    llist.insertArtTheBeggining("brown")
    llist.insertArtTheBeggining("quick")
    llist.insertArtTheBeggining("The")

    llist.printLinkedList()

    llist.insertAtTheEnd("node")
    llist.printLinkedList()

    llist.deleteFromBeginning()
    print("List after deletion")
    llist.printLinkedList()

    print(llist.serch('quick'))
    print(llist.serch('lazy'))