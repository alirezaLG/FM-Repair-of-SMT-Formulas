from z3 import * 
from config import *

def replace_logical_operators(expr):
    # expr = Bool(str(expr))
    if is_and(expr):
        # Replace AND with your desired operation
        return Or(expr.children())
    elif is_or(expr):
        # Replace OR with your desired operation
        return And(expr.children())
    elif is_not(expr):
        # Replace NOT with your desired operation
        return expr.arg(0)
    else:
        # If it's not a logical operator, return as it is
        return expr


def convert_SMTlib_to_Z3Solver(smtlib_formula, index):
    # Split the formula into parts
    parts = smtlib_formula.strip().split()
    for part in parts:
        print("part " +part)
    # Extract the operator and operands
    operator = parts[0]
    # print('line '+str(index)+" operator " +operator)
    operands = parts[1:]
    # for operand in operands:
    #     print('line '+str(index)+" operand " +operand)
    # Convert operator and operands to Python/Z3 format
    python_formula = ""
    if operator == ">":
        python_formula = f"{operands[0]} + {operands[1]} < {operands[2]}"
    elif operator == "<":
        python_formula = f"{operands[0]} + {operands[1]} > {operands[2]}"
    # Add support for other operators as needed...

    return python_formula


def extract_constants_and_assertions_with_datatypes(formula_string):
    constants = {}
    assertions = []

    lines = formula_string.split('\n')

    for line in lines:
        if line.startswith('(declare-const'):
            parts = line.split()
            constant = parts[1]
            datatype = parts[2]
            constants[constant] = datatype[:-1]  # Remove the closing bracket
        elif line.startswith('(declare-fun'):
            parts = line.split()
            constant = parts[1]
            datatype = parts[3]
            constants[constant] = datatype[:-1]  # Remove the closing bracket
        elif line.startswith('(assert'):
            assertions.append(line)
            # assertions.append(line[8:-1])
            

    return constants, assertions
# print works only on Development mode
def print_d(*args, **kwargs):
    if dev:
        print(*args, **kwargs)

# print work only on Production mode 
def print_p(*args, **kwargs):
    if dev == False:
        print(*args, **kwargs)
