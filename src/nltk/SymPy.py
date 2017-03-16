# -*- coding: utf-8 -*-

from sympy import Symbol,pprint,init_printing
init_printing(order='rev-lex')

x=Symbol('x')

series=x
for i in range(2,11):
    series=series+(x**i)/i
        
pprint(series)       
            