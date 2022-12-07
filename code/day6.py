def read_input():
    with open('../input/in_day6.txt','r') as f:
        return f.read()
stream = read_input()
# part 1
for i in range(4,len(stream)):
    if len(set(stream[i-4:i])) == len(stream[i-4:i]):
        print(i)
        break;
# part 2
for i in range(14,len(stream)):
    if len(set(stream[i-14:i])) == len(stream[i-14:i]):
        print(i)
        break;