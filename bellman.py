import numpy as np
from sympy import *

def f(u, x, t):
    return 0

def diffs(d): #частная производная
    x = Symbol('x')
    psi = Symbol('psi')
    u = Symbol('u')
    dic = {
        'H_u': diff(H, u),
        'H_x': diff(H, x)}
    return(dic[d])

def solvingu(expr): #выражаем u
    x = Symbol('x')
    psi = Symbol('psi')
    u = Symbol('u')
    return solve(expr, u)

def solvingdsdx(expr): #выражаем dsdx
    dsdx = Symbol('dsdx')
    dsdt = Symbol('dsdt')
    return solve(expr, dsdx)
    

dxdt = 'u'
dsdt = 'dsdt'
dsdx = 'dsdx'
u = 'u'

urav = 'max{dsdt + dsdx * u - 0.5*u**2} = 0' #воспользуемся уравнением Беллмана через максимум
H = f"{dsdt} + {dsdx}*{u} - 0.5*{u}^2" #максимизируемое выражение
print(H)
dHdu = diffs('H_u') #берём частную производную по u, тем самым выявляя максимум
print(f"{dHdu} = 0")
u_found = solvingu(dHdu)[0] #выражаем u
print(f"u* = {u_found}")
newH = str(H)
newH = H.replace('u', str(u_found)) #подставляем u в выражение
print(f"{newH} = 0")
pre_DU = solvingdsdx(newH) #подобные члены не очень получается привести, попробовала выразить одно через другое
print(pre_DU)
