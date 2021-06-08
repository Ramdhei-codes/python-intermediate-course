objective = int(input('Write a number: '))
ans = 0

while ans**2 < objective:
    ans+=1

if ans**2 == objective:
    print(f'The square root of {objective} is {ans}')
else:
    print(f'{objective} does not have a exact sq root')