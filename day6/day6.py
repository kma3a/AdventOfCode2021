import sys
import re
check_argv = len(sys.argv)-1
default = 'test'
input = sys.argv[1] if check_argv==1 else default
file_name = f'{input}.txt'


### part 1
with open(file_name) as f:
    f.close()


# ## part 2
# with open(file_name) as f:
#     f.close()

