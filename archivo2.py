import os
class RobotLanguageParser:
    def __init__(self):
        self.variables = {}
        self.functions = {}

    def check_syntax(self, program):
        instructions = program.split("\n")
        
        for instruction in instructions:
            instruction = instruction.strip()

            if instruction.startswith("(defvar"):
                self.define_variable(instruction)

            elif instruction.startswith("= name"):
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

            elif instruction.startswith("(") and not instruction.endswith(")"):
                self.block(instruction)

            else:
                print("Invalid instruction: " + instruction)
                return False

        return True

    def define_variable(self, instruction):
        parts = instruction.split()
        if len(parts) < 4:
            print("Invalid define variable instruction.")
            return

        name = parts[1]
        value = parts[2]
        self.variables[name] = value

    def assign_value(self, instruction):
        parts = instruction.split()
        if len(parts) < 3:
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
        if len(parts) < 2:
            print("Invalid turn instruction.")
            return

        direction = parts[1]

    def face(self, instruction):
        parts = instruction.split()
        if len(parts) < 3:
            print("Invalid face instruction.")
            return

        direction = parts[2]

    def put(self, instruction):
        parts = instruction.split()
        if len(parts) < 3:
            print("Invalid put instruction.")
            return

        object_type = parts[1]
        quantity = parts[2]

        

    def pick(self, instruction):
        parts = instruction.split()
        if len(parts) < 3:
            print("Invalid pick instruction.")
            return

        object_type = parts[1]
        quantity = parts[2]

        

    def move_dir(self, instruction):
        parts = instruction.split()
        if len(parts) < 2:
            print("Invalid move_dir instruction.")
            return

        steps = parts[1]
        direction = parts[2]

    def run_dirs(self, instruction):
        parts = instruction.split()
        if len(parts) < 2:
            print("Invalid run_dirs instruction.")
            return

        directions = parts[1].split(",")

        

    def move_face(self, instruction):
        parts = instruction.split()
        if len(parts) < 3:
            print("Invalid move_face instruction.")
            return

        steps = parts[1]
        direction = parts[2]

    def if_condition(self, instruction):
        parts = instruction.split()
        if len(parts) < 2:
            print("Invalid if condition instruction.")
            return

        condition = parts[1]

    def loop(self, instruction):
        parts = instruction.split()
        if len(parts) < 3:
            print("Invalid loop instruction.")
            return

        condition = parts[1]
        block = parts[2]

    def repeat(self, instruction):
        parts = instruction.split()
        if len(parts) < 3:
            print("Invalid repeat instruction.")
            return

        times = parts[2]
        block = parts[1]

    def define_function(self, instruction):
        parts = instruction.split()
        if len(parts) < 4:
            print("Invalid define function instruction.")
            return

        name = parts[1]
        params = parts[2].split(",")
        commands = parts[3].split(")")[0]

        self.functions[name] = commands

    def block(self, instruction):
        parts = instruction.split()
        if len(parts) < 2:
            print("Invalid block instruction.")
            return

        block = parts[1]

        

def check_robot_program(program):
    parser = RobotLanguageParser()
    return parser.check_syntax(program)


def check_robot_program(program):
    parser = RobotLanguageParser()
    return parser.check_syntax(program)


def check_robot_program(program):
    parser = RobotLanguageParser()
    return parser.check_syntax(program)


def get_file_path():
    return input("Ingrese la ruta del archivo: ")

def is_valid_command(command):
    if isinstance(command, str) and command.strip() != '':
        words = command.split()
        return len(words) > 0
    return False


def check_command(input_string):
    command = input_string.strip()
    return is_valid_command(command)


file_path = get_file_path()
if not os.path.isfile(file_path):
    print("Ruta de archivo inválida.")
else:
    with open(file_path, "r") as file:
        program = file.read()

if check_robot_program(program):
    print("Sí")
else:
    print("No")