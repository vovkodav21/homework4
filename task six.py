a = list(map(int, input().split()))
s=0
if len(a)<3:
   pass
else:
   for i in range(1,len(a)-1):
       if a[i] > a[i-1] and a[i]>a[i+1]:
           s+=1
print(s)