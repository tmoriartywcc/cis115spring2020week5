START_NUM = 1
END_NUM = 60

running_sum = 0

for the_num in range(START_NUM, END_NUM+1):
    running_sum += the_num
    #running_sum = running_sum + the_num

print('running sum is', running_sum)

