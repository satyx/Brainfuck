import sys

def loopend(i,prg):
	while(i<len(prg)):
		if prg[i]==']':
			return i
		i+=1
	return -1

def loopStart(i,prg):
	while(i>=0):
		if prg[i]=='[':
			return i
		i-=1
	return -1


def error(err):
	print('\n'+err)
	sys.exit()	




f = open(sys.argv[1],"r")
prg  = f.read()
f.close()

prg = "".join(prg.split())
prg = [i for i in prg]
i = 0
bf = ['.',',','+','-','>','<','[',']']
while(i<len(prg)):
	if prg[i] not in bf:
		del prg[i]
	else:
		i+=1
#print(prg)

cells = [0]
pointer = 0
lp = []

i=0
while(i<len(prg)):
	#print(cells,lp)
	if prg[i] == '+':
		#print("inside +")
		cells[pointer]+=1
		if(cells[pointer]>255):
			cells[pointer]=0

	elif prg[i] == '-':
		#print("inside -")
		cells[pointer]-=1
		if(cells[pointer]<0):
			cells[pointer]=255

	elif prg[i] == '>':
		#print("inside >")
		if(pointer>=len(cells)-1):
			cells.append(0)
		#print("hello",cells)
		pointer+=1
	
	elif prg[i] == '<':
		#print("inside <")
		if pointer == 0:
			error("Moved out of tape!!")
		pointer-=1
	
	elif prg[i] == '.':
		#print(cells)
		#print("inside .")
		print(chr(cells[pointer]),end="",flush=True)
		#sys.stdout.flush()
	
	elif prg[i] == ',':
		#print("inside ,")
		cells[pointer] = ord(input("Input:")[0])
	
	elif prg[i] == '[':
		#print("inside [")
		if len(lp)==0:
			lp.append(i)
		elif lp[-1]!=i:
			lp.append(i)
		
		if cells[pointer]==0:
			lp.pop()
			i = loopend(i,prg)

	elif prg[i] == ']':
		#print("inside ]")
		if len(lp)==0:
			error("Parenthesis Mismatched Error")
		i = lp[-1]-1

	i+=1


if(len(lp)!=0):
	error("Parenthesis Mismatched Error")