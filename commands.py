def commands(binary_str):
    cmds = []

    i = len(binary_str) - 1
    while i >= 0:
        if (binary_str[i] == '1') and (i == (len(binary_str) - 1)):
            cmds.append("wink")
        elif ((binary_str[i] == '1') and (i == (len(binary_str) - 2))):
            cmds.append("double blink")
        elif ((binary_str[i] == '1') and (i == (len(binary_str) - 3))):
            cmds.append("close your eyes")
        elif ((binary_str[i] == '1') and (i == (len(binary_str) - 4))):
            cmds.append("jump")

        i -= 1

    if binary_str[0] == '1':
        cmds.reverse()

    return cmds


print(commands("10011"))