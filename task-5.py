import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="#000000"):  # Початковий колір чорний
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Колір вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

# Функція для додавання ребер у граф і визначення позицій
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Додання вузла до графа
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

# Функція для візуалізації дерева
def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використання значення вузла для міток

    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Генерація кольору на основі індексу
def generate_color(index, max_steps):
    shade = int((index / max_steps) * 255)
    return f'#{shade:02X}{(255 - shade):02X}F0'  # Перехід від темного до світлого

# Обхід у глибину (DFS)
def dfs_visualize(root):
    if not root:
        return
    stack = [root]
    visited = []
    
    step = 0
    while stack:
        node = stack.pop()
        if node not in visited:
            node.color = generate_color(step, 20)  # Генеруємо колір
            draw_tree(root)
            visited.append(node)
            step += 1
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

# Обхід у ширину (BFS)
def bfs_visualize(root):
    if not root:
        return
    queue = deque([root])
    visited = []
    
    step = 0
    while queue:
        node = queue.popleft()
        if node not in visited:
            node.color = generate_color(step, 20)  # Генеруємо колір
            draw_tree(root)
            visited.append(node)
            step += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

# Створення дерева для демонстрації
root = Node(10)
root.left = Node(6)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(8)
root.right.left = Node(12)
root.right.right = Node(18)

# Візуалізація обходу у глибину
print("Обхід у глибину:")
dfs_visualize(root)

# Скидання кольору вузлів перед новим обходом
root.color = "#000000"
root.left.color = "#000000"
root.right.color = "#000000"
root.left.left.color = "#000000"
root.left.right.color = "#000000"
root.right.left.color = "#000000"
root.right.right.color = "#000000"

# Візуалізація обходу у ширину
print("Обхід у ширину:")
bfs_visualize(root)
