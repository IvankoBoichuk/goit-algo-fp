import random
import matplotlib.pyplot as plt

# Функція для симуляції кидків кубиків
def simulate_dice_rolls(num_rolls):
    outcomes = {i: 0 for i in range(2, 13)}  # Суми від 2 до 12

    for _ in range(num_rolls):
        roll1 = random.randint(1, 6)  # Перший кубик
        roll2 = random.randint(1, 6)  # Другий кубик
        sum_rolls = roll1 + roll2
        outcomes[sum_rolls] += 1

    probabilities = {k: v / num_rolls * 100 for k, v in outcomes.items()}
    return probabilities

# Виконуємо симуляцію
num_rolls = 1000000  # Кількість кидків
probabilities = simulate_dice_rolls(num_rolls)

# Аналітичні ймовірності
analytical_probabilities = {
    2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89, 7: 16.67,
    8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
}

# Візуалізація результатів
plt.figure(figsize=(10, 5))
plt.bar(probabilities.keys(), probabilities.values(), color='skyblue', label='Метод Монте-Карло')
plt.plot(analytical_probabilities.keys(), analytical_probabilities.values(), color='red', marker='o', label='Аналітичні значення')
plt.xlabel('Сума чисел на двох кубиках')
plt.ylabel('Ймовірність (%)')
plt.title('Ймовірності сум при киданні двох кубиків')
plt.legend()
plt.grid(True)
plt.show()

# Виведення результатів
print("Ймовірності за методом Монте-Карло:")
for sum_value, prob in probabilities.items():
    print(f"Сума {sum_value}: {prob:.2f}%")

print("\nАналітичні ймовірності:")
for sum_value, prob in analytical_probabilities.items():
    print(f"Сума {sum_value}: {prob:.2f}%")
