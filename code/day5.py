def read_input():
    with open('../input/in_day5.txt','r') as f:
        return [l.strip() for l in f.readlines()]
    
data = read_input()
instr = []
for line in data:
    if line.startswith('m'):
        arr = line.split(' ')
        instr += [[int(arr[1]),int(arr[3]),int(arr[5])]]

# part 1
stacks = [['C','Z','N','B','M','W','Q','V'],['H','Z','R','W','C','B'],['F','Q','R','J'],
         ['Z','S','W','H','F','N','M','T'],['G','F','W','L','N','Q','P'],['L','P','W'],
          ['V','B','D','R','G','C','Q','J'],['Z','Q','N','B','W'],['H','L','F','C','G','T','J']]
for step in instr:
    for i in range(step[0]):
        stacks[step[2]-1] += stacks[step[1]-1].pop()

res = ""
for stack in stacks:
    res += stack[-1]
print(res)

# part 2
stacks = [['C','Z','N','B','M','W','Q','V'],['H','Z','R','W','C','B'],['F','Q','R','J'],
         ['Z','S','W','H','F','N','M','T'],['G','F','W','L','N','Q','P'],['L','P','W'],
          ['V','B','D','R','G','C','Q','J'],['Z','Q','N','B','W'],['H','L','F','C','G','T','J']]
for step in instr:
    tmp = []
    for i in range(step[0]): 
        tmp += stacks[step[1]-1].pop()
    stacks[step[2]-1] += reversed(tmp)
res = ""
for stack in stacks:
    res += stack[-1]
print(res)
