STOP_VAL = -999

running_sum = 0

INPUT_MSG = 'please enter positivenum( ' + str(STOP_VAL) + ' to stop):'

the_num = int(input(INPUT_MSG))

while the_num != STOP_VAL:
    running_sum += the_num
    the_num = int(input(INPUT_MSG))

print('running sum is', running_sum)