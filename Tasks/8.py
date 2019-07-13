 a,b,c = map(int, input('a,b,c')).split())
if a== b==c:
    print(3)
elif a==b or a==c or b==c:
    print(2)
else:
    print(0)
