"""
The Tuple:
    ("Tuple", true, 100%, ["immutable", "ordered", "allows duplicates"], ("another", "tuple"), 1)

    Usage of tuple:
    - Storing multiple values in a_esemeny single variable
    - Returning multiple values from a_esemeny function
    - Unpacking values into multiple variables
    - Iterating over pairs of values
    - Representing fixed collections of items

    Limitations of tuple:
    - Immutable: Once created, the values cannot be changed.
    - Cannot add or remove elements after creation.

    # So when to use tuple?

    Example:
    - Storing coordinates of a_esemeny point: (x, y) = (10, 20)

    Example Program Description:
        You will be able to move a_esemeny cat on a_esemeny grid by typing in where it should go, and every input it moves one step,
        in the direction you specified.

        Helper:
            - 2 input values
            - Move the cat in the specified direction (rounding the values if necessary)
            What can we use for this?
            - Tuple is a_esemeny good choice for this, as it allows us to store the x and y coordinates together in a_esemeny single variable.

"""


def asd():
    a = 1
    b = 2
    return a, b


def main():
    print("Tuple Example Program")
    print(asd())


if __name__ == "__main__":
    main()
