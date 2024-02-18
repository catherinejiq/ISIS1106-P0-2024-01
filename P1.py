import os
import re
class RobotLanguageParser:
    def __init__(self):
        self.variables = {}
        self.functions = {}
    def check_syntax(self, program):
        instructions = program.split("\n")
        for instruction in instructions:
            instruction = instruction.strip()
            palabra = re.sub(r'[()]', '', instruction)
            if not palabra:
                continue

            print("evaluando instrucción:", palabra)

            if palabra.startswith("defvar"):
                self.define_variable(palabra)
                print('definiendo variable')

            elif palabra.startswith("="):
                self.assign_value(palabra)
                print('asignando variable')

            elif palabra.startswith("move"):
                print('asignando move')
                self.move(palabra)

            elif palabra.startswith("skip"):
                print('asignando skip')
                self.skip(palabra)

            elif palabra.startswith("turn"):
                print('asignando turn')
                self.turn(palabra)

            elif palabra.startswith("face"):
                print('asignando face')
                self.face(palabra)

            elif palabra.startswith("put"):
                print('asignando put')
                self.put(palabra)

            elif palabra.startswith("pick"):
                print('asignando pick')
                self.pick(palabra)

            elif palabra.startswith("move-dir"):
                print('asignando move-dir')
                self.move_dir(palabra)

            elif palabra.startswith("run-dirs"):
                print('asignando run-dirs')
                self.run_dirs(palabra)

            elif palabra.startswith("move-face"):
                print('asignando move-face')
                self.move_face(palabra)

            elif palabra.startswith("if"):
                print('asignando if')
                self.if_condition(palabra)

            elif palabra.startswith("loop"):
                print('asignando loop')
                self.loop(palabra)

            elif palabra.startswith("repeat"):
                print('asignando repeat')
                self.repeat(palabra)

            elif palabra.startswith("defun"):
                print('asignando defun')
                self.define_function(palabra)

            elif palabra in self.functions:
                print(self.functions)
                print('asignando nueva fun')
                self.define_fun(palabra)

            elif palabra.startswith("null"):
                print('asignando null')
                self.define_null()

            else:
                parts = palabra.split()
                if parts[0] in self.functions:
                    if len(parts) != len(self.functions[parts[0]]) + 1:
                        print("Instruccion invalida", palabra)
                        return False
                else:
                    print("Instruccion invalida", palabra)
                    return False

        return True


    def define_variable(self, instruction):
        parts = instruction.split()
        if len(parts) != 3:
            print("Instrucción de definición de variable no válida.")
            return

        name = parts[1]
        value = parts[2]
        self.variables[name] = value


    def define_function(self,instruction):
        parts = instruction.split()
        if len(parts)<3:
            print('Instrucción de definición de función inválida')
            return
        function_name = parts[1]
        parameters = parts[2:]
        self.functions[function_name] = parameters
        print(self.functions)
        print("Función definida:", function_name)
        print("Parámetros:", parameters)

    def define_fun(self, instruction):
        parts = instruction.split()
        if len(parts) < 2:
            print("Instrucción de función de definición no válida.")
            return

        function_name = parts[1]
        if function_name not in self.functions:
            print("Funcion no definida " + function_name)
            return

        parameters = parts[2:]
        if len(parameters) != len(self.functions[function_name]):
            print("El recuento de parámetros no coincide con la función: " + function_name)
            return

        self.execute_function(function_name, parameters)

    def execute_instruction(self, instruction):
        parts = instruction.split()
        if parts[0] == 'foo':
            if len(parts) != len(self.functions['foo']) + 1:
                print("Numero de argumentos no válido para la función foo.")
                return
            self.execute_function('foo', parts[1:])
        else:
            print("Instruccion invalida", instruction)

    def execute_function(self, function_name, arguments):
        if function_name not in self.functions:
            print("Funcion no definida:", function_name)
            return
        parameters = self.functions[function_name]

        parameter_mapping = {}
        for i in range(len(parameters)):
            parameter_mapping[parameters[i]] = arguments[i]

        print("Funcion ejecutada:", function_name)
        print("Argumentos", parameter_mapping)

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

    def definep(self):
        return

    def define_null(self):
        return

    def extract_function_info(self,instruction):
        match = re.match(r"\(defun\s+([\w_]+)\((.*)\)", instruction)
        if match:
            function_name = match.group(1)
            params = match.group(2).split(',')
            params=[p.strip for p in params]
            return function_name, params
        else:
            return None,None

    def block(self, instruction):
        parts = instruction.split()
        if len(parts) < 2:
            print("Invalid block instruction.")
            return

        block = parts[1]


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
    print("Respuesta final: Sí")
else:
    print("Respuesta final: No")