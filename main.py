from figure import *
import os

# Функція для створення об'єкта фігури з рядка
def parse_figure(line):
    parts = line.strip().split()
    figure_type = parts[0]
    params = list(map(float, parts[1:]))

    if figure_type == 'Triangle':
        return Triangle(*params)
    elif figure_type == 'Rectangle':
        return Rectangle(*params)
    elif figure_type == 'Trapeze':
        return Trapeze(*params)
    elif figure_type == 'Parallelogram':
        return Parallelogram(*params)
    elif figure_type == 'Circle':
        return Circle(*params)
    elif figure_type == 'Ball':
        return Ball(*params)
    elif figure_type == 'TriangularPyramid':
        return TriangularPyramid(*params)
    elif figure_type == 'QuadrangularPyramid':
        return QuadrangularPyramid(*params)
    elif figure_type == 'RectangularParallelepiped':
        return RectangularParallelepiped(*params)
    elif figure_type == 'Cone':
        return Cone(*params)
    elif figure_type == 'TriangularPrism':
        return TriangularPrism(*params)
    else:
        raise ValueError(f"Unknown figure type: {figure_type}")

# Обробка одного файлу
def process_file(filepath):
    figures = []
    with open(filepath, 'r') as file:
        for line in file:
            if line.strip():
                try:
                    fig = parse_figure(line)
                    figures.append(fig)
                except Exception as e:
                    print(f"Помилка обробки рядка: {line.strip()} ({e})")

    if not figures:
        return f"Файл {filepath}: Немає коректних фігур.\n"

    # Знаходимо фігуру з найбільшою мірою
    max_figure = max(figures, key=lambda f: f.volume())

    result = f"Файл {filepath}:\nНайбільша міра: {max_figure.volume():.2f}\nТип фігури: {type(max_figure).__name__}\n"
    return result

# Основна частина програми
if __name__ == "__main__":
    input_files = ["inputs/input01.txt", "inputs/input02.txt", "inputs/input03.txt"]
    os.makedirs('outputs', exist_ok=True)

    with open('outputs/output.txt', 'w') as out:
        for filepath in input_files:
            if os.path.exists(filepath):
                result = process_file(filepath)
                print(result)
                out.write(result + "\n")
            else:
                print(f"Файл {filepath} не знайдено.")
                out.write(f"Файл {filepath} не знайдено.\n")
