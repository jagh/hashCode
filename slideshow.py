import sys
import itertools
import collections
from collections import OrderedDict

DataSildes = collections.namedtuple('DataSildes', 'cardinality size tags id_photo')

class SlideShow:
    def __init__(self, datasildes):
        self.slideshow = list()
        self.dataslides = datasildes
        self.slideshow_to_file = []

    def validation(self):
        vertical_Photos = OrderedDict()

        ## Gruped node as FIFO order
        join_v_photo = []
        count = 0

        for photo in self.dataslides:
            if photo.cardinality == 'V':
                join_v_photo.append(photo.id_photo)

                if len(join_v_photo) == 2:
                    self.slideshow_to_file.append((join_v_photo[0], join_v_photo[1]))
                    count += 1
                else:
                    count += 1

            elif photo.cardinality == 'H':
                self.slideshow_to_file.append(photo.id_photo)
                count += 1
            # print(photo)
        return self.slideshow_to_file


# def output_file()/

def read_file(file_path):
    items_corpus = []
    f = open(file_path, 'r')
    f.readline()
    id_count = 0
    for line in f:
        content = line.split(' ')
        # DataSplit(name='cardinality', inputs=X_train, targets=y_train)
        # DataSildes
        tags = []
        count = 0
        # print content
        for i in content:
            if count == 0:
                card=i
                count += 1
                # DataSildes(cardinality=i)
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



def main():
    file_name='a_example' #'b_lovely_landscapes' #'a_example'   #'b_small'   #   #'c_medium'
    dataSildes = read_file('dataset/'+file_name+'.txt')
    ss = SlideShow(dataSildes)
    slideshow_to_file =ss.validation()
    print(slideshow_to_file)


if __name__ == "__main__":
    main()
