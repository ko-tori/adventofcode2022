print(max(sum(int(i)for i in j.split())for j in open('1.txt').read().split('\n\n')))
print(sum(list(sorted(sum(int(i)for i in j.split())for j in open('1.txt').read().split('\n\n')))[-3:]))
