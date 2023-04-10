import inspect

def generate_api_docs(module_name):
    module = __import__(module_name)
    module_doc = inspect.getdoc(module)
    classes = inspect.getmembers(module, inspect.isclass)
    functions = inspect.getmembers(module, inspect.isfunction)

    api_docs = f"# Модуль {module_name}\n\n{module_doc}\n\n"

    for class_name, class_obj in classes:
        class_doc = inspect.getdoc(class_obj)
        class_methods = inspect.getmembers(class_obj, inspect.ismethod)
        class_docs = f"## Класс {class_name}\n\n{class_doc}\n\n"

        for method_name, method_obj in class_methods:
            method_doc = inspect.getdoc(method_obj)
            method_args = inspect.signature(method_obj).parameters
            method_signature = f"**Метод** `{method_name}({', '.join(method_args)})`\n\n"
            method_docs = f"{method_signature}{method_doc}\n\n"
            class_docs += method_docs

        api_docs += class_docs

    for function_name, function_obj in functions:
        function_doc = inspect.getdoc(function_obj)
        function_args = inspect.signature(function_obj).parameters
        function_signature = f"Сигнатура: `{function_name}({', '.join(function_args)})`\n\n"
        function_docs = f"## Функция {function_name}\n\n{function_signature}{function_doc}\n\n"
        api_docs += function_docs

    return api_docs

if __name__ == "__main__":
    module_name = "module_test"
    api_docs = generate_api_docs(module_name)
    print(api_docs)