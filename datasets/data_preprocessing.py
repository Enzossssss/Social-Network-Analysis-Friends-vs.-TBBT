def process_data(initial_path, end_path):
    '''
    create a new file of the type "X1 X2" in a file of type "X1 X2 N" where N is the number of "X1 X2" or "X2 X1" lines 
    
    Parameters
    ----------
    initial_path : absolute path of the file that you want to modify
    end_path : absolute path where you want to save the new file (including the name of the new file)
    '''

    current_dict = {}

    with open(initial_path) as f:
        for line in f:
            l = line.split()
            if len(l) == 2 and l[0][0] != '#':
                s1 = str(l[0] + ' ' + l[1])
                s2 = str(l[1] + ' ' + l[0])
                if (not (s1 in current_dict.keys())) or (not (s2 in current_dict.keys())):
                    current_dict[s1] = 1
                else:
                    current_dict[s1] += 1
            if 'str' in line:
                break

    with open(end_path, 'w') as f:
        for line in current_dict.keys():
            f.write(str(line) + ' ' + str(current_dict[line]))
            f.write('\n')

def main():
    process_data("C:\\Users\\vince\\OneDrive\\Desktop\\Work in progress\\Social Network Analysis\\SNA Project\\datasets\\native datasets\\bbt22.txt", "C:\\Users\\vince\\OneDrive\\Desktop\\Work in progress\\Social Network Analysis\\SNA Project\\datasets\\processed datasets\\tbbt_processed.txt")
    process_data("C:\\Users\\vince\\OneDrive\\Desktop\\Work in progress\\Social Network Analysis\\SNA Project\\datasets\\native datasets\\friends_episodes.txt", "C:\\Users\\vince\\OneDrive\\Desktop\\Work in progress\\Social Network Analysis\\SNA Project\\datasets\\processed datasets\\friends_processed.txt")

if __name__ == "__main__":
    main()