sum1=0
counter=0
while True:
    
    input1=input('Enter your numbers please: ')
    if input1=='':
        numbers=215610008416 #very 
        break
    else:
        numbers=input1
    if numbers.isnumeric()==False:
        print('Error! Enter only numbers! ')
        break
    numbers=int(input1)
    counter+=1
    match numbers:
        case 0:
            print('Cant divide to ZERO ;)')
            break
        case 215610008416:
            break
        case _:
            sum1+=numbers
if counter==0:
    exit()
else:
    print(f'The sum is: {sum1}')
    print(counter)
    print(f'The average is:{round(sum1/counter,2)}')