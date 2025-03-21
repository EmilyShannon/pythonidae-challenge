from multipledispatch import dispatch
from utils import string_utils

# Challenge 0
def convert_string_to_num_bytes(S : str) -> int:
    S_bytes = S.encode('utf-8')
    return len(S_bytes)

# Challenge 1
def concatenate_string_to_each_element(U : str, E : list) -> list:
    return [U + s for s in E]

# Challenge 2
@dispatch(str, int, int)
def conceal_substring(D : str, S : int, E : int) -> str: 
    # In the given example they seemingly only count non-space indices and start from 1
    s_index = string_utils.compute_index_after_spaces(D, S)
    e_index = string_utils.compute_index_after_spaces(D, E)
    return D[ : s_index - 1] + 'x'*(E-S + 1) + D[e_index:]

@dispatch(bytes, int, int)
def conceal_substring(D : bytes, S : int, E : int) -> str:
    # TODO implement challenge 2 for bytes
    pass

    
