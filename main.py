#######################################
# IMPORTS
#######################################
from lexer import *
from parser1 import *
from interpreter1 import *


#######################################
# RUN
#######################################

global_symbol_table = SymbolTable()
global_symbol_table.set("फोल", Number(0))
global_symbol_table.set("खोटे", Number(0))
global_symbol_table.set("खरे", Number(1))


def run(fn, text):
    # Generate tokens
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    if error: return None, error

    # Generate AST
    parser = Parser(tokens)
    ast = parser.parse()
    if ast.error: return None, ast.error

    # Run program
    interpreter = Interpreter()
    context = Context('<program>')
    context.symbol_table = global_symbol_table
    result = interpreter.visit(ast.node, context)

    return result.value, result.error