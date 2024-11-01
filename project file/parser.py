import ply.yacc as yacc
from lexer import tokens

# Global list to store generated intermediate code
intermediate_code = []
temp_count = 0  # Counter for temporary variables

def new_temp():
    global temp_count
    temp = f't{temp_count}'
    temp_count += 1
    return temp

# Production rules for arithmetic expressions with intermediate code generation

def p_expression_plus(p):
    'expression : expression PLUS term'
    global intermediate_code
    p[0] = new_temp()
    code = f"{p[0]} = {p[1]} + {p[3]}"
    intermediate_code.append(code)

def p_expression_minus(p):
    'expression : expression MINUS term'
    global intermediate_code
    p[0] = new_temp()
    code = f"{p[0]} = {p[1]} - {p[3]}"
    intermediate_code.append(code)

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    global intermediate_code
    p[0] = new_temp()
    code = f"{p[0]} = {p[1]} * {p[3]}"
    intermediate_code.append(code)

def p_term_divide(p):
    'term : term DIVIDE factor'
    global intermediate_code
    p[0] = new_temp()
    code = f"{p[0]} = {p[1]} / {p[3]}"
    intermediate_code.append(code)

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_id(p):
    'factor : ID'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

# Function to parse an expression and return intermediate code
def parse_expression(expression):
    global intermediate_code
    intermediate_code = []  # Reset intermediate code list before parsing
    parser.parse(expression)
    return intermediate_code
