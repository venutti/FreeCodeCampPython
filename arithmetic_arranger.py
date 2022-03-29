MAX_PROBLEMS = 5
MAX_DIGITS = 4
OPERATORS = "+-"
SEPARATOR = "    "

ERROR_MAX_PROBLEMS = "Error: Too many problems."
ERROR_OPERATOR = "Error: Operator must be '+' or '-'."
ERROR_NO_DIGIT = "Error: Numbers must only contain digits."
ERROR_MAX_DIGITS = "Error: Numbers cannot be more than four digits."


def restar(a,b):
    return a - b

def sumar(a,b):
    return a + b

mapeo_op = {
    "+":sumar,
    "-":restar,
}

def arithmetic_arranger(operations, solve=False):
    #Resuelvo cuando hay muchos problemas
    if len(operations) > MAX_PROBLEMS:
        return ERROR_MAX_PROBLEMS

    row1 = []
    row2 = []
    lines = []
    results = []
    arithmetic_operation = []

    for problem in operations:
        op1, operator, op2 = problem.split()

        #Resuelvo error de operando
        if operator not in OPERATORS:
            return ERROR_OPERATOR
        #Resuelvo cuando no son numeros
        try:
            n1 = int(op1)
            n2 = int(op2)
        except ValueError:
            return ERROR_NO_DIGIT
        #Resuelvo cuando los numeros son muy largos
        if len(op1) > MAX_DIGITS or len(op2) > MAX_DIGITS:
            return ERROR_MAX_DIGITS

        width = len(op1) if len(op1) > len(op2) else len(op2)
        #Ajusto los tamaños
        op1 = op1.rjust(width + 2)
        op2 = operator + op2.rjust(width + 1)
        line = "-"*(width + 2)

        row1.append(op1)
        row2.append(op2)
        lines.append(line)

        if solve:
            res = mapeo_op[operator]
            res = res(n1,n2)
            res = str(res)
            res = res.rjust(width + 2)
            results.append(res)

    arithmetic_operation.append("    ".join(row1))
    arithmetic_operation.append("    ".join(row2))
    arithmetic_operation.append("    ".join(lines))
    if solve:
        arithmetic_operation.append("    ".join(results))

    return "\n".join(arithmetic_operation)

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))