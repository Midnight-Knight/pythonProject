import os
from graphviz import Digraph

def generate_module_hierarchy(project_path):
    module_hierarchy = Digraph('Module Hierarchy', format='png') # Создаем объект графа

    # Рекурсивная функция для анализа модулей в проекте
    def analyze_modules(path, parent=None):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path): # Если текущий элемент является директорией
                module_hierarchy.node(item_path, label=item) # Добавляем узел в граф с именем директории
                if parent: # Если есть родительский узел, добавляем связь между родителем и текущим узлом
                    module_hierarchy.edge(parent, item_path)
                analyze_modules(item_path, item_path) # Рекурсивно анализируем поддиректорию
            elif item_path.endswith('.py'): # Если текущий элемент является Python-модулем
                module_name = os.path.splitext(item)[0] # Извлекаем имя модуля без расширения
                module_hierarchy.node(item_path, label=module_name) # Добавляем узел в граф с именем модуля
                if parent: # Если есть родительский узел, добавляем связь между родителем и текущим узлом
                    module_hierarchy.edge(parent, item_path)

    analyze_modules(project_path) # Запускаем анализ модулей с указанной директории

    module_hierarchy.render('module_hierarchy', view=True) # Визуализация графа и сохранение в файл

# Пример использования
project_path = '/path/to/your/project' # Замените на путь к вашему проекту
generate_module_hierarchy(project_path)
