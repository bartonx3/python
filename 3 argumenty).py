# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 19:03:27 2022

@author: Bartosz
"""
# jesli podamy 1 argument funkcja liczy pole kwadratu, 2 liczy pole prostokąta,
# 3 liczy objetosc
def Pole(bok1=None,bok2=None,bok3=None):
    if bok2 is None and bok3 is None:
        return bok1*bok1
    elif bok3 is None:
        return bok1*bok2
    else:
        return bok1*bok2*bok3

    
print(Pole(2,6,4))
    