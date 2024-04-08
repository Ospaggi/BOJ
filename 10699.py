import time
talmo=time.time()
seoul=talmo + 9*3600
seoulF=time.gmtime(seoul)
print("%d-%s-%s" % (seoulF[0],'{:02}'.format(seoulF[1]),'{:02}'.format(seoulF[2])))
