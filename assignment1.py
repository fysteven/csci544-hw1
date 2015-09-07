__author__ = 'Frank'

import sys

def main():
    #p = "people love to drink coffee"
    #words = p.split()
    #count = len(words)
    #print("The total word count is:", count)
    #lambada function has not been added to this program yet
    
    print("The name of this script file is: ", sys.argv[0])

    if len(sys.argv) == 3:
        print("The input path in the first argument is: ", sys.argv[1])
        print("The output path in the second argument is: ", sys.argv[2])

        file = open(sys.argv[1], "r")
        count_for_all_the_lines = ""
        for line in file:
            words = line.split()
            count = len(words)
            print("The word count of this line is:", count)
            this_line = str(count) + '\n'
            count_for_all_the_lines += this_line

        print(count_for_all_the_lines)

        file_to_write = open(sys.argv[2], "w")
        file_to_write.write(count_for_all_the_lines)


main()
