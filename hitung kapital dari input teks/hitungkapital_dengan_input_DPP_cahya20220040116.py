print('Program Menghitung Kemunculan Huruf Besar')
print('******************************************')

kata = input('masukkan kata = ')

huruf_besar = 0
for kar in kata :
    if kar.isupper():
        huruf_besar = huruf_besar + 1
print('Banyaknya kemnculan huruf besar  = ', huruf_besar)
