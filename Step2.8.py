s=input()
cnt=1
i=0
x=len(s)
while (i < x-1):
  if s[i]==s[i+1]:
    cnt+=1
  else:
    print(s[i],end='')
    print(cnt,end='')
    cnt=1
  i+=1
print(s[-1],end='')
print(cnt,end='')
