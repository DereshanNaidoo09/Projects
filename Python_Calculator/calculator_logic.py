#model
#calculates the equation

#variables
equation = []
operators = ['+', '-', '*', '/']

def calculate(equation_string):
    #converts string to array
    for i in range(len(equation_string)):
        if equation_string[i] in operators:
            equation.append(int(equation_string[0:i]))
            equation.append(equation_string[i])
            equation.append(int(equation_string[i+1:len(equation_string)]))

    #solves equation
    if equation[1] == operators[0]:
        answer = equation[0] + equation[2]
    
    elif equation[1] == operators[1]:
        answer = equation[0] - equation[2]

    if equation[1] == operators[2]:
        answer = equation[0] * equation[2]
        
    if equation[1] == operators[3]:
        answer = equation[0] / equation[2]
    
    #returns answer
    equation.clear()
    return answer