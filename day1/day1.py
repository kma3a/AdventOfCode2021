# with open('input.txt') as f:
#     data = f.read().splitlines()
#     previous_num = 0
#     positive = -1
#     for current_line in data:
#         if int(current_line) > int(previous_num):
#             positive+=1
#         previous_num = current_line
#     f.close()
#     print(positive)

with open('input.txt') as f:
    data = f.read().splitlines()
    array = [int(data.pop(0)),int(data.pop(0)),int(data.pop(0))]
    previous_sum = sum(array)
    positive = 0
    while len(data) > 0:
        array.pop(0)
        array.append(int(data.pop(0)))
        current_sum = sum(array) 
        if int(current_sum) > previous_sum:
            positive+=1
        previous_sum = current_sum
    f.close()
    print(positive)
