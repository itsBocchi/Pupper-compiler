# -----------------------------------------------------------------------------
#Pupper
# -----------------------------------------------------------------------------

tokens = (
    'NAME','NUMBA',
    'PLUS','MINUS','TIMES','DIVIDE','EQUALS',
    'LPAREN','RPAREN', 'AND', 'WURD', 'TYPE', 'COM'
    )

# Tokens

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'\='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'   # r'[a-zA-Z_][a-zA-Z0-9_]*\!' solucion parche a diferenciacion entre nombre de variable y wurd
t_AND     = r'\&'
t_WURD    = r'[a-zA-Z_]+'
t_TYPE    = r'(numba)|(wurd)'
#t_GET     = r'get'
#t_ANDD    = r'and'
t_COM     = r'\''

def t_NUMBA(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Pupper can't count that much :( %d", t.value)
        t.value = 0
    return t

#def t_EQUALS(t):
    

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Pupper doesn't like that character >:( '%s'" % t.value[0]) #illegal character
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lexer = lex.lex()

# Parsing rules

precedence = (
    ('left','PLUS','MINUS','AND'),
    ('left','TIMES','DIVIDE'),
    ('right','UMINUS'),
    )

# dictionary of names
names = { }

def p_statement_declaration(t):  #NUEVO PARA HACER DIFERENCIA DE TIPO names[t[1]] = ["value","type"]
    'statement : NAME EQUALS TYPE'
    #names[t[1]] = ["value",t[3]]

def p_statement_assign(t):
    'statement : NAME EQUALS expression'
    #names[t[1]][0] = t[3]
    names[t[1]] = t[3]

def p_statement_expr(t):
    'statement : expression'
    print(t[1])

def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression AND expression'''
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]
    elif t[2] == '&': t[0] = '{0}{1}'.format(t[1],t[3])   #bosquejo de get together expression and expression

#def p_expression_add(t):
 #   'expression : GET expression ANDD expression'
  #  if t[1] == 'get': t[0] = '{0}{1}'.format(t[2],t[4])   #bosquejo de get together expression and expression

def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = -t[2]

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_expression_NUMBA(t):
    'expression : NUMBA'
    t[0] = t[1]

def p_expression_wurd(t): #ARREGLAAAAR
    'expression : COM WURD COM'
    if t[1] == '\'':
        t[0] = '{0}\n'.format(t[2])
    print("ud esta en la funcion para wurd")
    

def p_expression_name(t):
    'expression : NAME'
    try:
        #t[0] = names[t[1]][0]  #modificado antes era t[0] = names[t[1]]
        t[0] = names[t[1]]
    except LookupError:
        print("Pupper doesn't know that name :S '%s'" % t[1]) #undefined name
        t[0] = 0

def p_error(t):
    print("Pupper smells something weird: '%s'" % t.value)  #syntax error

import ply.yacc as yacc

if __name__ == '__main__':
    parser = yacc.yacc()
    s = input('pupper >> ')
    if s == "hey pupper":
        while True:
            try:
                s = input('pupper >> ')   # Use raw_input on Python 2
                if s == "stay safe gud doggo":
                    print("bye :p")
                    break
                elif s == "play dead":
                    print("bye xp")
                    break
            except EOFError:
                break
            parser.parse(s)
    else: print("u forgot 2 say something")
