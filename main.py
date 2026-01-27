from utils.methods import MyClass

if __name__ == "__main__":
    obj = MyClass(3, 5)
    print("Addition:", obj.add())
    print("Multiplication:", obj.multiply())
    print("Subtraction:", obj.subtract())
    print("Sum of Squares:", obj.sum_squares())

    print()
    print(help(MyClass))