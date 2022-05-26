medida = float(input('Uma distancia em metros: '))
mm = medida * 1000
cm = medida * 100
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('a media de {} M coresponde a \n{} Km \n{} Hm \n{} Dam \n{:.0f} Dm \n{:.0f} Cm \n{:.0f} Mm'.format(medida, km, hm, dam, dm, cm, mm))