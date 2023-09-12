class Visitor:
    def visit_circle(self, circle):
        pass

    def visit_rectangle(self, rectangle):
        pass

class Circle:
    def accept(self, visitor):
        visitor.visit_circle(self)

class Rectangle:
    def accept(self, visitor):
        visitor.visit_rectangle(self)

class AreaCalculator(Visitor):
    def visit_circle(self, circle):
        print("Calculando a área do círculo")

    def visit_rectangle(self, rectangle):
        print("Calculando a área do retângulo")

class PerimeterCalculator(Visitor):
    def visit_circle(self, circle):
        print("Calculando o perímetro do círculo")

    def visit_rectangle(self, rectangle):
        print("Calculando o perímetro do retângulo")

if __name__ == "__main__":
    circle = Circle()
    rectangle = Rectangle()

    area_calculator = AreaCalculator()
    perimeter_calculator = PerimeterCalculator()

    circle.accept(area_calculator)
    rectangle.accept(area_calculator)

    circle.accept(perimeter_calculator)
    rectangle.accept(perimeter_calculator)