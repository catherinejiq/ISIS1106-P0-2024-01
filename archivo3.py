import os

class RobotLanguageParser:
    def __init__(self):
        self.variables = {}
        self.functions = {}

def check_syntax(self, program):
        instructions = program.split("\n")

        stack = []  # Stack to keep track of opening parentheses

        for instruction in instructions:
            instruction = instruction.strip()

            if not instruction:
                continue  # Skip empty lines

            for char in instruction:
                if char == '(':
                    stack.append(char)
                elif char == ')':
                    if not stack:
                        print("Unmatched closing parenthesis.")
                        return False
                    stack.pop()

            if instruction.startswith("(defvar"):
                self.define_variable(instruction)

            elif instruction.startswith("(= "):
                self.assign_value(instruction)

            elif instruction.startswith("(move"):
                self.move(instruction)

            elif instruction.startswith("(skip"):
                self.skip(instruction)

            elif instruction.startswith("(turn"):
                self.turn(instruction)

            elif instruction.startswith("(face"):
                self.face(instruction)

            elif instruction.startswith("(put"):
                self.put(instruction)

            elif instruction.startswith("(pick"):
                self.pick(instruction)

            elif instruction.startswith("(move-dir"):
                self.move_dir(instruction)

            elif instruction.startswith("(run-dirs"):
                self.run_dirs(instruction)

            elif instruction.startswith("(move-face"):
                self.move_face(instruction)

            elif instruction.startswith("(if"):
                self.if_condition(instruction)

            elif instruction.startswith("(loop"):
                self.loop(instruction)

            elif instruction.startswith("(repeat"):
                self.repeat(instruction)

            elif instruction.startswith("(defun"):
                self.define_function(instruction)

            elif instruction.startswith("(null)"):
                pass  # Null instruction, do nothing

            elif instruction.startswith("(") and not instruction.endswith(")"):
                self.block(instruction)

            else:
                print("Invalid instruction: " + instruction)
                return False

        if stack:
            print("Unmatched opening parenthesis.")
            return False

        return True

def define_variable(self, instruction):
        parts = instruction.split()
        if len(parts) != 3:
            print("Invalid define variable instruction.")
            return

        name = parts[1]
        value = parts[2]
        self.variables[name] = value

def if_condition(self, instruction):
    parts = instruction.split()
    if len(parts) < 2:
        print("Invalid if condition instruction.")
        return False

    condition = " ".join(parts[1:])
    if condition.startswith("(facing?"):
        facing_condition = condition[10:]
        if facing_condition not in ["north", "south", "east", "west"]:
            print("Invalid facing direction.")
            return False
    elif condition.startswith("(blocked?)") or condition.startswith("(not (blocked?))"):
        pass
    elif condition.startswith("(can-put?") or condition.startswith("(can-pick?"):
        parts = condition.split("?")
        if len(parts) != 2:
            print(f"Invalid {parts[0]} condition.")
            return False

        object_type = parts[1].split()[1]
        if object_type not in ["chips", "balloons"]:
            print(f"Invalid object type in {parts[0]} condition.")
            return False
    elif condition.startswith("(can-move?"):
        parts = condition.split("?")
        if len(parts) != 2:
            print("Invalid can-move? condition.")
            return False

        direction = parts[1][9:]
        if direction not in ["north", "south", "west", "east"]:
            print("Invalid direction in can-move? condition.")
            return False
    elif condition.startswith("(isZero?"):
        parts = condition.split("?")
        if len(parts) != 2:
            print("Invalid isZero? condition.")
            return False

        value = parts[1][7:]
    elif condition.startswith("(not ") and condition.endswith(")"):
        condition = condition[5:-1]
        if not self.is_condition_valid(condition):
            return False
    else:
        print("Invalid if condition instruction.")
        return False

    return True

def block(self, instruction):
        parts = instruction.split(")(")
        if len(parts) < 2:
            print("Invalid block instruction.")
            return False

        block_instructions = parts[1].split(")(")
        for block_instruction in block_instructions:
            if not self.check_syntax(block_instruction):
                return False

        return True

def define_variable(self, instruction):
        parts = instruction.split()
        if len(parts) != 3:
            print("Invalid define variable instruction.")
            return

        name = parts[1]
        value = parts[2]
        self.variables[name] = value

def assign_value(self, instruction):
        parts = instruction.split()
        if len(parts) != 3:
            print("Invalid assignment instruction.")
            return

        name = parts[1]
        value = parts[2]

        if name not in self.variables:
            print("Variable not defined: " + name)
            return

        self.variables[name] = value

def move(self, instruction):
        parts = instruction.split()
        if len(parts) < 2:
            print("Invalid move instruction.")
            return

        steps = parts[1]

def skip(self, instruction):
        parts = instruction.split()
        if len(parts) < 2:
            print("Invalid skip instruction.")
            return

        steps = parts[1]

def turn(self, instruction):
        parts = instruction.split()
        if len(parts) != 2:
            print("Invalid turn instruction.")
            return

        direction = parts[1]

def face(self, instruction):
        parts = instruction.split()
        if len(parts) != 2:
            print("Invalid face instruction.")
            return

        direction = parts[1]

def put(self, instruction):
        parts = instruction.split()
        if len(parts) != 3:
            print("Invalid put instruction.")
            return

        object_type = parts[1]
        quantity = parts[2]

def pick(self, instruction):
        parts = instruction.split()
        if len(parts) != 3:
            print("Invalid pick instruction.")
            return

        object_type = parts[1]
        quantity = parts[2]

def move_dir(self, instruction):
        parts = instruction.split()
        if len(parts) != 3:
            print("Invalid move_dir instruction.")
            return

        steps = parts[1]
        direction = parts[2]

def run_dirs(self, instruction):
        parts = instruction.split()
        if len(parts) != 2:
            print("Invalid run_dirs instruction.")
            return

        directions = parts[1].split(",")

def move_face(self, instruction):
        parts = instruction.split()
        if len(parts) != 3:
            print("Invalid move_face instruction.")
            return

        steps = parts[1]
        direction = parts[2]

def loop(self, instruction):
        parts = instruction.split()
        if len(parts) < 2:
            print("Invalid loop instruction.")
            return

        condition = parts[1]

def repeat(self, instruction):
        parts = instruction.split()
        if len(parts) < 2:
            print("Invalid repeat instruction.")
            return

        times = parts[1]

def block(self, instruction):
        parts = instruction.split(")(")
        if len(parts) < 2:
            print("Invalid block instruction.")
            return

        block_instructions = parts[1].split(")(")

def define_function(self, instruction):
        parts = instruction.split()
        if len(parts) < 4:
            print("Invalid define function instruction.")
            return

# Function to check the robot program
def check_robot_program(program):
    parser = RobotLanguageParser()
    return parser.check_syntax(program)

# Function to get the file path from user input
def get_file_path():
    return input("Enter the file path: ")

# Function to validate a command
def is_valid_command(command):
    if isinstance(command, str) and command.strip() != '':
        words = command.split()
        return len(words) > 0
    return False

# Function to check the validity of user input
def check_command(input_string):
    command = input_string.strip()
    return is_valid_command(command)

# Get the file path from the user
file_path = get_file_path()

# Check if the file path is valid
if not os.path.isfile(file_path):
    print("Invalid file path.")
else:
    # Read the program from the file
    with open(file_path, "r") as file:
        program = file.read()

    # Check the syntax of the robot program
    if check_robot_program(program):
        print("Yes")
    else:
        print("No")