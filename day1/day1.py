with open('input.txt') as f:
    data = f.read().splitlines()
    previous_num = 0
    positive = -1
    for current_line in data:
        if int(current_line) > int(previous_num):
            positive+=1
        previous_num = current_line
    f.close()
    print(positive)

