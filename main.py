# mov0: $
# mov1 : Reg
opcode = {'add': '00000', 'sub': '00001', 'mov': ['00010', '00011'], 'ld': '00100', 'st': '00101', 'mul': '00110', 'div': '00111', 'rs': '01000', 'ls': '01001', 'xor': '01010', 'or': '01011', 'and': '01100', 'not': '01101', 'cmp': '01110', 'jmp': '01111', 'jlt': '11100', 'jgt': '11101', 'je': '11111', 'hlt': '11010', 'addf': '10000', 'subf': '10001',"var": ""}
reg = {"R1" : "001", "R2" : "010", "R3" : "011", "R4" : "100", "R5" : "101", "R6" : "110", "R7":"111"}
unused = {'add': '00', 'sub': '00', 'mov':[ '0', '00000'], 'ld': '0', 'st': '0', 'mul': '00', 'div': '00000', 'rs': '0', 'ls': '0', 'xor': '00', 'or': '00', 'and': '00', 'not': '00000', 'cmp': '00000', 'jmp': '0000', 'jlt': '0000', 'jgt': '0000', 'je': '0000', 'hlt': '00000000000', 'addf': '00', 'subf': '00'}
var_dict = {}
label_dict = {}
var_num = 1
label_num = 125

out = open("output.txt",'w')

def syntax_error(v):
    if v[0] not in opcode.keys():
        return False
    return True

def var_error(v):
    return True

def reg_error(v):
    return True

def label_error(v):
    return True

def size_error(v):
    return True

def error(v):
    if(syntax_error(v) and var_error(v) and reg_error(v) and label_error(v) and size_error(v)):
        return True
    return False

def bitcon(s):
    if(len(s) < 7):
        for i in range(7 - len(s)):
            s = '0' + s
    return s

def var_dec(s):
    a = bitcon(bin(var_num)[2::])
    return a

def var(s):
    var_dict[s] = var_dec(s)
    
def imm(s):
    out.write(opcode[s[0]])
    out.write(reg[s[1]])
    out.write(bitcon(bin(int(v[2][1::]))[2::]))
    out.write('\n')

def mov(s):
    if "$" in s:
        out.write(opcode["mov"][0])
        out.write(unused["mov"][0])
        out.write(reg[v[1]])
        out.write(bitcon(bin(int(v[2][1::]))[2::]))
    else:
        out.write(opcode["mov"][1])
        out.write(unused["mov"][1])
        out.write(reg[v[1]])
        out.write(reg[v[2]])
    out.write('\n')
    
def gen_reg(s):
    out.write(opcode[v[0]])
    out.write(unused[v[0]])
    out.write(reg[s[1]])
    out.write(reg[s[2]])
    out.write(reg[s[3]])
    out.write('\n')


def hlt():
    out.write(opcode['hlt'])
    out.write(unused['hlt'])
    out.write('\n')

    
def st(s):
    out.write(opcode['st'])
    out.write(unused['st'])
    out.write(reg[s[1]])
    out.write(var_dict[s[2]])
    out.write('\n')

def ld(s):
    out.write(opcode['ld'])
    out.write(unused['ld'])
    out.write(reg[s[1]])
    out.write(var_dict[s[2]])
    out.write('\n')
def jgt(s):
    temp=bin(label_num)
    out.write(opcode["jgt"])
    out.write(unused["jgt"])
    out.write(label_dict[s[1]])
    out.write("\n")    
def jmp(s):
    temp=bin(label_num)
    out.write(opcode["jmp"])
    out.write(unused["jmp"])
    out.write(label_dict[s[1]])
    out.write("\n")    

def gen(s):
    out.write(opcode[s[0]])
    out.write(unused[s[0]])
    out.write(reg[s[1]])
    out.write(reg[s[2]]) 
    out.write('\n')
        
def je(s): 
        out.write(opcode['je'])
        out.write(unused['je'])
        out.write(bitcon(bin(label_num)[2::]))
        out.write('\n')

with open ("input.txt") as f:
    l = f.readlines()
    
for i in range(len(l)):
    l[i] = l[i].replace("\n","")

flag = 0

for i in l:
    v = i.split()
    if(not error(v)):
        flag = 1
        break
    
# print(l)

# if flag == 1:
#     out.write("error\n")


for i in l:
    v = i.split()
    print(v)
    if(v[0] == "mov"):
        mov(v[-1])
    elif(v[0] == 'add' or v[0] == 'sub' or v[0] == "mul" or v[0] == "and" or v[0] == "or" or v[0] == "xor"):
        gen_reg(v)
    elif(v[0] == 'hlt'):
        hlt()
    elif(v[0] == "var"):
        var(v[-1])
        var_num += 1
    elif(v[0] == "st"):
        st(v)
    elif(v[0] == "ld"):
        ld(v)
    elif(v[0] == "div" or v[0] == "not" or v[0] == "cmp"):
        gen(v)
    elif(v[0] == 'rs' or v[0] == "ls"):
        imm(v)
    elif(v[0] == 'je'):
        je(v)
        label_num -= 1
    elif(v[0]=='jmp'):
        jmp(v)
    elif (v[0]=='jgt'):
        jgt(v)
out.close()
