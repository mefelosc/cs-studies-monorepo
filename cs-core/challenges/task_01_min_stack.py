
class MinStack:
    def __init__(self):
      
        self.pilha = []
        self.minimos = []
        pass

    def push(self, val: int) -> None:
        self.pilha.append(val)
        if self.minimos == []:
            self.minimos.append(val)
        else:
            if val < self.minimos[-1]:
                self.minimos.append(val)
            else:
                self.minimos.append(self.minimos[-1])
        pass

    def pop(self) -> None:
      
        self.pilha.pop()
        self.minimos.pop()

        pass

    def top(self) -> int:
      
        return self.pilha[-1]
        pass

    def get_min(self) -> int:
      
        return self.minimos[-1]
        pass

if __name__ == "__main__":
    # Exemplo de uso:
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    print(stack.get_min()) # Deve retornar -3
    stack.pop()
    print(stack.top())     # Deve retornar 0
    print(stack.get_min()) # Deve retornar -2
