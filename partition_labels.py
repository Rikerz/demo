# https://leetcode.com/problems/partition-labels/


def get_partition_labels(s):
    # If we are missing the parameter, there is nothing to return.
    if not s:
        return []

    s_len = len(s)
    s_reverse = s[::-1]

    def find_end_index(start_index):
        start_char = s[start_index]
        # Find the last occurrence of the character.
        end_index = -(s_reverse.index(start_char) - s_len)
        # Check if any of the characters in between exist in what is left.
        remaining = s[end_index:]
        for i in range(start_index + 1, end_index):
            char = s[i]
            if char in remaining:
                # The partition is not valid, expand it further to contain
                # all occurrences of this character.
                return find_end_index(i)

        # The partition is valid.
        return end_index

    result = []
    start_index = 0
    end_index = 0
    while end_index < s_len:
        end_index = find_end_index(start_index)
        result.append(end_index - start_index)
        start_index = end_index

    return result
