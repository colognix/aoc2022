import string

def read_input_day3():
    ret = []
    with open("../input/in_day3.txt") as f:
        raw_input = f.read()
        # windows handling
        raw_input = raw_input.replace('\r','')
        return raw_input.split('\n')
    
sacks = read_input_day3()

priority = {}
i = 1
for lit in string.ascii_lowercase:
    priority[lit] = i
    i += 1
for lit in string.ascii_uppercase:
    priority[lit] = i
    i += 1
    
# part 1
res = 0
for sack in sacks:
    comp1, comp2 = sack[:int(len(sack)/2)],sack[int(len(sack)/2):]
    res += priority[set(comp1).intersection(set(comp2)).pop()]
print(res)

# part 2
res = 0
team_sacks = [sacks[i:i+3] for i in range(0,len(sacks),3)]
for sacks in team_sacks:
    res += priority[set(sacks[0]).intersection(set(sacks[1])).intersection(set(sacks[2])).pop()]
print(res)