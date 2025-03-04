class StringChallengeSolution:
    # Challenge 0
    def convert_string_to_num_bytes(self, S : str) -> int:
        S_bytes = S.encode('utf-8')
        return len(S_bytes)

    # Challenge 1
    def concatenate_string_to_each_element(self, U : str, E : list) -> list:
        return [U + s for s in E]
