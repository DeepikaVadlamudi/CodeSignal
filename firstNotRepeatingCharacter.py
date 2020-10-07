def firstNotRepeatingCharacter(s):
    seen1 = []
    seen2 =[]
    for i in s:
        if i in seen1:
            if i not in seen2:
                seen2.append(i)
        else:
            seen1.append(i)

    for i in seen2:
        if i in seen1:
            seen1.remove(i)

    if not seen1:
        return '_'
    return seen1[0]
