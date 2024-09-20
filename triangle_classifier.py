import math


def classify_triangle(a, b, c):
    """Classifies the type of triangle based on the lengths of its sides."""
    if a <= 0 or b <= 0 or c <= 0:
        return "Not a triangle"

    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle"

    triangle_type = ""
    if a == b == c:
        triangle_type = "Equilateral triangle"
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles triangle"
    else:
        triangle_type = "Scalene triangle"

    sides = sorted([a, b, c])
    if round(sides[0] ** 2 + sides[1] ** 2, 5) == round(sides[2] ** 2, 5):
        triangle_type += " and Right triangle"

    return triangle_type


def main():
    print("Welcome to the Triangle Classifier!")

    while True:
        try:
            a = float(input("Enter length of side a: "))
            b = float(input("Enter length of side b: "))
            c = float(input("Enter length of side c: "))
        except ValueError:
            print("Please enter valid numeric values.")
            continue

        result = classify_triangle(a, b, c)
        print(f"The triangle is classified as: {result}")

        again = input(
            "Would you like to classify another triangle? (yes to continue, any other key to exit): ").strip().lower()
        if again != 'yes':
            print("Thank you for using the Triangle Classifier! Goodbye!")
            break


if __name__ == "__main__":
    main()
