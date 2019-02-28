###########################################################
### Hash Code 2019                                      ###
### Pizza Practice Problem                              ###
### Team: SuicideSquad                                  ###
###########################################################


import sys
import itertools
from collections import deque
from collections import OrderedDict
from sortedcontainers import SortedDict



def read_file(file_path):
    items_corpus = []
    f = open(file_path, 'r')
    for line in f:
        items_corpus.append(line)
    f.close()
    return items_corpus



def main():
    file_name='a_example'   #'b_small'   #   #'c_medium'
    items = read_file('dataset/'+file_name+'.txt')
    print(items)


if __name__ == "__main__":
    main()
