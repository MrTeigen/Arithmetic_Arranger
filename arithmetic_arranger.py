def arithmetic_arranger(problems, answers = False):

    # Checks that the array is within the allowed size.
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    
    first_line = ''
    second_line = ''
    third_line = ''
    fourth_line = ''

    '''This loop simply checks every item in the array and gives back an error code if data is not correct. We then start sorting into the different lines.'''
    for item in problems:
        
        split_items = item.split()
        if split_items[1] == ('/' or '*'):
            return "Error: Operator must be '+' or '-'."
        
        try:
            int(split_items[0])
            int(split_items[2])
        except ValueError:
            return 'Error: Numbers must only contain digits.'
        
        
        if (len(split_items[0]) > 4) or (len(split_items[2]) > 4):
            return 'Error: Numbers cannot be more than four digits.'
        
        
        if len(split_items[0]) == len(split_items[2]):
            first_line = first_line + '  ' + split_items[0]
            second_line = second_line + split_items[1] + ' ' + split_items[2]
            third_line = third_line + ('-' * (len(split_items[0]) + 2))
            fourth_line = fourth_line + (' ' * (len(split_items[0]) + 2 - len(str(eval(item))))) + str(eval(item))
        elif len(split_items[0]) < len(split_items[2]):
            dif_len = len(split_items[2]) - len(split_items[0])
            first_line = first_line + (' ' * (dif_len + 2)) + split_items[0]
            second_line = second_line + split_items[1] + ' ' + split_items[2]
            third_line = third_line + ('-' * (len(split_items[2]) + 2))
            fourth_line = fourth_line + (' ' * (len(split_items[2]) + 2 - len(str(eval(item))))) + str(eval(item))
        else:
            dif_len = len(split_items[0]) - len(split_items[2])
            first_line = first_line + (' ' * 2) + split_items[0]
            second_line = second_line + split_items[1] + (' ' * (dif_len + 1)) + split_items[2]
            third_line = third_line + ('-' * (len(split_items[0]) + 2))
            fourth_line = fourth_line + (' ' * (len(split_items[0]) + 2 - len(str(eval(item))))) + str(eval(item))           
            
            
        if item != problems[-1]:
            first_line = first_line + '    '
            second_line = second_line + '    '
            third_line = third_line + '    '
            fourth_line = fourth_line + '    '
    

    if answers == True:
        return first_line + '\n' + second_line + '\n' + third_line + '\n' + fourth_line
    else:
        return first_line + '\n' + second_line + '\n' + third_line
    