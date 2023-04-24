class Tree:
    scale_x = 25
    scale_y = 50

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.x = 0
        self.y = 0

    def visualize(self, svg, x=0, y=0):
        self.x = x
        self.y = y

        if self.left is not None:
            self.left.visualize(svg, x, y + 1)

        svg.circle(self.x * Tree.scale_x, self.y * Tree.scale_y, r=5, color='black')  # Draw node as a circle

        if self.right is not None:
            self.right.visualize(svg, x, y + 1)

class SVG:
    def __init__(self):
        self.lines = []
        self.circles = []
        self.texts = []

    def line(self, x1, y1, x2, y2, color='black'):
        self.lines.append((x1, y1, x2, y2, color))

    def circle(self, cx, cy, r, color='black'):
        self.circles.append((cx, cy, r, color))

    def text(self, x, y, text, color='black'):
        self.texts.append((x, y, text, color))

    def save(self, filename, width, height):
        with open(filename, 'w') as f:
            f.write(f'<svg version="1.1" width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n')
            for line in self.lines:
                f.write(f'<line x1="{line[0]}" y1="{line[1]}" x2="{line[2]}" y2="{line[3]}" stroke="{line[4]}" />\n')
            for circle in self.circles:
                f.write(f'<circle cx="{circle[0]}" cy="{circle[1]}" r="{circle[2]}" fill="{circle[3]}" />\n')
            for text in self.texts:
                f.write(f'<text x="{text[0]}" y="{text[1]}" fill="{text[3]}">{text[2]}</text>\n')
            f.write('</svg>')



if __name__ == "__main__":
    svg = SVG()

    tree_2 = Tree(2, Tree(3, Tree(4), Tree(5)), Tree(6, Tree(7)))
    tree_8 = Tree(8, Tree(9, Tree(10), Tree(11, Tree(12), Tree(13))), Tree(14))
    tree = Tree(1, tree_2, tree_8)

    tree.visualize(svg, 0, 0)

    svg.save('tree.svg', 500, 500)

    svg.save('tree.svg', 800, 800)