###########################################################
### Hash Code 2019                                      ###
### Pizza Practice Problem                              ###
### Team: SuicideSquad                                  ###
###########################################################


import sys
import itertools
import collections
from collections import OrderedDict

DataSildes = collections.namedtuple('DataSildes', 'cardinality size tags')

class SlideShow:
    def __init__(self):
        pass


def read_file(file_path):
    items_corpus = []
    f = open(file_path, 'r')
    for line in f:
        content = line.split(' ')
        # DataSplit(name='cardinality', inputs=X_train, targets=y_train)
        # DataSildes
        tags = []
        count = 0
        for i in content:
            if count == 0:
                card=i
                count += 1
                # DataSildes(cardinality=i)
            elif count ==1:
                size=i
                count += 1
            else:
                tags.append(i)
                count += 1

        items_corpus.append(DataSildes(cardinality=card, size=size, tags=tags))
    f.close()
    return items_corpus



def main():
    file_name='a_example'   #'b_small'   #   #'c_medium'
    dataSildes = read_file('dataset/'+file_name+'.txt')
    print(dataSildes[0].cardinality)


if __name__ == "__main__":
    main()
