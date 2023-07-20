import pprint as pp

def pprint(x): pp.pprint(x)

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a // b
def mod(a, b): return a % b

variables = {}
customFunctions = {}

def clear_out_variables():
    global variables
    variables = {}

def define(name, val):
    global variables
    variables[name] = val

def get_var(name):
    global variables
    if name in variables:
        return variables[name]
    else:
        raise RuntimeError("The variable {} is not defined in this context!".format(name))

def is_var(name):
    global variables
    return name in variables

def evaluate(instruction, variables):
    var_copy = variables.copy()

    def define(name, value):
        var_copy[name] = value

    def parseInstruction(ins, vars):
        if type(ins) == list:
            pprint("BEFORE:")
            pprint(ins)
            fname = ins[0]
            rest = ins[1:]
            if fname == "fn":
                args = rest[0]
                body = rest[1]
                return parseFnInstruction(args, body, var_copy)
            elif fname in functions:
                rest = [parseInstruction(x, vars) for x in ins[1:]]
                return functions[fname](*rest)
            elif fname in var_copy:
                rest = [parseInstruction(x, vars) for x in ins[1:]]
                return var_copy[fname](*rest)
            else:
                raise RuntimeError("Undefined function: {}".format(ins[0]))
        elif ins in var_copy:
            return var_copy[ins]
        else:
            return ins

    def parseFnInstruction(args, body, old_vars):
        def func(*values):
            new_vars = old_vars.copy()
            for (name, val) in zip(args, values):
                new_vars[name] = val
            return parseInstruction(body, new_vars)
        return func

    def do(*x): return x[-1]

    functions = {
        "print": print,
        "do": do,
        "def": define,
        "+": add,
        "-": sub,
        "*": mul,
        "/": div,
        "*": mod,
    }

    return parseInstruction(instruction, var_copy)

