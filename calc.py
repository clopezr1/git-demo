print('enter operation')

op = input()

if op not in '+-*^':
    print('unknown op')

print('enter two numbers')

a = int(input())
b = int(input())


if op == '+':
    print('the sum is', a + b)
if op == '-':
    print('the difference is', a - b)
if op == '*':
    c = 0
    for i in range(a):
        c += b
    print('the product is', c)
if op == '^':
    print('a power b is', a ** b)
