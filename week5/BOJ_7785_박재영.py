import collections

N = int(input())
enter = []
leave = []

for _ in range(N) :
    log = input()
    emply = log.split()[0]
    state = log.split()[1]

    if state == 'enter':
        enter.append(emply)
    else:
        leave.append(emply)

result = collections.Counter(enter) - collections.Counter(leave)
key_list = sorted(list(result.keys()), reverse=True)

for i in key_list:
    print(i)