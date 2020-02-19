def get_input():
    """
    Receives an input from user
    """
    try:
        a0 = float(input("First and second sides: "))
        b0 = float(input("Third side: "))
        accuracy0 = float(input("Accuracy: "))
        return a0, b0, accuracy0
    except ValueError:
        print("Please enter floats")
        return get_input()


def main():
    a, b, accuracy = get_input()
    coordinates = {"A": (0, 0), "B": (a, 0), "C": (a / 2, (b * b - a * a / 4) ** 0.5)}
    x = 0
    tangent = coordinates["C"][1] / (a / 2)
    while x * tangent < a / 2 - x:
        x += accuracy / 2
    return x * tangent


if __name__ == "__main__":
    print(main())
