
# with open('input.txt') as f:
#     data = f.read().splitlines()
#     h_p = 0
#     dep_p = 0
#     for line in data:
#         split = line.split(' ')
#         if split[0] == 'forward':
#             h_p+=int(split[1])
#         elif split[0] == 'down':
#             dep_p+=int(split[1])
#         else:
#             dep_p-=int(split[1])
#     print(h_p*dep_p)
#     f.close()

with open('input.txt') as f:
    data = f.read().splitlines()
    h_p = 0
    dep_p = 0
    aim=0
    for line in data:
        split = line.split(' ')
        if split[0] == 'forward':
            h_p+=int(split[1])
            dep_p+=(aim * int(split[1]))
        elif split[0] == 'down':
            aim+=int(split[1])
        else:
            aim-=int(split[1])
    print(h_p*dep_p)
    f.close()
