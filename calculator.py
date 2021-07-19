run = True
vardictionary = {}
operatorlist = ['=','+', '-', '*', '/']

while run:
    defError = False

    order = input('')
    orderlist = order.split()

    if orderlist[0].lower() == 'quit':
        run = False
        continue

    #계산기 시작
    if orderlist[0] == 'def':
        if order.count('=') != 1:
            print('Error: invalid command')
            continue

        exp = order.split('def')[1]
        var_value = exp.split('=')
        var = var_value[0].strip()
        value = var_value[1].strip()

        for ope in operatorlist:
            if ope in var:
                defError = True
        if var.isdigit() == True:
            defError = True
        elif value.isdigit() == False:
            defError = True

        if defError:
            print('Error: invalid command')
            continue

        vardictionary[var] = int(value)

    elif orderlist[0] == 'calc':
        orderchar = list(order)
        if orderchar.count('+') + orderchar.count('-') + orderchar.count('*') + orderchar.count('/') != 1:
            print('Error: invalid command')
            continue

        for char in orderchar:
            if char == '+':
                operator = '+'

            elif char == '-':
                operator = '-'

            elif char == '*':
                operator = '*'

            elif char == '/':
                operator = '/'

        expression = order.split('calc')[1]
        var1_var2 = expression.split(operator)
        var1 = var1_var2[0].strip()
        var2 = var1_var2[1].strip()  
        varlist = vardictionary.keys()

        if var1 not in varlist:
            print('Error: variable is not defined')
            continue
        if var2 not in varlist:
            print('Error: variable is not defined')
            continue
        
        if operator == '+':
            result = vardictionary[var1] + vardictionary[var2]

        elif operator == '-':
           result = vardictionary[var1] - vardictionary[var2]
        
        elif operator == '*':
           result = vardictionary[var1] * vardictionary[var2]
        
        elif operator == '/':
            if vardictionary[var2] == 0:
                print('Error: division by zero')
                continue
            result = vardictionary[var1] / vardictionary[var2]

            if vardictionary[var1] % vardictionary[var2] == 0:
                result = int(result)
            elif int(result * 100) != (result * 100):
                    result = int((result * 100) + 1) / 100

        print(result)
        
    elif orderlist[0] == 'see':
        print('======'+ 'Variables' + '=====')

        for key in vardictionary.keys():
            print(key,':',' ',vardictionary[key],sep='')

        print('====================')

    else:
        print('undefined')
