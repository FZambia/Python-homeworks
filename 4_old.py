n=[0,0,0,0,0,0]
a=b=999
answer=0
while(b>99):
	a=999
	while(a>=b):
		n[0]=(a*b)//100000
		n[1]=((a*b)-n[0]*100000)//10000
		n[2]=((a*b)-n[0]*100000-n[1]*10000)//1000
		n[3]=((a*b)-n[0]*100000-n[1]*10000-n[2]*1000)//100
		n[4]=((a*b)-n[0]*100000-n[1]*10000-n[2]*1000-n[3]*100)//10
		n[5]=(a*b)-n[0]*100000-n[1]*10000-n[2]*1000-n[3]*100-n[4]*10
		if(n[0]==n[5] and n[1]==n[4] and n[2]==n[3]):
			temp=n[0]+10*n[1]+100*n[2]+1000*n[3]+10000*n[4]+100000*n[5]
			if temp>answer:
				answer=temp
		a-=1
	b-=1
print(answer)