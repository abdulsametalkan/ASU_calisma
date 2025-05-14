# -*- coding: utf-8 -*-
"""
Created on Thu May  8 14:51:59 2025
 ödev:
     bu soruyu while ile çöz
@author: abdul
"""




N1 = int(input("Bir sayı giriniz:"))
fonk=0
sayac2 = 2
while sayac2 <= N1:
    fonk +=  sayac2*(sayac2-1)
    print(f"{sayac2}x{sayac2-1}", end = '')
    if sayac2!=N1: 
        print(" + ", end = '')
    else: 
        print(" = ", end = '')
        
    sayac2+=1 

print(fonk)

