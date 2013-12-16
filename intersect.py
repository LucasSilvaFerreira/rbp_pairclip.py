__author__ = 'Lucas'
import re


def search_mark(arquivo_bed, arquivo_querys):
    '''arquivo_bed=bed format file
     arquivo_querys= vetor com querys'''



    #else:
    #    print 'teste
    #print arquivo_bed.split("_")[2]
    saida = open('saida_' + arquivo_bed.split("_")[3] + "_" + arquivo_querys, 'w')
    file = open(arquivo_bed, 'r')
    encontradas = 0
    tamanho = len(file.read().split('\n'))
    file = open(arquivo_bed, 'r')

    for linha in file:
        if len(linha) > 0:
            #print linha
            chr = linha.split('\t')[0]
            start = linha.split('\t')[1]
            end = linha.split('\t')[2]
            #print chr,int(start),int(end)
            file_meia_vida = open(arquivo_querys, 'r')
            for linha_meia in file_meia_vida:
                #print 'entrou1'
                if len(linha_meia) > 0:
                    #print 'entrou2'
                    if not re.match('#', linha_meia):
                        valores = linha_meia.split('\t')
                        cordenadas = re.split(':|-', valores[12]) #12 em alguns arquivos.Arquivos de
                        #print cordenadas
                        if (chr == cordenadas[0]):
                            #print chr == cordenadas[0]

                            if int(start) > int(cordenadas[1]):
                                #print 'aa'
                                if int(end) < int(cordenadas[2]):
                                    #print "\t".join(valores)+'\n'
                                    #print start
                                    saida.write("\t".join(valores))
                                    encontradas += 1
    print  'saida',float(encontradas) / float(tamanho), "saida_" + arquivo_bed.split("_")[3] + "_" + arquivo_querys
    #chr_rna=valores[]
    #if
    #break


