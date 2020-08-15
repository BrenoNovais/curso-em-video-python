m = float(input('Digite quantos metros'))
km = m*0.001
hm = m*0.01
dam = m*0.1
dm = m*0.1
c = m*100
mm = m*1000
print('{} m são \n{}km \n{}hm \n{:.2f}dam \n{:.2f}dm \n{:.0f}c \n{:.0f}mm ' .format(m, km, hm, dam, dm, c, mm))
