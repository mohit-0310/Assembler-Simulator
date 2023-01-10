

dict_Reg = {'R0':'000','R1':'001','R2' : '010','R3':'011','R4':'100','R5':'101','R6':'110','FLAGS':'111'}

dict_ISA = {'add':'10000','sub':'10001','mov':'10010','ld':'10100','st':'10101','mul':'10110','div':'10111','rs':'11000','ls':'11001','xor':'11010','or':'11011','and':'11100','not':'11101','cmp':'11110','jmp':'11111','jlt':'01100','jgt':'01101','je':'01111','hlt':'01010'
}

dict_Label = {}
dict_Variable = {}

labelAddress = 1
memAddress = 5

output = []

def convert2Binary(constant):
    result = bin(int(constant))[2:]
    while(len(result)!= 8):
        result = '0' + result
    
    return result



def typeA(instruction_split,line):
    s= ''
    s += dict_ISA[instruction_split[0]]
    instruction_split = instruction_split[1:]
    s+='00'
    for instruction in instruction_split:
        if(instruction not in dict_Reg.keys()):
            print(f'Invalid Register at line {line+1}')
            exit()
        else:
            s+=dict_Reg[instruction]
    
    return s

def typeB(instruction_split,line):
    s =''
    s += dict_ISA[instruction_split[0]]
    #instruction_split = instruction_split[1:]
    
    if(instruction_split[1] not in dict_Reg.keys()):
        print(f'Invalid Register at line {line+1}')
        exit()
    else:
        s+=dict_Reg[instruction_split[1]]
    
    instruction_split[2] = int(instruction_split[2][1:])

    if(instruction_split[2]>=0 and instruction_split[2]<=255 ):
        s+=convert2Binary(instruction_split[2])
    else:
        print(f'Invalid immediate Value at line {line+1}')
        exit()
    
    return s

def typeC(instruction_split,line):
    s= ''
    if(instruction_split[0]=='mov'):
        s+='10011'
    else:
        s += dict_ISA[instruction_split[0]]
    s+='00000'

    if(instruction_split[1] not in dict_Reg.keys()):
        print(f'Invalid Register at line {line+1}')
        exit()
    else:
        s+=dict_Reg[instruction_split[1]]
    
    if(instruction_split[2] not in dict_Reg.keys()):
        print(f'Invalid Register at line {line+1}')
        exit()
    else:
        s+=dict_Reg[instruction_split[2]]

    return s

def typeD(instruction_split,line):
    s = ''
    s += dict_ISA[instruction_split[0]]

    if(instruction_split[1] not in dict_Reg.keys()):
        print(f'Invalid Register at line {line+1}')
        exit()
    else:
        s+=dict_Reg[instruction_split[1]]

    if(instruction_split[2] not in dict_Variable.keys()):
        print(f'Invalid Variable at line {line+1}')
        exit()
    else:
        s+=dict_Variable[instruction_split[2]]
    
    return s

def typeE(instruction_split,line):
    s = ''
    s += dict_ISA[instruction_split[0]]

    s+='000'

    if(instruction_split[1] not in dict_Label.keys()):
        print(f'Invalid Label at line {line+1}')
        exit()
    else:
        s+=dict_Label[instruction_split[1]]
    
    return s



    


x = ''
instructions = []
try:
    while(True):
        x = input()
        instructions.append(x)
except EOFError:
    pass



def labelRun(instruction_split,line):

        if(instruction_split[0]=='add' or instruction_split[0]=='sub' or instruction_split[0]=='mul' or instruction_split[0]=='xor' or instruction_split[0]=='and'):
            if(len(instruction_split)!=4):
                print(f"Invalid number of registers in line {line+1}")
                exit()
            else:
                output.append((typeA(instruction_split,line)))
        elif((instruction_split[0]=='mov' and instruction_split[2][0]=='$') or instruction_split[0]=='ls'):
            output.append((typeB(instruction_split,line)))
        elif(instruction_split[0]=='mov' or instruction_split[0]=='div' or instruction_split[0]=='not' or instruction_split[0]=='cmp' ):
            output.append((typeC(instruction_split,line)))
        elif(instruction_split[0]=='ld' or instruction_split[0]=='st'):
            output.append((typeD(instruction_split,line)))
        elif(instruction_split[0]=='jmp' or instruction_split[0]=='jlt' or instruction_split[0]=='jgt' or instruction_split[0]=='je'):
            output.append((typeE(instruction_split,line)))


flag = 0
i = 0
for instruction in instructions:
    
    line = i
    i+=1
    instruction_split = instruction.split()

    if(len(instruction_split)==0):
        continue
        

    if(instruction_split[0]!='var'):
        flag = 1

    if(instruction_split[0]=='add' or instruction_split[0]=='sub' or instruction_split[0]=='mul' or instruction_split[0]=='xor' or instruction_split[0]=='and'):
        if(len(instruction_split)!=4):
                print(f"Invalid number of registers in line {line+1}")
                exit()
        else:
                output.append((typeA(instruction_split,line)))
    elif((instruction_split[0]=='mov' and instruction_split[2][0]=='$') or instruction_split[0]=='ls'):
        if(len(instruction_split)!=3):
                print(f"Syntax Error in {line+1}")
                exit()
        else:
            output.append((typeB(instruction_split,line)))
    elif(instruction_split[0]=='mov' or instruction_split[0]=='div' or instruction_split[0]=='not' or instruction_split[0]=='cmp' ):
        if(len(instruction_split)!=3):
                print(f"Invalid number of registers in line {line+1}")
                exit()
        else:
            output.append((typeC(instruction_split,line)))
    elif(instruction_split[0]=='ld' or instruction_split[0]=='st'):
        if(len(instruction_split)!=3):
                print(f"Syntax error in line {line+1}")
                exit()
        else:
            output.append((typeD(instruction_split,line)))
    elif(instruction_split[0]=='var'):
        if(flag==1):
            print(f"Variable defined at wrong place in {line+1}")
            exit()
        else:
            if(len(instruction_split)==1):
                print(f"Variable name not provided in {line+1}")
                exit()
            else:
                dict_Variable[instruction_split[1]] = convert2Binary(memAddress)
                memAddress+=1
    elif(instruction_split[0]=='jmp' or instruction_split[0]=='jlt' or instruction_split[0]=='jgt' or instruction_split[0]=='je'):
        if(len(instruction_split)!=2):
                print(f"Syntax error in line {line+1}")
                exit()
        else:
            output.append((typeE(instruction_split,line)))
    elif(instruction_split[0][-1]==':' and instruction_split[0][-2]!=' '):
        if(len(instruction_split)==1):
            print(f"Invalid loop instruction in line {line+1}")
            exit()
        else:
            dict_Label[instruction_split[0][0:-1]] = convert2Binary(labelAddress)
            labelAddress+=1
            instruction_split = instruction_split[1:]
            labelRun(instruction_split,line)
    elif(instruction_split[0]=='hlt'):
        
        if(instruction_split[-1]=='hlt' and line==len(instructions)-1):
            output.append('0101000000000000')
        else:
            print(f'Invalid statement(halt) at {line+1}')
            exit()
    else:
        print(f"Syntax Error at {line+1}")
        exit()
    
if(instructions[-1]!='hlt'):
    print("'hlt' missing at the end")
    exit()

for i in output:
    print(i)