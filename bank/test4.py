from z3 import *

# Declare p as a boolean constant
p = Bool('p')
# unsal_bool = And(Bool('p'), Not(Bool('p')))

print(type(And(p, Not(p))))
print(type(parse_smt2_string(str(And(p, Not(p))))))
# Create an And expression with nested operators
expr = parse_smt2_string(str(And(p, Not(p))))


# Define a function to detect and replace one logical operator at a time
def replace_one_logical_operator(expr):
    # expr = Bool(str(expr))
    if is_and(expr):
        print("AND operator is replaced with OR")
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
        print("else")
        return expr

# Apply the function to replace one logical operator at a time
expr_replaced = replace_one_logical_operator(expr)

print(expr_replaced)


# from z3 import *

# # Declare p as a boolean constant
# p = Bool('p')


# # Create an And expression
# expr = And(p, Not(p))
# # expr2 = "(and (= x 1) (or (= y 2) (> z 3)))"
# # parse_smt2_string(expr2, )
# print("expression children is:", (expr.arg(1)))

# # Define a function to detect and replace logical operators
# def replace_logical_operators(expr):
#     if is_and(expr):
#         # Replace AND with your desired operation
#         return Or(expr.children())
#     elif is_or(expr):
#         # Replace OR with your desired operation
#         return And(expr.children())
#     elif is_not(expr):
#         # Replace NOT with your desired operation
#         return expr.arg(0)
#     else:
#         # If it's not a logical operator, return as it is
#         return expr

# # Apply the function recursively to the expression
# expr_replaced = simplify(replace_logical_operators(expr))

# # Create a solver
# solver = Solver()

# # Add the modified expression to the solver
# solver.add(expr_replaced)

# # Check satisfiability
# if solver.check() == sat:
#     print("Satisfiable")
#     model = solver.model()
#     print("Model for p:", model)
# else:
#     print("Unsatisfiable")


# x = Int('x')
# y = Int('y')
# print ("simplify is: ",simplify(x + y + 2*x + 3))



# from z3 import *

# # Sample SMT-LIB formula
# smt_formula = "(and (= x 1) (or (= y 2) (> z 3)))"

# # Parse the formula
# parsed_formula = parse_smt2_string(smt_formula)

# # Function to recursively find logical operators
# def find_logical_operators(expr):
#     operators = []
#     if is_and(expr):
#         operators.add("AND")
#     elif is_or(expr):
#         operators.add("OR")
#     elif is_not(expr):
#         operators.add("NOT")
#     else:
#         for arg in expr.children():
#             operators.update(find_logical_operators(arg))
#     return operators

# # Find logical operators in the parsed formula
# logical_operators = find_logical_operators(parsed_formula)

# print("Logical operators found:", logical_operators)