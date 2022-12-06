print(sum(ord(i)-96 if ord(i)>96 else ord(i)-38 for i in[list(set(i[:len(i)//2])&set(i[len(i)//2:]))[0] for i in open('3.txt').read().strip().split('\n')]))
print(sum(ord(i)-96 if ord(i)>96 else ord(i)-38 for i in[list(set(i)&set(j)&set(k))[0]for i,j,k in zip(*(iter(open('3.txt').read().strip().split('\n')),)*3)]))
