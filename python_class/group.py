from itertools import groupby, tee
import csv
#
# f = csv.reader(open("Memti_Info_ADV_BS.txt", "r"), dialect="excel-tab")
# of1 = csv.writer(open("demo.txt", "w"), dialect="excel-tab")
# # of2 = csv.writer(open("results2.txt", "w"), dialect="excel-tab")
#
# for k,g in groupby(f, lambda key=x:x[0]) :
#    # passed=0
#     g, g2 = tee(g)
#     for line in g :
#          print(line)
#          print(key)
    #     if(float(line[2]) >= 30 and abs(int(line[13])-int(line[9])+int(line[8])+1) < 10) :
    #         passed += 1
    #         break
    #
    # if(passed>0) :
    #     for line in g2 :
    #         of1.writerow(line)
    # else :
    #     for line in g2 :
    #         of2.writerow(line)

from itertools import groupby

things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "speed boat"), ("vehicle", "school bus")]

for key, group in groupby(things, lambda x: x[0]):
    for thing in group:
        print ("A %s is a %s." % (thing[1], key))
    print (" ")