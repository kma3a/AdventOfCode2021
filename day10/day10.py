import sys
import math
check_argv = len(sys.argv)
default = 'test'
input = sys.argv[1] if check_argv>1 else default
file_name = f'{input}.txt'

count = {
    ')':0,
    ']':0,
    '}':0,
    '>':0,
}

## part 1 points
# points = {
#     ')':3,
#     ']':57,
#     '}':1197,
#     '>':25137,
# }

def check_legal(line):
    finished = line
    con = False
    while not con:
        has_removed = False
        line_count =  len(finished)
        for key in ['()','[]','{}','<>']:
            finished = finished.replace(key, '')
            if len(finished) == 0:
                con = True
                break
            elif len(finished) < line_count:
                line_count = len(finished)
                has_removed = True
        if not has_removed:
            con = True
    return finished
    


# print(check_legal('([])') == '' )
# print(check_legal('{()()()}') == '' )
# print(check_legal('<([{}])>') == '' )
# print(check_legal('[<>({}){}[([])<>]]') == '' )
# print(check_legal('(((((((((())))))))))') == '' )
# print(check_legal('(((((((((())>)))))))') == '((((((((>)))))))' )

def get_illegal_character(line):
    ends = [']','>',')','}']
    illegal = ''
    for char in line:
        if char in ends:
            illegal=char
            break
    return illegal


# test = '{([(<{}[<>[]}>{[]{[(<()>'
# test_illegal = check_legal(test)
# illegal_mark = get_illegal_character(test_illegal) 
# print(illegal_mark == '}')

# test = '[[<[([]))<([[{}[[()]]]'
# test_illegal = check_legal(test)
# illegal_mark = get_illegal_character(test_illegal) 
# print(illegal_mark == ')')

# test = '[{[{({}]{}}([{[{{{}}([]'
# test_illegal = check_legal(test)
# illegal_mark = get_illegal_character(test_illegal) 
# print(illegal_mark == ']')

### part 1
# with open(file_name) as f:
#     data = f.read().splitlines()
#     for line in data:
#         get_legal = check_legal(line)
#         if len(get_legal) > 0:
#             illegal_mark = get_illegal_character(get_legal)
#             if illegal_mark == '':
#                 continue
#             value = count[illegal_mark] 
#             count[illegal_mark] = value+1
#     score = 0
#     for key in points.keys():
#         score+= points[key] * count[key]
#     print(score)

#     f.close()


## part 1 points
points = {
    '(':1,
    '[':2,
    '{':3,
    '<':4,
}

def count_marks(line):
    score = 0
    for mark in line[::-1]:
        score = (score *5) + points[mark]
    return score

# test = '<{([{{}}[<[[[<>{}]]]>[]]'
# illegal = check_legal(test)
# test_score = count_marks(illegal)
# print(test_score == 294)


# ## part 2
with open(file_name) as f:
    scores = []
    data = f.read().splitlines()
    for line in data:
        get_legal = check_legal(line)
        if len(get_legal) > 0:
            illegal_mark = get_illegal_character(get_legal)
            if illegal_mark == '':
                scores.append(count_marks(get_legal))
    scores.sort()
    print(scores[math.floor(len(scores)/2)])


    # score = 0
    # for key in points.keys():
    #     score+= points[key] * count[key]
    # print(score)

#     f.close())

