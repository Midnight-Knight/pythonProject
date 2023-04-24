import os
from graphviz import Digraph

def generate_module_hierarchy(project_path):
    module_hierarchy = Digraph('Module Hierarchy', format='png') # Создаем объект графа

    # Рекурсивная функция для анализа модулей в проекте
    def analyze_modules(path, parent=None):
        if os.path.isdir(path): # Если текущий элемент является директорией
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                module_hierarchy.node(item_path, label=item) # Добавляем узел в граф с именем директории
                if parent: # Если есть родительский узел, добавляем связь между родителем и текущим узлом
                    module_hierarchy.edge(parent, item_path)
                analyze_modules(item_path, item_path) # Рекурсивно анализируем поддиректорию
        elif path.endswith('.py'): # Если текущий элемент является Python-модулем
            module_name = os.path.splitext(os.path.basename(path))[0] # Извлекаем имя модуля без расширения
            module_hierarchy.node(path, label=module_name) # Добавляем узел в граф с именем модуля
            if parent: # Если есть родительский узел, добавляем связь между родителем и текущим узлом
                module_hierarchy.edge(parent, path)

    analyze_modules(project_path) # Запускаем анализ модулей с указанной директории

    module_hierarchy.render('module_hierarchy', view=True)

if __name__ == "__main__":
    project_path = 'module_test3.py'
    generate_module_hierarchy(project_path)
