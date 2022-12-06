print(sum((3-3*m+4*n)%9+1 for m,n in(('ABC'.index(i[0]),'XYZ'.index(i[2]))for i in open('2.txt').read().strip().split('\n'))))
print(sum((m+n-1)%3+1+n*3 for m,n in(('ABC'.index(i[0]),'XYZ'.index(i[2]))for i in open('2.txt').read().strip().split('\n'))))
