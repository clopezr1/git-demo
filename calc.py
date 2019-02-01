print('enter operation')

op = input()

if op not in '+*':
    print('unknown op')

print('enter two numbers')

a = int(input())
b = int(input())


if op == '+':
    print('the sum is', a + b)

if op == '*':
    print('the product is', a * b)
