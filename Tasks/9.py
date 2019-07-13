n1, m1, n2, m2 = map(int, input('n1, m1, n2, m2')).split())
dn= math.abs(n2-n1)
dm = math.abs(m2-m1)
if (dn==1 and dm==2) or (dn==2 and dm==1):
    print('YES')
else: 
    print('NO')
