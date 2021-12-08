import sys
import math
check_argv = len(sys.argv)
default = 'test'
input = sys.argv[1] if check_argv>1 else default
file_name = f'{input}.txt'

### part 1
# with open(file_name) as f:
#     data = [ int(item) for item in f.read().split(',')]
#     f.close()


# ## part 2
with open(file_name) as f:
    data = [ int(item) for item in f.read().split(',')]
    f.close()

