import turtle
import math

# Функція для малювання дерева Піфагора
def draw_pythagoras_tree(t, branch_length, level, angle=45):
    if level == 0:
        return

    # Малюємо основну гілку
    t.forward(branch_length)
    
    # Зберігаємо поточну позицію і напрямок
    pos = t.position()
    heading = t.heading()
    
    # Малюємо праву гілку
    t.left(angle)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1, angle)
    
    # Повертаємось до початкової позиції і напрямку
    t.setposition(pos)
    t.setheading(heading)
    
    # Малюємо ліву гілку
    t.right(angle)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1, angle)

    # Повертаємось назад, щоб не залишати ліній на малюнку
    t.setposition(pos)
    t.setheading(heading)

# Ініціалізація вікна Turtle
screen = turtle.Screen()
screen.title("Дерево Піфагора")

# Ініціалізація Turtle
t = turtle.Turtle()
t.speed(0)  # Максимальна швидкість малювання
t.left(90)  # Повертаємо напрямок вгору

# Параметри малювання
initial_branch_length = 100
recursion_level = int(input("Введіть рівень рекурсії: "))

# Малюємо дерево
draw_pythagoras_tree(t, initial_branch_length, recursion_level)

# Завершуємо роботу
turtle.done()
