def read_input_day2():
    ret = []
    with open("../input/in_day2.txt") as f:
        raw_input = f.read()
        # windows handling
        raw_input = raw_input.replace('\r','')
        ret = [line.split(' ') for line in raw_input.split('\n')]
    return ret

def compute_score(line, score_mapping):
    return score_mapping[line[1]][0] + score_mapping[line[1]][1][line[0]]

# both tasks: A = rock (1p), B = paper(2p), C = scissors(3p)

# X = rock, Y = paper, Z = scissors
mapping_part1 = {'X':[1, {'A':3, 'B':0, 'C':6}],
             'Y':[2,{'A':6, 'B':3, 'C':0}],
             'Z':[3,{'A':0, 'B':6, 'C':3}]}

# X = loss, Y = draw, Z = win
mapping_part2 = {'X':[0, {'A':3, 'B':1, 'C':2}],
             'Y':[3,{'A':1, 'B':2, 'C':3}],
             'Z':[6,{'A':2, 'B':3, 'C':1}]}
    
def compute_overall_score(matches, task_part):
    overall_score = 0
    if task_part == 1:
        for match in matches:
            overall_score += compute_score(match, mapping_part1)
    if task_part == 2:
        for match in matches:
            overall_score += compute_score(match, mapping_part2)
    return overall_score

input_data = read_input_day2()
for i in range(1,3):
    print(compute_overall_score(input_data, i))