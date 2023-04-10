class HTML:
    def __init__(self):
        self.text = ""
        self.stack = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        tag = self.stack.pop()
        self.text += f"</{tag}>\n"

    def body(self):
        self.text += "<body>\n"
        self.stack.append("body")
        return self

    def div(self):
        self.text += "<div>\n"
        self.stack.append("div")
        return self

    def p(self, text):
        self.text += "<p>"
        self.text += text
        self.text += "</p>\n"
        return self


if __name__ == "__main__":
    html = HTML()
    with html.body():
        with html.div():
            with html.div():
                html.p('Первая строка.')
                html.p('Вторая строка.')
            with html.div():
                html.p('Третья строка.')
    print(html.text)

