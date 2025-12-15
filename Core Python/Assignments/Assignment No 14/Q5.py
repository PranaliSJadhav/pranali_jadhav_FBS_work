def longest_common_prefix(strings):
    prefix = ""
    shortest = min(strings, key=len)

    for i in range(len(shortest)):
        chars = {s[i] for s in strings}
        if len(chars) == 1:
            prefix += chars.pop()
        else:
            break
    return prefix

strings = ["flower", "flow", "flight"]
print(longest_common_prefix(strings))
