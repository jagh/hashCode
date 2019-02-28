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

class Photo:
    def __init__(self, orientation, nb, tags):
        self.orientation = orientation
        self.nb = nb
        self.tags = tags

    def getOrientation(self):
        return self.orientation

    def getTags(self):
        return self.tags

    def toStr(self):
        return self.tags


class Slide:
    def __init__(self, photo):
        self.photo = photo
        self.tags = photo.getTags()

    def getTags(self):
        return self.tags

    def intersection(self, toCompare):
        return list(set(toCompare.getTags()) & set(self.tags))

    def difference(self, toCompare):
        return list(set(toCompare.getTags()) - set(self.tags))

    def score(self, toCompare):
        score1 = len(self.intersection(toCompare))
        score2 = len(self.difference(toCompare))
        score3 = len(toCompare.difference(self))
        return min(score1, score2, score3)


class SlideShow:
    def __init__(self):
        self.slideshow = list()

    def addSlide(self, slide):
        self.slideshow.append(slide)

    def evaluate(self):
        total_score = 0
        for i in range(len(self.slideshow)-1):
            slide1 = self.slideshow[i]
            slide2 = self.slideshow[i+1]
            #slide1.intersection(slide2)
            #slide1.diff(slide2)
            #slide2.diff(slide1)
            total_score += slide1.score(slide2)
        return total_score


def read_file(file_path):
    items_corpus = []
    f = open(file_path, 'r')
    f.readline()
    for line in f:
        line = line.rstrip('\n')
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
            elif count == 1:
                size=i
                count += 1
            else:
                tags.append(i)
                count += 1
        items_corpus.append(DataSildes(cardinality=card, size=size, tags=tags))
    f.close()
    return items_corpus



def main():
    photolist = list()
    slidelist = list()
    slideshow = SlideShow()
    file_name= 'b_lovely_landscapes' #''a_example'   #'b_small'   #   #'c_medium'
    dataSildes = read_file('dataset/'+file_name+'.txt')

    for el in dataSildes:
        photolist.append(Photo(el.cardinality, el.size, el.tags))

    for photo in photolist:
        #if photo.getOrientation() == 'H':
        slidelist.append(Slide(photo))

    for slide in slidelist:
        slideshow.addSlide(slide)

    print "score " + str(slideshow.evaluate())



if __name__ == "__main__":
    main()
