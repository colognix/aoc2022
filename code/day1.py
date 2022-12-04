def read_input_day1():
    
    def process(raw):
        split_data = raw.split('\n\n')
        ret = []
        for data_set in split_data:
            try:
                ret += [[int(i) for i in data_set.split('\n')]]
            except ValueError:
                continue
        return ret
    
    with open("../input/in_day1.txt") as f:
        raw_in = f.read()
        # windows handling
        raw_in = raw_in.replace('\r','')
        return process(raw_in)
    
def compute_sum(in_data):
    sum_data = []
    for vals in in_data:
        sum_data += [sum(vals)]
    return sum_data 


# part 1
sums = compute_sum(read_input_day1())
print(max(sums), sums.index(max(sums)))

# part 2
sum_three = 0
for i in range(3):
    sum_three += max(sums)
    sums.pop(sums.index(max(sums)))
print(sum_three)