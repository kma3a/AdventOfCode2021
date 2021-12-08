import sys
import math
check_argv = len(sys.argv)
default = 'test'
input = sys.argv[1] if check_argv>1 else default
file_name = f'{input}.txt'

# def count_row(string):
#     unique_length = [2,3,4,7]
#     split_str = string.split(' | ')
#     four_dig_out = split_str[1].split(' ')
#     count = 0
#     for num in four_dig_out:
#         if len(num) in unique_length:
#             count+=1
#     return count



# print(count_row('be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe') == 2)
# print(count_row('fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb') == 4)
# print(count_row('edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc') == 3)
### part 1
# with open(file_name) as f:
#     data = f.read().splitlines()
#     count = 0
#     for row in data:
#         count += count_row(row)
#     print(count)
#     f.close()


# def decode_unique(string):
#     str_len= str(len(string))
#     num_len = {
#         '2':1,
#         '3':7,
#         '4':6,
#         '7':8
#     }
#     if str_len in num_len.keys():
#         return num_len[str_len] 
#     else:
#         return -1


# print(decode_unique('acedgfb')==8)
# print(decode_unique('ab')==1)
# print(decode_unique('dab')==7)
# print(decode_unique('eafb')==4)

def get_unique(uniq_list):
    unique_length = [2,3,4,7]
    uiq_list = []
    for num in uniq_list:
        if len(num) in unique_length:
            uiq_list.append(num)
    return uiq_list 

# print(get_unique(['be','cfbegad','cbdgef','fgaecd','cgeb','fdcge','agebfd','fecdb','fabcd','edb'])==['be','cfbegad', 'cgeb','edb'])


def decode_row(string):
    ten_patterns= string.split(' ')
    uniqu_match={
        '2':'1',
        '3':'7',
        '4':'4',
        '7':'8'

    }
    nums_combos = {}
    unique_nums = get_unique(ten_patterns)
    non_unique_nums = list(set(ten_patterns) - set(unique_nums))
    for num in unique_nums:
        nums_combos[uniqu_match[str(len(num))]] = num
    for num in non_unique_nums:
        if len(num) == 5:
            if len(list(set(num) - set(nums_combos['4']))) == 2:
               if len(list(set(num) - set(nums_combos['1']))) == 3:
                 nums_combos['3'] = num
               else:
                 nums_combos['5'] = num 
            else:
                nums_combos['2'] = num 
        else:
           if len(list(set(num) - set(nums_combos['1']))) == 4:
               if len(list(set(num) - set(nums_combos['4'])- set(nums_combos['7']))) == 1:
                   nums_combos['9'] = num
               else:
                   nums_combos['0'] = num
           else:
               nums_combos['6'] = num  
    return nums_combos


# print(decode_row('be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb'))

# value = decode_row('acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab')

# print(value['8'] == 'acedgfb')
# print(value['5'] == 'cdfbe')
# print(value['5'])
# print(value['2'] == 'gcdfa')
# print(value['3'] == 'fbcad')
# print(value['7'] == 'dab')
# print(value['9'] == 'cefabd')
# print(value['6'] == 'cdfgeb')
# print(value['4'] == 'eafb')
# print(value['0'] == 'cagedb')
# print(value['1'] == 'ab')

def parse_num(string, decoded):
    output= string.split(' ')
    keys = decoded.keys()
    final_num= []
    for num in output:
        for key in keys:
            if len(num) == len(decoded[key]) and (len(list(set(num) - set(decoded[key]))) == 0):
                final_num.append(key)
                break
    return int(''.join(final_num))




# print(parse_num('cdfeb fcadb cdfeb cdbaf',decode_row('acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab')) ==5353)

# ## part 2
with open(file_name) as f:
    data = f.read().splitlines()
    count = 0
    for row in data:
        split_data = row.split(' | ')
        ten_patterns=  split_data[0]
        output_val=  split_data[1]
        count += parse_num(output_val,decode_row(ten_patterns))
    print(count)
    f.close()
