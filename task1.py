def replace_variables():
    variables = globals()
    for name, value in variables.items():
        if name.endswith('s') and name[:-1] in variables:
            variables[name[:-1]] = variables[name]
            variables[name] = None


s = 500
girls = "Masha"
girl = "xxx"
boys = "Pasha"
boy = "xxx"

replace_variables()
print(*filter(lambda x: not x[0].startswith('__'), globals().items()))