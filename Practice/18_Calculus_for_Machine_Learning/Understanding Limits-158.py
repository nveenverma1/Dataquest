## 3. Introduction to SymPy ##

import sympy
x,y = sympy.symbols('x y')

y = x^2 + 1
print(y)

#y = 3(x)

## 4. Limits Using SymPy ##

import sympy
x2,y = sympy.symbols('x2 y')

approaches = 2.9
input_v = x2
func = (-(x2**2) + 3*x2 - 1+1)/(x2-3)

limit_one = sympy.limit(func, input_v, approaches)
limit_one

## 5. Properties Of Limits I ##

x,y = sympy.symbols('x y')

approaches = 1
input_v = x
func = 3*(x**2) + 3*x - 3

limit_two = sympy.limit(func, input_v, approaches)
print(limit_two)

## 6. Properties Of Limits II ##

x,y = sympy.symbols('x y')

approaches = -1
input_v = x
func = x**3 + 2*(x**2) - 10*x

limit_three = sympy.limit(func, input_v, approaches)
limit_three

## 7. Undefined Limit To Defined Limit ##

import sympy
x2, y = sympy.symbols('x2 y')

approaches = 3
input_v = x2
func = -x2

limit_four = sympy.limit(func, input_v, approaches)
limit_four