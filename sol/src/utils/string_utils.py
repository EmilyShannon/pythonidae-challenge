def compute_index_after_spaces(S : str, a : int):
    new_index = 0
    num_chars = 0
    while num_chars < a:
        if S[new_index] != ' ':
            num_chars += 1
        new_index += 1 
    return new_index