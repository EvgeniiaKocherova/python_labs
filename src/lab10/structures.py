from collections import deque

class Stack:
    """Стек на базе list."""
    
    def __init__(self):
        self._data = [] 
    
    def push(self, item):
        self._data.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пустой")
        return self._data.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self._data[-1]
    
    def is_empty(self):
        return len(self._data) == 0
    
    def __len__(self):
        return len(self._data)


class Queue:
    """Очередь на базе deque."""
    
    def __init__(self):
        self._data = deque()  
    
    def enqueue(self, item):
        self._data.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Очередь пустая")
        return self._data.popleft()
    
    def peek(self):
        if self.is_empty():
            return None
        return self._data[0]
    
    def is_empty(self):
        return len(self._data) == 0
    
    def __len__(self):
        return len(self._data)
    

if __name__ == "__main__":
    print('========>Stack<========')
    
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    
    print(f'Снятие верхнего элемента стека: {stack.pop()}')
    print(f'Проверка, пустой ли стек: {stack.is_empty()}')
    print(f'Число сверху: {stack.peek()}')
    stack.push(5)
    print(f'Значение сверху после добавления числа в стек: {stack.peek()}')
    print(f'Длина стека: {len(stack)}')
    print(f'Стек: {stack._data}')
    
    print('========>Queue<=========')
    
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    
    print(f'Значение первого элемента: {q.peek()}')
    q.dequeue()
    print(f'Значение первого элемента после удаления числа: {q.peek()}')
    q.enqueue(52)
    print(f'Значение первого элемента после добавления числа: {q.peek()}')
    print(f'Проверка, пустая ли очередь: {q.is_empty()}')
    print(f'Количество элементов в очереди: {len(q)}')