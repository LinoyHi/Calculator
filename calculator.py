def calculator():
    '''
    args:
        starting_num= the first number in the equation
        action = checks which action to use => '+' / '-' / '/' / '*' / '^' / '='
        num= next number in the equation
        again= another action or end
    
    returns:
        the result of the equation(all_numbers)
    '''
    caculate= input('would you want to caculate? if so enter"y":').lower()
    if caculate!='y':
        print('bye bye :)')
    else:
        starting_num= input('please enter a number:')
        while not starting_num.isdigit():
            starting_num= input('please enter a number:')
        all_numbers= [float(starting_num)]
        incase_power= [float(starting_num)]
        cal= True
        while cal:
            action= input('please enter one of this actions "-" , "+" , "/", "*", "^", "=":')
            if action=='-' or action=='+' or action=='/' or action=='*' or action=='^':
                num= input('enter another number:')
                while not num.isdigit():
                    num= input('please enter a number:')
                num= float(num)
                if action=='-' or action=='+':
                    if action== '-':
                        num= -num
                    all_numbers.append(num)
                    incase_power.append('!')
                elif action=='/':
                    while num==0:
                        print('math eror')
                        num= input('please enter a different number:')
                        while not num.isdigit():
                            num= input('please enter a different number:')
                        num= float(num)
                    last_num= all_numbers.pop()
                    all_numbers.append(last_num/num)
                    incase_power.append(last_num)
                    incase_power.append('/')
                    incase_power.append(num)
                elif action=='*':
                    last_num= all_numbers.pop()
                    all_numbers.append(last_num*num)
                    incase_power.append(last_num)
                    incase_power.append('*')
                    incase_power.append(num)
                elif action=='^':#in python power is done like so- num**num2
                    check= incase_power.pop()
                    last_num= all_numbers.pop()
                    if last_num==0 and not isinstance(check,float) or check==0:
                        while num<0:
                            num= float(input('enter a number bigger than 0:'))
                    if isinstance(check,float):
                        if len(incase_power)>0:
                            check_action= incase_power.pop()
                            if check_action== '/':
                                power= check**num
                                num_before= incase_power.pop()
                                new= num_before/power
                                all_numbers.append(new)
                            else:
                                power= check**num
                                num_before= incase_power.pop()
                                new= num_before*power
                                all_numbers.append(new)
                        else:
                            new= check**num
                            all_numbers.append(new)
                    else:
                        new= last_num**num
                        all_numbers.append(new)
            else:
                again= input('would you like to do another action?if not enter"=" if yes enter anything else:')
                if again== '=':
                    cal= False
        if not cal:
            length= len(all_numbers)
            for i in range (1,length):
                all_numbers[0]+=all_numbers[i] 
            print(all_numbers[0])
calculator()