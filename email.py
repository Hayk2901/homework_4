emails = input().split('"')
normalEmails = []
n = len(emails)
s = []
# print(emails)


def mail(k):
    j = 0
    e1 = []
    pl = True
    # print(emails[k])
    ln = len(emails[k])
    for j in range(ln):
        if emails[k][j] == '+':
            pl = False
        if emails[k][j] == '@':
            break
        if pl and emails[k][j] != '.':
            e1.append(emails[k][j])
    # print(''.join(e1)+emails[k][j:])
    return ''.join(e1)+emails[k][j:]


for i in range(1, n - 1, 2):
    ss = mail(i)
    if ss in s:
        continue
    else:
        s.append(ss)
print(len(s))
