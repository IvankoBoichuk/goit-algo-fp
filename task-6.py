# Дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Жадібний алгоритм
def greedy_algorithm(items, budget):
    # Сортуємо страви за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    
    total_cost = 0
    total_calories = 0
    chosen_items = []
    
    for item, properties in sorted_items:
        if total_cost + properties["cost"] <= budget:
            chosen_items.append(item)
            total_cost += properties["cost"]
            total_calories += properties["calories"]
    
    return chosen_items, total_cost, total_calories

# Алгоритм динамічного програмування
def dynamic_programming(items, budget):
    item_list = list(items.items())
    n = len(item_list)
    
    # Створюємо таблицю для збереження результатів
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    # Заповнюємо таблицю
    for i in range(1, n + 1):
        item_name, properties = item_list[i - 1]
        cost = properties["cost"]
        calories = properties["calories"]
        
        for b in range(1, budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + calories)
            else:
                dp[i][b] = dp[i - 1][b]
    
    # Відстежуємо вибрані предмети
    chosen_items = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            item_name, properties = item_list[i - 1]
            chosen_items.append(item_name)
            b -= properties["cost"]
    
    total_calories = dp[n][budget]
    total_cost = sum(items[item]["cost"] for item in chosen_items)
    
    return chosen_items, total_cost, total_calories

# Тестування функцій
budget = 100

# Жадібний алгоритм
greedy_result = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print(f"Вибрані страви: {greedy_result[0]}")
print(f"Загальна вартість: {greedy_result[1]}")
print(f"Загальна калорійність: {greedy_result[2]}")

# Динамічне програмування
dp_result = dynamic_programming(items, budget)
print("\nДинамічне програмування:")
print(f"Вибрані страви: {dp_result[0]}")
print(f"Загальна вартість: {dp_result[1]}")
print(f"Загальна калорійність: {dp_result[2]}")
