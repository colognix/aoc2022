def read_input():
    with open('../input/in_day7.txt','r') as f:
        return [l.strip() for l in f.readlines()]
    
    
def compute_size(directory, dir_dict):
    # currently processed directory
    tmp = dir_dict[directory]
    size = tmp[0]
    # compute size of nested directories recursively
    if tmp[1]:
        for nested_dir in tmp[1]:
            size += compute_size(nested_dir, dir_dict)
    return size
    
log = read_input()

# dictionary to store directory information
dirs = {}
# ctrl-variable to check if currently a directory is scanned (after ls)
in_dirscan = False
# ctrl-variable to check if a scan finished recently (to update directory information)
was_in_dirscan = False
# list containing path elements of current position
position = []

# temporary variables for current directory scanned: nested directories and size of present files
curdirs = []
cursize = 0

for line in log:
    # check if scanning directory or using commands
    if line.startswith('$'):
        # currently not scanning directory
        in_dirscan = False
        if was_in_dirscan:
            # process size information for previous directory scanned
            dirs[curpath] = [cursize,curdirs]
            was_in_dirscan = False
    else:
        in_dirscan = True
    split_line =  line.split(' ')
    
    # command-section
    if not in_dirscan:
        cmd = split_line[1]
        # case cd
        if cmd == 'cd':
            # keep track of position. Current directory is in position[-1]
            if split_line[2] == '/':
                position = ['/']
            elif split_line[2] == '..':
                position.pop()
            else:
                position += [split_line[2]]
        # case ls
        if cmd == 'ls':
            # handling in dirscan, nothing to do here
            pass
    # scanning section
    if in_dirscan:
        if not was_in_dirscan:
            # reset directory information (path/size/nested dirs)
            was_in_dirscan = True
            curpath = '/'
            for p in position[1:]:
                curpath += p + '/'
            curdirs = []
            cursize = 0

        # scan directory line by line and update size or contained directories
        if split_line[0] == 'dir':
            curdirs += [curpath+split_line[1]+'/']
        else:
            cursize += int(split_line[0])
            
# process size information for final directory
if was_in_dirscan:
    dirs[curpath] = [cursize,curdirs]

# use list for list comparison
dirs_total_size = []

# compute the total sizes of each directory
for directory in dirs.keys():
    dirs_total_size += [[directory,compute_size(directory, dirs)]]
    
# part 1
print(sum([d[1] for d in dirs_total_size if d[1]< 100000]))
# part 2
unused_space = 70000000 - dirs_total_size[0][1]
needed_space = 30000000 - unused_space
print(min([d[1] for d in dirs_total_size if d[1] > needed_space]))

