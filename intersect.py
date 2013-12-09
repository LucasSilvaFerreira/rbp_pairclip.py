__author__ = 'Lucas'
import re

def search_mark(arquivo_bed,arquivo_querys):

    '''arquivo_bed=bed format file
     arquivo_querys= vetor com querys'''
    file_meia_vida=open(arquivo_querys,'r')



        #else:
        #    print 'teste


    file=open(arquivo_bed,'r')
    for linha in file:
        if len(linha)>0:
            #print linha
            chr=linha.split('\t')[0]
            start=linha.split('\t')[1]
            end=linha.split('\t')[2]
            for linha_meia in file_meia_vida:
                if len(linha_meia)>0:
                    if not re.match('#',linha_meia):
                        valores=linha_meia.split('\t')
                        cordenadas=re.split(':|-',valores[57])
                        #print cordenadas
                        if (chr == cordenadas[0]):

                            if int(start) > int(cordenadas[1]):
                                #print end
                                if int(end) < int(cordenadas[2]):
                                    print 'aa'
                                    print valores
                                    print start
                        #chr_rna=valores[]
                        #if
                        #break
search_mark('starBase2_NAR2014_HHLE1.bed.txt','AS_enriched+exclusivo_nucleo_meia-vida.txt')