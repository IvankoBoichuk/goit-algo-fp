import uuid

import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

    
def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева
draw_tree(root)

def heapify(arr, n, i):
    largest = i  # Ініціалізуємо найбільший елемент як корінь
    left = 2 * i + 1  # Лівий дочірній елемент
    right = 2 * i + 2  # Правий дочірній елемент

    # Перевіряємо, чи лівий дочірній елемент існує і більший за корінь
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Перевіряємо, чи правий дочірній елемент існує і більший за найбільший елемент
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Заміна і продовження heapify, якщо найбільший елемент не корінь
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Створення дерева на основі масиву
def create_tree_from_heap(arr):
    if not arr:
        return None
    
    nodes = [Node(key) for key in arr]
    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]
    return nodes[0]

# Масив для побудови купи
arr = [10, 7, 8, 5, 3, 6, 2]
n = len(arr)

# Створюємо купу
for i in range(n // 2 - 1, -1, -1):
    heapify(arr, n, i)

# Створюємо дерево та відображаємо його
root = create_tree_from_heap(arr)
draw_tree(root)
