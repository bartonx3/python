# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 18:42:07 2022

@author: Bartosz
"""

def pole(a,b):
    return a*b
def raport (funkcja,a,b):
    print(f"Pole wynosi: {funkcja(a, b)}")
    
raport(pole, 4, 5)