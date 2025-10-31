#a=int (input( "Juft son kiriting:"))
#if a%2==0:
 #   print('Rahmat!')
#else:
    #print(f'{a} juft emas')
    
#yosh=int(input('Yoshingizni kiriiting\n'))
#if yosh<4  or yosh>60:
  #  print ('Bepul!')
#elif yosh<18:
  #else:
   # print('20.000 so/tm ')
    
#mahsulotlar=['nok','olma','anor','banan','kivi']
#savat=[]
#print(f' Do\'konizmizda {mahsulotlar} bor')
#for i in range (5):
 # a=input(f'{i+1} - mahsulotni kiriting\n').lower()
 # savat.append(a)
 # print('Sizning savatingiz', savat)
#for meva in savat :
    #if meva in mahsulotlar:
     #   print(f'Bizda {meva} bor')
   # else:
   #     print(f'{meva}- do\'konimizda yo\'q')
    
foydalanuvchilar=['shodiyona','oyparcha', 'diyora', 'oktamxon' ]
a=str(input('Yangi login tanglang!\n'))
if a.lower() in foydalanuvchilar:
    print(f'{a}- bu nomdagi foydalanuvchi bor')
else:
    print('Yangi login sozlandi')
    