class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        next_temp = curr.next  # Guardar próximo nó
        curr.next = prev       # Inverter o ponteiro
        prev = curr            # Mover prev para curr
        curr = next_temp       # Mover curr para o próximo nó
    return prev

# Teste
head = ListNode(1, ListNode(2, ListNode(3)))
new_head = reverse_list(head)
# Esperado: 3 -> 2 -> 1
print(f"New Head: {new_head.val if new_head else 'None'}")

# Imprimir a lista completa para verificar a ordem
current = new_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")