def encode(text):
    s = text.split()
    ans = ''

    for i in s:
        if i[0].isalpha() and len(i[0]) > 0:
            ans = ans + i[1:] + i[0] + 'оп' + ' '
        else:
            ans = ans + i[0] + ' '

    return ans.strip(' ')
