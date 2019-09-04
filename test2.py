expr = "(Z OR Y) AND D AND (((A OR B) AND C) ET D)"

expr2 = "(A OR B) AND C AND (D OR E)"

depth = expr.count("(")

def all_index(expression):

    list_index_op = []
    list_index_end = []

    for i, val in enumerate(expression):
        if expression[i] == "(" :
            list_index_op.append(i)
    for i, val in enumerate(expression):
        if expression[i] == ")" :
            list_index_end.append(i)
    return list_index_op, list_index_end

print(all_index(expr))


