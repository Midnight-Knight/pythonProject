class SVG:
    def __init__(self):
        self.lines = []
        self.circles = []

    def line(self, x1, y1, x2, y2, color='black'):
        line = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" />'
        self.lines.append(line)

    def circle(self, cx, cy, r, color='black'):
        circle = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" />'
        self.circles.append(circle)

    def save(self, filename, width, height):
        svg_content = '<svg version="1.1" ' f'width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n'
        svg_content += '\n'.join(self.lines + self.circles)
        svg_content += '\n</svg>'

        with open(filename, 'w') as f:
            f.write(svg_content)

if __name__ == "__main__":
    svg = SVG()

    svg.line(10, 10, 60, 10, color='black')
    svg.line(60, 10, 60, 60, color='black')
    svg.line(60, 60, 10, 60, color='black')
    svg.line(10, 60, 10, 10, color='black')

    svg.circle(10, 10, r=5, color='red')
    svg.circle(60, 10, r=5, color='red')
    svg.circle(60, 60, r=5, color='red')
    svg.circle(10, 60, r=5, color='red')

    svg.save('pic.svg', 100, 100)
