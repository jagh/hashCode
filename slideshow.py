import sys, os
import itertools
import collections
from collections import OrderedDict
import numpy as np


DataSildes = collections.namedtuple('DataSildes', 'cardinality size tags id_photo')

class SlideShow:
    def __init__(self, datasildes):
        self.slideshow = list()
        self.dataslides = datasildes
        self.slideshow_to_file = []

    def validation(self):
        vertical_Photos = OrderedDict()

        ## Join vertical photo
        join_v_photo = []
        count = 0
        for photo in self.dataslides:
            if photo.cardinality == 'V':
                join_v_photo.append(photo.id_photo)

                if len(join_v_photo) == 2:
                    # print((join_v_photo[0], join_v_photo[1]))
                    slide_joined = str(join_v_photo[0])+' '+str(join_v_photo[1])
                    # self.slideshow_to_file.append((join_v_photo[0], join_v_photo[1]))
                    self.slideshow_to_file.append(slide_joined )
                    count += 1
                else:
                    count += 1

            elif photo.cardinality == 'H':
                self.slideshow_to_file.append(photo.id_photo)
                count += 1
            # print(photo)
        return self.slideshow_to_file

def read_file(file_path):
    items_corpus = []
    f = open(file_path, 'r')
    f.readline()
    id_count = 0
    for line in f:
        line = line.rstrip('\n')
        content = line.split(' ')
        tags = []
        count = 0
        for i in content:
            if count == 0:
                card=i
                count += 1
            elif count == 1:
                size=i
                count += 1
            else:
                tags.append(i)
                count += 1
        items_corpus.append(DataSildes(cardinality=card, size=size, tags=tags, id_photo=id_count))
        id_count += 1
    f.close()
    return items_corpus

def output(out, file_name):
    size = len(out)
    with open(file_name + '.out', 'w') as output_final:
        outline = []
        outline.append(str(size))
        output_final.write("".join(outline) + "\n")
        for i in range(len(out)):
            outline = []
            temp = out[i]
            # print(type(temp))
            if type(temp) == type(tuple()):
                for j in temp:
                    # print("j:"+ str(j))
                    outline.append(str(j)+" ")
            else:
                outline.append(str(temp))
            # print(outline)
            output_final.write("".join(outline) + "\n")


def main():
    file_name='a_example'   #'e_shiny_selfies'  #'b_lovely_landscapes' #'b_lovely_landscapes'
    dataSildes = read_file('dataset/'+file_name+'.txt')
    ss = SlideShow(dataSildes)
    slideshow_to_file = ss.validation()
    output(slideshow_to_file, file_name)

if __name__ == "__main__":
    main()
