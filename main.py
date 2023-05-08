# mov0: $
# mov1 : Reg
opcode = {'add': '00000', 'sub': '00001', 'mov': ['00010', '00011'], 'ld': '00100', 'st': '00101', 'mul': '00110', 'div': '00111', 'rs': '01000', 'ls': '01001', 'xor': '01010', 'or': '01011', 'and': '01100', 'not': '01101', 'cmp': '01110', 'jmp': '01111', 'jlt': '11100', 'jgt': '11101', 'je': '11111', 'hlt': '11010', 'addf': '10000', 'subf': '10001'}
reg = {"R1" : "001", "R2" : "010", "R3" : "011", "R4" : "100", "R5" : "101", "R6" : "110", "R7":"111"}
unused = {'add': '00', 'sub': '00', 'mov':[ '0', '00000'], 'ld': '0', 'st': '0', 'mul': '00', 'div': '00000', 'rs': '0', 'ls': '0', 'xor': '00', 'or': '00', 'and': '00', 'not': '00000', 'cmp': '00000', 'jmp': '0000', 'jlt': '0000', 'jgt': '0000', 'je': '0000', 'hlt': '00000000000', 'addf': '00', 'subf': '00'}
var_dict = {}
var_num = 1
label_num = 125

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
    print(opcode[s[0]],end = "_")
    print(reg[s[1]],end = "_")
    print(bitcon(bin(int(v[2][1::]))[2::]))
    
def mov(s):
    if "$" in s:
        print(opcode["mov"][0],end = "_")
        print(unused["mov"][0],end = "_")
        print(reg[v[1]],end = "_")
        print(bitcon(bin(int(v[2][1::]))[2::]))
    else:
        print(opcode["mov"][1],end = "_")
        print(unused["mov"][1],end = "_")
        print(reg[v[1]],end = "_")
        print(reg[v[2]])
        
def gen_reg(s):
    print(opcode[v[0]],end = "_")
    print(unused[v[0]],end = "_")
    print(reg[s[1]],end = "_")
    print(reg[s[2]],end = "_")
    print(reg[s[3]])


def hlt():
    print(opcode['hlt'],end = "_")
    print(unused['hlt'])
    
    
def st(s):
    print(opcode['st'],end = "_")
    print(unused['st'],end = "_")
    print(reg[s[1]],end = "_")
    print(var_dict[s[2]])
    
def ld(s):
    print(opcode['ld'],end = "_")
    print(unused['ld'],end = "_")
    print(reg[s[1]],end = "_")
    print(var_dict[s[2]])

def gen(s):
    print(opcode[s[0]],end = "_")
    print(unused[s[0]],end = "_")
    print(reg[s[1]],end = "_")
    print(reg[s[2]]) 

def jmp(s):
    print(opcode[s[0]],end = "_")
    print(unused[s[0]],end = "_")
    print(bin(label_num)[2::])

with open ("input.txt") as f:
    l = f.readlines()
    
for i in range(len(l)):
    l[i] = l[i].replace("\n","")

for i in l:
    v = i.split()
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
    elif(v[0] == "jmp" or v[0] == 'jlt' or v[0] == 'jgt' or v[0] == 'je'):
        jmp(v)
        label_num -= 1
