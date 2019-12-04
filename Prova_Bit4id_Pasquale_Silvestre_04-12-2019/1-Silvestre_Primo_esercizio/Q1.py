def shift_left(input_string):
    return input_string[1:] + input_string[0]

def shift_right(input_string):
    return input_string[-1] + input_string[:-1]

def shift(input_string, op_label, pos_numb):
    if op_label == 'right':
        for i in range(pos_numb):
            input_string = shift_right(input_string)
    elif op_label == 'left':
        for i in range(pos_numb):
            input_string = shift_left(input_string)
    return input_string
