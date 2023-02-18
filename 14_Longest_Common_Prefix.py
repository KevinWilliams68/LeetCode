def longestCommonPrefix(strs):
    new_str = ""
    res = list(zip(*strs))
    for i in range(len(res)):
        if (res[i].count(res[i][0])) == len(strs):
            new_str += res[i][0]
        else:
            break
    return new_str