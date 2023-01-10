

dict_Reg = {'000':'R0','001':'R1','010':'R2','011':'R3','100':'R4','101':'R5','110':'R6','111':'FLAGS'}

dict_ISA = {'10000':'add','10001':'sub','10010':'mov','10100':'ld','10101':'st','10110':'mul','10111':'div','11000':'rs','11001':'ls','11010':'xor','11011':'or','11100':'and','11101':'not','11110':'cmp','11111':'jmp','01100':'jlt','01101':'jgt','01111':'je','01010':'hlt'
}

dict_typeA={'10000':'add','10001':'sub','10110':'mul','11010':'xor','11011':'or','11100':'and'}
dict_typeB={'10010':'mov','11001':'ls','11000':'rs'}
dict_typeC={'10011':'mov','10111':'div','11101':'not','11110':'cmp'}
dict_typeD={'10100':'ld','10101':'st'}
dict_typeE={'11111':'jmp','01100':'jlt','01101':'jgt','01111':'je'}
dict_typeF={'01010':'hlt'}

def Binary2Decimal(n):
	return int(n,2)

def Decimal2Binary(constant):
	result = bin(int(constant))[2:]
	while(len(result)!= 8):
		result = '0' + result
	
	return result

def makeit8(constant):
	result = constant
	while(len(result)!=8):
		result = '0' + result
	
	return result

def makeit16(constant):
	result = constant
	while(len(result)!=16):
		result = '0' + result
	
	return result


x = ''
instructions = []
# try:
#     while(True):
#         x = input()
#         instructions.append(x)
# except EOFError:
#     pass

while(True):
	try:
		x = input()
		instructions.append(x)
		if(x=='0101000000000000'):
			break
	except EOFError:
		break

pCounter = 0

r0 = 0
r1 = 0
r2 = 0
r3 = 0
r4 = 0
r5 = 0
r6 = 0
flags = 0

result = []

memoryAddress=[]
for i in range (0,256):
	memoryAddress.append('0'*16)

for i in range(len(instructions)):
	memoryAddress[i] = instructions[i]



def type_A(instruction):
	global r0,r1,r2,r3,r4,r5,r6,flags,pCounter,result
	flags = 0
	reg1 = dict_Reg[instruction[7:10]]
	reg2 = dict_Reg[instruction[10:13]]
	reg3 = dict_Reg[instruction[13:16]]
	operation = dict_ISA[instruction[0:5]]

	if (reg1 == 'R1'):
		a = r1
	elif(reg1 == 'R0'):
		a = r0
	elif (reg1 == 'R2'):
		a = r2
	elif (reg1 == 'R3'):
		a = r3 
	elif (reg1 == 'R4'):
		a = r4
	elif (reg1 == 'R5'):
		a = r5
	elif (reg1 == 'R6'):
		a = r6

	if (reg2 == 'R1'):
		b = r1
	elif(reg2 == 'R0'):
		b = r0
	elif (reg2 == 'R2'):
		b = r2
	elif (reg2 == 'R3'):
		b = r3 
	elif (reg2 == 'R4'):
		b = r4
	elif (reg2 == 'R5'):
		b = r5
	elif (reg2 == 'R6'):
		b = r6

	if (reg3 == 'R1'):
		c = r1
	elif(reg3 == 'R0'):
		c = r0
	elif (reg3 == 'R2'):
		c = r2
	elif (reg3 == 'R3'):
		c = r3
	elif (reg3 == 'R4'):
		c = r4
	elif (reg3 == 'R5'):
		c = r5
	elif (reg3 == 'R6'):
		c  = r6

	if(operation == 'add'):
		c = b+a
	elif(operation == 'sub'):
		c = a-b
	elif(operation == 'mul'):
		c = a*b
	elif(operation == 'xor'):
		c = a ^ b
	elif(operation == 'or'):
		c = a or b
	elif(operation == 'and'):
		c = a and b

	if (reg3 == 'R1'):
		r1 = c		
	elif(reg3 == 'R0'):
		r0 = (c)
	elif (reg3 == 'R2'):
		r2 = (c)
	elif (reg3 == 'R3'):
		r3 = (c)
	elif (reg3 == 'R4'):
		r4 = (c)
	elif (reg3 == 'R5'):
		r5 = (c)
	elif (reg3 == 'R6'):
		r6 = (c)

	# s = makeit8(Decimal2Binary(pCounter))+" "+makeit16(Decimal2Binary(r0))+ " " + makeit16(Decimal2Binary(r1))+ " " + makeit16(Decimal2Binary(r2))+ " " + makeit16(Decimal2Binary(r3))+ " " + makeit16(Decimal2Binary(r4))+ " " +makeit16(Decimal2Binary(r5))+ " " + makeit16(Decimal2Binary(r6))+ " " + makeit16(Decimal2Binary(flags))
	# pCounter+=1
	# result.append(s)

def type_B(instruction):
	global r0,r1,r2,r3,r4,r5,r6,flags,pCounter,result
	flags = 0
	operation = dict_ISA[instruction[0:5]]
	constant = Binary2Decimal(instruction[8:16])
	reg1 = dict_Reg[instruction[5:8]]
	
	if (reg1 == 'R1'):
		a = r1
	elif(reg1 == 'R0'):
		a = r0
	elif (reg1 == 'R2'):
		a = r2
	elif (reg1 == 'R3'):
		a = r3 
	elif (reg1 == 'R4'):
		a = r4
	elif (reg1 == 'R5'):
		a = r5
	elif (reg1 == 'R6'):
		a = r6
	
	if(operation == 'mov'):
		a = constant
	elif(operation == 'ls'):
		a = a << constant
		b = bin(a)[2:]
		if(len(b)<=8):
			a = a
		else:
			b = b[-8:]
			a = Binary2Decimal(b)

	elif (operation == 'rs'):
		a = a >> constant
		b = bin(a)[2:]
		if(len(b)<=8):
			a = a
		else:
			b = b[-8:]
			a = Binary2Decimal(b)
	
	if (reg1 == 'R1'):
		r1 = a		
	elif(reg1 == 'R0'):
		r0 = (a)
	elif (reg1 == 'R2'):
		r2 = (a)
	elif (reg1 == 'R3'):
		r3 = (a)
	elif (reg1 == 'R4'):
		r4 = (a)
	elif (reg1 == 'R5'):
		r5 = (a)
	elif (reg1 == 'R6'):
		r6 = (a)
	
	# s = makeit8(Decimal2Binary(pCounter))+" "+makeit16(Decimal2Binary(r0))+ " " + makeit16(Decimal2Binary(r1))+ " " + makeit16(Decimal2Binary(r2))+ " " + makeit16(Decimal2Binary(r3))+ " " + makeit16(Decimal2Binary(r4))+ " " +makeit16(Decimal2Binary(r5))+ " " + makeit16(Decimal2Binary(r6))+ " " + makeit16(Decimal2Binary(flags))
	# pCounter+=1
	# result.append(s)



def type_C(instruction):
	global r0,r1,r2,r3,r4,r5,r6,flags,pCounter,result
	operation = dict_typeC[instruction[0:5]]  
	reg2 = dict_Reg[instruction[10:13]]
	reg3 = dict_Reg[instruction[13:16]]
	b = 0
	if (reg2 == 'R1'):
		b = r1
	elif(reg2 == 'R0'):
		b = r0
	elif (reg2 == 'R2'):
		b = r2
	elif (reg2 == 'R3'):
		b = r3
	elif (reg2 == 'R4'):
		b = r4
	elif (reg2 == 'R5'):
		b = r5
	elif (reg2 == 'R6'):
		b = r6
	elif(reg2=='FLAGS'):
		b = flags

	if (reg3 == 'R1'):
		c = r1
	elif(reg3 == 'R0'):
		c = r0
	elif (reg3 == 'R2'):
		c = r2
	elif (reg3 == 'R3'):
		c = r3
	elif (reg3 == 'R4'):
		c = r4
	elif (reg3 == 'R5'):
		c = r5
	elif (reg3 == 'R6'):
		c = r6
	elif(reg3=='FLAGS'):
		c = flags

	if (operation == 'mov'):
		
		c = b
		if (reg3 == 'R1'):
			r1 = c	
		elif(reg3 == 'R0'):
			r0 = c	
		elif (reg3 == 'R2'):
			r2 = c	
		elif (reg3 == 'R3'):
			r3 = c	
		elif (reg3 == 'R4'):
			r4 = c	
		elif (reg3 == 'R5'):
			r5 = c	
		elif (reg3 == 'R6'):
			r6 = c	
		flags = 0
	elif (operation == 'div'):
		flags = 0
		r0 = (b//c)
		r1 = (b%c)
	elif (operation == 'not'):
		flags = 0
		c = ~b
		if (reg3 == 'R1'):
			r1 = c			
		elif(reg3 == 'R0'):
			r0 = c	
		elif (reg3 == 'R2'):
			r2 = c	
		elif (reg3 == 'R3'):
			r3 = c	
		elif (reg3 == 'R4'):
			r4 = c	
		elif (reg3 == 'R5'):
			r5 = c	
		elif (reg3 == 'R6'):
			r6 = c	
	elif (operation == 'cmp'):
		if (c==b):
			flags = 1
		if (c>b):
			flags = 4
		if (c<b):
			flags = 2
	
	# s = makeit8(Decimal2Binary(pCounter))+" "+makeit16(Decimal2Binary(r0))+ " " + makeit16(Decimal2Binary(r1))+ " " + makeit16(Decimal2Binary(r2))+ " " + makeit16(Decimal2Binary(r3))+ " " + makeit16(Decimal2Binary(r4))+ " " +makeit16(Decimal2Binary(r5))+ " " + makeit16(Decimal2Binary(r6))+ " " + makeit16(Decimal2Binary(flags))
	# pCounter+=1
	# result.append(s)

def type_D(instruction):
	global memoryAddress
	global r0,r1,r2,r3,r4,r5,r6,flags,result,pCounter
	flags = 0
	operation = dict_typeD[instruction[0:5]]  
	rega = dict_Reg[instruction[5:8]]
	mem = instruction[8:16]
	if(operation=='ld'):
		z = Binary2Decimal(mem)
		#c = memoryAddress.index(z)
		d = Binary2Decimal(memoryAddress[z])

		if (rega == 'R1'):
			r1 = d
		elif(rega == 'R0'):
			r0 = d
		elif (rega == 'R2'):
			r2 = d
		elif (rega == 'R3'):
			r3 = d
		elif (rega == 'R4'):
			r4 = d
		elif (rega == 'R5'):
			r5 = d
		elif (rega == 'R6'):
			r6 = d

	elif(operation=='st'):

		d = Binary2Decimal(mem)

		if (rega == 'R1'):
			c = r1
		elif(rega == 'R0'):
			c = r0
		elif (rega == 'R2'):
			c = r2
		elif (rega == 'R3'):
			c = r3
		elif (rega == 'R4'):
			c = r4
		elif (rega == 'R5'):
			c = r5
		elif (rega == 'R6'):
			c = r6
		
		memoryAddress[d] = makeit16(Decimal2Binary(c)) 

	# s = makeit8(Decimal2Binary(pCounter))+" "+makeit16(Decimal2Binary(r0))+ " " + makeit16(Decimal2Binary(r1))+ " " + makeit16(Decimal2Binary(r2))+ " " + makeit16(Decimal2Binary(r3))+ " " + makeit16(Decimal2Binary(r4))+ " " +makeit16(Decimal2Binary(r5))+ " " + makeit16(Decimal2Binary(r6))+ " " + makeit16(Decimal2Binary(flags))
	# pCounter+=1
	# result.append(s)
	
		

def type_E(instruction):
	global r0,r1,r2,r3,r4,r5,r6,flags,pCounter,result
	# flags = 0
	operation = dict_ISA[instruction[0:5]]
	mem = instruction[8:16]
	
	#print(pCounter)
	if (operation == 'jmp'):
		
		d = Binary2Decimal(mem)
		s =makeit8(Decimal2Binary(pCounter))+" "+makeit16(Decimal2Binary(r0))+ " " + makeit16(Decimal2Binary(r1))+ " " + makeit16(Decimal2Binary(r2))+ " " + makeit16(Decimal2Binary(r3))+ " " + makeit16(Decimal2Binary(r4))+ " " +makeit16(Decimal2Binary(r5))+ " " + makeit16(Decimal2Binary(r6))+ " " + makeit16(Decimal2Binary(flags))
		result.append(s)
		pCounter = d
		
		# pCounter+=1
		
	elif (operation == 'jlt'):
		if (flags == 4):
			flags = 0
			d = Binary2Decimal(mem)
			s = makeit8(Decimal2Binary(pCounter))+" "+makeit16(Decimal2Binary(r0))+ " " + makeit16(Decimal2Binary(r1))+ " " + makeit16(Decimal2Binary(r2))+ " " + makeit16(Decimal2Binary(r3))+ " " + makeit16(Decimal2Binary(r4))+ " " +makeit16(Decimal2Binary(r5))+ " " + makeit16(Decimal2Binary(r6))+ " " + makeit16(Decimal2Binary(flags))
			result.append(s)
			pCounter = d
			# pCounter+=1
		else:
			flags = 0
			s =makeit8(Decimal2Binary(pCounter))+" "+makeit16(Decimal2Binary(r0))+ " " + makeit16(Decimal2Binary(r1))+ " " + makeit16(Decimal2Binary(r2))+ " " + makeit16(Decimal2Binary(r3))+ " " + makeit16(Decimal2Binary(r4))+ " " +makeit16(Decimal2Binary(r5))+ " " + makeit16(Decimal2Binary(r6))+ " " + makeit16(Decimal2Binary(flags))
			result.append(s)
			pCounter+=1
	elif (operation == 'jgt'):
		if (flags == 2):
			flags = 0
			d = Binary2Decimal(mem)
			s = makeit8(Decimal2Binary(pCounter))+" "+makeit16(Decimal2Binary(r0))+ " " + makeit16(Decimal2Binary(r1))+ " " + makeit16(Decimal2Binary(r2))+ " " + makeit16(Decimal2Binary(r3))+ " " + makeit16(Decimal2Binary(r4))+ " " +makeit16(Decimal2Binary(r5))+ " " + makeit16(Decimal2Binary(r6))+ " " + makeit16(Decimal2Binary(flags))
			result.append(s)
			pCounter = d
			# pCounter+=1
		else:
			flags = 0
			s =makeit8(Decimal2Binary(pCounter))+" "+makeit16(Decimal2Binary(r0))+ " " + makeit16(Decimal2Binary(r1))+ " " + makeit16(Decimal2Binary(r2))+ " " + makeit16(Decimal2Binary(r3))+ " " + makeit16(Decimal2Binary(r4))+ " " +makeit16(Decimal2Binary(r5))+ " " + makeit16(Decimal2Binary(r6))+ " " + makeit16(Decimal2Binary(flags))
			result.append(s)
			pCounter+=1
	elif (operation == 'je'):
		if (flags == 1):
			flags = 0
			d = Binary2Decimal(mem)
			s = makeit8(Decimal2Binary(pCounter))+" "+makeit16(Decimal2Binary(r0))+ " " + makeit16(Decimal2Binary(r1))+ " " + makeit16(Decimal2Binary(r2))+ " " + makeit16(Decimal2Binary(r3))+ " " + makeit16(Decimal2Binary(r4))+ " " +makeit16(Decimal2Binary(r5))+ " " + makeit16(Decimal2Binary(r6))+ " " + makeit16(Decimal2Binary(flags))
			result.append(s)
			pCounter = d
			# pCounter+=1
		else:
			flags = 0
			s =makeit8(Decimal2Binary(pCounter))+" "+makeit16(Decimal2Binary(r0))+ " " + makeit16(Decimal2Binary(r1))+ " " + makeit16(Decimal2Binary(r2))+ " " + makeit16(Decimal2Binary(r3))+ " " + makeit16(Decimal2Binary(r4))+ " " +makeit16(Decimal2Binary(r5))+ " " + makeit16(Decimal2Binary(r6))+ " " + makeit16(Decimal2Binary(flags))
			result.append(s)
			pCounter+=1
	flags = 0
	

def type_F():
	pass




def main():
	global pCounter,flags
	length = len(instructions)
	#for instruction in instructions:
	while(pCounter!=length):
		instruction = instructions[pCounter]
		opCode = instruction[:5] #opcode
		if(opCode in dict_typeA.keys()):
				type_A(instruction)
		elif(opCode in dict_typeB.keys()):
				type_B(instruction)
		elif(opCode in dict_typeC.keys()):
				type_C(instruction)
		elif(opCode in dict_typeD.keys()):
			type_D(instruction)
		elif(opCode in dict_typeE.keys()):
			type_E(instruction)
			
		elif(opCode in dict_typeF.keys()):
			pass
		
		if(opCode not in dict_typeE.keys()):
			s = makeit8(Decimal2Binary(pCounter))+" "+makeit16(Decimal2Binary(r0))+ " " + makeit16(Decimal2Binary(r1))+ " " + makeit16(Decimal2Binary(r2))+ " " + makeit16(Decimal2Binary(r3))+ " " + makeit16(Decimal2Binary(r4))+ " " +makeit16(Decimal2Binary(r5))+ " " + makeit16(Decimal2Binary(r6))+ " " + makeit16(Decimal2Binary(flags))
			pCounter+=1
			result.append(s)
		else:
			# s = makeit8(Decimal2Binary(pCounter))+" "+makeit16(Decimal2Binary(r0))+ " " + makeit16(Decimal2Binary(r1))+ " " + makeit16(Decimal2Binary(r2))+ " " + makeit16(Decimal2Binary(r3))+ " " + makeit16(Decimal2Binary(r4))+ " " +makeit16(Decimal2Binary(r5))+ " " + makeit16(Decimal2Binary(r6))+ " " + makeit16(Decimal2Binary(flags))
			# result.append(s)
			pass
		

		



		

main()

for i in result:
	print(i)

for y in memoryAddress:
	print(y)