DIGITS = '०१२३४५६७८९'


def eng_to_mar(num):
    eng_num = str(num)
    mar_num = ''

    i = 0
    while i < len(eng_num):
        char = int(eng_num[i])
        mar_num += DIGITS[char]
        i += 1

    return mar_num
