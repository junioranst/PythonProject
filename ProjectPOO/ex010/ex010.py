msg = 'canal = '
a = 8
for cn in range(0,11):
    if cn == a:
        msg += f'\033[31m{cn}\033[m '
    else:
        msg += f'{cn} '

print(msg)
