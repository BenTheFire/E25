import getpass
import time
import os


class ControlTerminal:
    terminal: str = None
    options: {int: str} = None

    def __init__(self):
        self.options = {}
        python_files = [f for f in os.listdir("ErettsegiGyakPy") if f.endswith(".py")]
        self.options = {i + 1: os.path.join("ErettsegiGyakPy", file) for i, file in enumerate(python_files)}

        self.terminal = ("-- Enter Q to quit the program\n"
                         "-- Enter C for contributors\n"
                         "-- Enter L for license\n"
                         "-- Enter H to see this menu\n"
                         "-- Enter the number for the corresponding section, to run it's code.")
        self.terminal += "\n//------------------------//"
        for i, file in self.options.items():
            self.terminal += f"\n{i} - {file}"

    def user_input_command(self):
        print(self.terminal)
        while True:
            user_input = input("Enter your choice: ")
            if user_input.lower() == 'q':
                print("Exiting the program...")
                break
            elif user_input.lower() == 'c':
                print("Contributors:\n- Pongrácz Benedek (https://github.com/BenTheFire)")
            elif user_input.lower() == 'l':
                print("License: MIT License")
            elif user_input.lower() == 'h':
                print(self.terminal)
            else:
                try:
                    choice = int(user_input)
                    if choice in self.options.keys():
                        print(f"Running {self.options[choice]}...")
                        os.system(f"python {self.options[choice]}")
                    else:
                        print(f"Invalid choice: {choice}. Please enter a_esemeny number between 1 and {len(self.options)}.")
                except ValueError:
                    print(f"You entered: {user_input}")
                    time.sleep(1)
                    print("Invalid input. Please try again.")
                time.sleep(1)

    def __str__(self):
        return self.terminal


def main():
    # grab username of the user from the system
    username = getpass.getuser()
    print(f"Welcome {username} to the Python world!")
    time.sleep(1)
    print("In this course, we will learn about Python programming.")
    time.sleep(1)
    print("Python is a_esemeny versatile language that can be used for various applications.")
    time.sleep(1)
    print("Below, you will find our control terminal.")
    time.sleep(1)
    print("\n------------------------\n")
    print("Control Terminal")
    ct = ControlTerminal()
    ct.user_input_command()
    print(ct)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
