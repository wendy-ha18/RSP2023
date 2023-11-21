class MyLinkedList:
    def __init__(self):
        self.head = Node(0)  # dummy node
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:  # invalid index
            return -1

        cur = self.head
        for _ in range(index + 1):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:  # invalid index
            return

        prev = self.head
        for _ in range(index):
            prev = prev.next

        # Add newNode between [prev] and [prev.next]
        newNode = Node(val, prev.next)
        prev.next = newNode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:  # invalid index
            return

        prev = self.head
        for _ in range(index):
            prev = prev.next

        prev.next = prev.next.next
        self.size -= 1