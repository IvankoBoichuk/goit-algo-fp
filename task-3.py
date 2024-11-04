import heapq

# Створення графа у вигляді словника суміжностей
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1, 'E': 3},
    'E': {'D': 3}
}

# Функція для реалізації алгоритму Дейкстри
def dijkstra(graph, start):
    # Ініціалізація відстаней до вершин як нескінченних, крім початкової вершини
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # Ініціалізація бінарної купи
    priority_queue = [(0, start)]  # Кортежі у вигляді (відстань, вершина)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Перевіряємо, чи вже знайдений коротший шлях
        if current_distance > distances[current_vertex]:
            continue

        # Перевіряємо всіх сусідів поточної вершини
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Якщо знайдено коротший шлях до сусіда, оновлюємо відстань і додаємо до черги
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Запуск алгоритму Дейкстри
start_vertex = 'A'
shortest_paths = dijkstra(graph, start_vertex)

# Вивід результатів
print(f"Найкоротші шляхи від вершини '{start_vertex}':")
for vertex, distance in shortest_paths.items():
    print(f"Відстань до {vertex}: {distance}")
