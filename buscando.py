__author__ = 'lucas'
from os import listdir
from intersect import search_mark
from threading import Thread
class Th(Thread):
    def __init__ (self,num,bed_file,genes_file):
        Thread.__init__(self)
        self.num =num
        self.bed_file=bed_file
        self.genes_file=genes_file
    def run(self):
        print "thread iniciada "
        print self.num
        search_mark(self.bed_file,self.genes_file)





vetor_beds=listdir("bed_files")
count_thread=1
threads_vector=[]
for bed in vetor_beds:
    print 'bed_files/'+bed
    threads_vector.append( Th(count_thread,'bed_files/'+bed,'half_life_AS_menor 3h.txt'))
    print len(threads_vector)
    threads_vector[len(threads_vector)-1].start()
    count_thread+=1
