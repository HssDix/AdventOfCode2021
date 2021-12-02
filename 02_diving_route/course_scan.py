
# %% read input
from typing import ForwardRef


with open('course_input.txt', 'r') as f:
    course = f.readlines()

# %% Part One
get_num = lambda nav_string: [int(s) for s in nav_string.split() if s.isdigit()][0]

def navigate(course, depth, pos):
    for nav_string in course:

        num = get_num(nav_string)
        
        if 'up' in nav_string:
            depth -= num
        elif 'down' in nav_string:
            depth += num
        elif 'forward' in nav_string:
            pos += num
        else:
            pass

    return depth, pos

depth, pos = navigate(course, 0, 0)
product = depth*pos

print(f'The depth is: {depth}\nHorizontal position is: {pos}\nThe product is: {product}')
# %% Part Two

def navigate_by_manual(course, aim, depth, pos):
    for nav_string in course:
        
        num = get_num(nav_string)
        
        if 'up' in nav_string:
            aim -= num
        elif 'down' in nav_string:
            aim += num
        elif 'forward' in nav_string:
            pos += num
            depth += num*aim
        else:
            pass
        
    return depth, pos

depth, pos = navigate_by_manual(course, 0, 0, 0)
product = depth*pos

print(f'The depth by manual is: {depth}\nHorizontal position by manual is: {pos}\nThe product by manual is: {product}')
# %%
