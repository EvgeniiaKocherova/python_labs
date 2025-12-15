class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1
    
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self._size += 1
    
    def insert(self, idx, value):
        if idx < 0 or idx > self._size:
            raise IndexError("Индекс вне диапазона")
        
        if idx == 0:
            self.prepend(value)
        elif idx == self._size:
            self.append(value)
        else:
            new_node = Node(value)
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self._size += 1
    
    def remove(self, value):
        if not self.head:
            return
        
        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1
            return
        
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        
        if current.next:
            current.next = current.next.next
            self._size -= 1
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next
    
    def __len__(self):
        return self._size


if __name__ == "__main__":
    lst = SinglyLinkedList()
    
    lst.append(1)
    lst.append(2)
    lst.append(3)
    print(f"Добавили элементы в пустой список: {list(lst)}")
    
    lst.prepend(0)
    print(f"Добавили ноль в начало списка: {list(lst)}")

    lst.insert(2, 1.5)
    print(f"Вставили новый элемент на позицию 2: {list(lst)}")
    
    lst.remove(2)
    print(f"Убрали 2: {list(lst)}")
    
    print("Длина:", len(lst))
