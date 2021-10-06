'''
fails=open("lapa.txt", 'w', encoding='utf-8')

linija1 = "Rozes ir sarkanas.\n"
linija2 = "Rudens ir klāt\n"
linija3 = "Python ir jauks\n"
linija4 = "Vai tu esi jautrs?\n"

fails.write(linija1+linija2+linija3+linija4)
fails.close()
'''


'''
fails=open('astite.txt', 'a', encoding='utf-8')
for i in range(10):
    fails.write("Pievieno rindu %d\r\n" % (i+1))
'''
'''
#fails=open('astites.txt', 'x', encoding='utf-8')
#fails.write('Šodiena drīz beigsies')
'''
'''
#fails=open('astite.txt', 'w', encoding='utf-8')
#fails.write('Šodiena drīz beigsies')
'''
'''
#fails=open('astite.txt', 'a', encoding='utf-8')
#fails.write('Šodiena drīz beigsies')
'''


'''
#fails=open('aste.txt', 'a', encoding='utf-8')
#print(fails.read())
fails.close()
'''