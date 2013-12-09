__author__ = 'lucas'
from os import listdir
from intersect import search_mark
vetor_beds=listdir("bed_files")

for bed in vetor_beds:
    print 'bed_files/'+bed
    search_mark('bed_files/'+bed,'half_life_AS_maior 3h.txt')
