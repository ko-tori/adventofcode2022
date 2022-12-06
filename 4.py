print(sum((a>=c)*(b<=d)|(a<=c)*(b>=d) for a,b,c,d in[[int(j)for j in __import__('re').split(',|-',i.strip())]for i in open('4.txt').readlines()]))
print(sum(a<=d and c<=b for a,b,c,d in[[int(j)for j in __import__('re').split(',|-',i.strip())]for i in open('4.txt').readlines()]))
