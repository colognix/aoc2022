def read_input():
    with open('../input/in_day4.txt','r') as f:
        return [l.strip() for l in f.readlines()]
    
in_data = read_input()


cleaner_pairs = [[set(range(int(vals1.split('-')[0]),int(vals1.split('-')[1])+1)),
  set(range(int(vals2.split('-')[0]),int(vals2.split('-')[1])+1))]
 for [vals1,vals2] in [l.split(',') for l in in_data]]

# part 1
is_contained = [not (len(pair[0].intersection(pair[1])) < min(len(pair[0]),len(pair[1]))) for pair in cleaner_pairs]
print(sum(is_contained))

# part 2
overlaps = [len(pair[0].intersection(pair[1])) > 0 for pair in cleaner_pairs]
print(sum(overlaps))