# to jest test do wlasnego modulu
import MyModule
print("Choose a figure (1 - circle) (2 - triangle) (3 - square):")
i = int(input())
if i == 1:
    j = 0
    while j == 0:
        print("Enter radius of your circle:")
        r = float(input())
        if r < 0:
            print("Radius must be greater than 0.")
        else:
            j = 1
    circle_1 = MyModule.Circle(r)
    p_circle_1 = circle_1.perimeter()
    a_circle_1 = circle_1.area()
    print("Perimeter of your circle is:", p_circle_1)
    print("Area of your circle is:", a_circle_1)
elif i == 2:
    j = 0
    while j == 0:
        print("Enter sides of your triangle:")
        a = float(input())
        b = float(input())
        c = float(input())
        if a < 0 or b < 0 or c < 0 or a >= b+c or b >= a+c or c >= a+b:
            print("Such triangle doesn't exist.")
        else:
            j = 1
    triangle_1 = MyModule.Triangle(a, b, c)
    p_triangle_1 = triangle_1.perimeter()
    a_triangle_1 = triangle_1.area()
    print("Perimeter of your triangle is:", p_triangle_1)
    print("Area of your triangle is:", a_triangle_1)
elif i == 3:
    j = 0
    while j == 0:
        print("Enter side of your square:")
        a = float(input())
        if a < 0:
            print("Side of square must be greater than 0")
        else:
            j = 1
    square_1 = MyModule.Square(a)
    p_square_1 = square_1.perimeter()
    a_square_1 = square_1.area()
    print("Perimeter of your square is:", p_square_1)
    print("Area of your square is:", a_square_1)
elif i < 1 or i > 3:
    print("You entered wrong number!")
