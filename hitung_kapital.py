print('Program Menghitung Kemunculan Huruf Besar')
print('******************************************')


def kal(kata):
    kapital = 0
    for kar in kata:
        if kar.isupper():
            kapital = kapital + 1
    print('banyaknya huruf kapital = ',kapital)

