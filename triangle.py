a,b,c= map(int,input().split())
if(a+b>c)&(b+c>c)&(c+a>c):
	print("yes")
else:
	print("no")
