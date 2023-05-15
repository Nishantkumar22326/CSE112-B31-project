# mov0: $
# mov1 : Reg
opcode = {'add': '00000', 'sub': '00001', 'mov': ['00010', '00011'], 'ld': '00100', 'st': '00101', 'mul': '00110', 'div': '00111', 'rs': '01000', 'ls': '01001', 'xor': '01010', 'or': '01011', 'and': '01100', 'not': '01101', 'cmp': '01110', 'jmp': '01111', 'jlt': '11100', 'jgt': '11101', 'je': '11111', 'hlt': '11010', 'addf': '10000', 'subf': '10001',"var": ""}
reg = {"R0" : "000","R1" : "001", "R2" : "010", "R3" : "011", "R4" : "100", "R5" : "101", "R6" : "110","FLAGS" : "111"}
unused = {'add': '00', 'sub': '00', 'mov':[ '0', '00000'], 'ld': '0', 'st': '0', 'mul': '00', 'div': '00000', 'rs': '0', 'ls': '0', 'xor': '00', 'or': '00', 'and': '00', 'not': '00000', 'cmp': '00000', 'jmp': '0000', 'jlt': '0000', 'jgt': '0000', 'je': '0000', 'hlt': '00000000000', 'addf': '00', 'subf': '00'}
ins_size = {'add': 4, 'sub': 4, 'mov': 3, 'ld': 3, 'st': 3, 'mul': 4, 'div': 3, 'rs': 3, 'ls': 3, 'xor': 4, 'or': 4, 'and': 4, 'not': 3, 'cmp': 3, 'jmp': 2, 'jlt': 2, 'jgt': 2, 'je': 2, 'hlt': 1}
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

def flag_error(v):
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

def label_dec():
    a = bitcon(bin(label_num)[2::])
    return a

def var_dec():
    a = bitcon(bin(var_num)[2::])
    return a

def var(s):
    var_dict[s] = ""
    var_dict[s] = var_dec()
    
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

def gen(s):
    out.write(opcode[s[0]])
    out.write(unused[s[0]])
    out.write(reg[s[1]])
    out.write(reg[s[2]]) 
    out.write('\n')

def jgt(s):
    temp=bin(label_num)
    out.write(opcode["jgt"])
    out.write(unused["jgt"])
    out.write(label_dict[s[1]])
    out.write("\n")

def jlt(s):
    temp = bin(label_num)
    out.write(opcode['jlt'])
    out.write(unused['jlt'])
    out.write(label_dict[s[1]])
    out.write("\n")

def jmp(s):
    temp=bin(label_num)
    out.write(opcode["jmp"])
    out.write(unused["jmp"])
    out.write(label_dict[s[1]])
    out.write("\n")


def check_var(l):
    line = 1
    for i in l:
        v = i.split()
        if v[0] != "var":
            return line
        line += 1
        
def check_halt(l):
    line = 1
    for i in l:
        v = i.strip()
        if v == "hlt":
            if line < len(l):
                return -1
            return 1
        line += 1
    return -2

def jlt(s):
    temp = bin(label_num)
    label_dict[s[1]] = temp[2:]
    out.write(opcode['jlt'])
    out.write(unused['jlt'])
    out.write(label_dict[s[1]])
    out.write("\n")   
    
with open ("input.txt") as f:
    l = f.readlines()
    
for i in range(len(l)):
    l[i] = l[i].replace("\n","")

if('' in l):
    l.remove('')

flag = 0
line = 1

# print(check_halt(l))

for i in l:
    v = i.split()
for i in l:
    i = i.strip()
    v = i.split()
    if v[0] == 'var':
        var_dict[v[-1]] = var_dec()
        var_num += 1
    for j in v:
        if ':' in j:
            j = j.replace(":","")
            label_dict[j] = label_dec()
            label_num -= 1
    line += 1

for i in l:
    over = 1
    flags = 0
    label_info = 0
    var_info = 0
    opcode_info = 1
    v = i.split()   
    if ':' in v[0]:
        opcode_info = 0
    if 'j' in v[0]:
        label_info = 1
    if v[0] == 'ld' or v[0] == 'st':
        var_info = 1
    if v[-1] == "FLAGS":
        over = 0
        # print(line,over)
    b = error(v,opcode_info,line,label_info,var_info,over)
    if(not b):
        flag = 1
    line += 1


if(flag == 0):
    for i in l:
        v = i.split()
        if(v[0] == "mov"):
            mov(v[-1])
        elif(v[0] == 'add' or v[0] == 'sub' or v[0] == "mul" or v[0] == "and" or v[0] == "or" or v[0] == "xor"):
            gen_reg(v)
        elif(v[0] == 'hlt'):
            hlt()
        elif(v[0] == "st"):
            st(v)
        elif(v[0] == "ld"):
            ld(v)
        elif(v[0] == "div" or v[0] == "not" or v[0] == "cmp"):
            gen(v)
        elif(v[0] == 'rs' or v[0] == "ls"):
            imm(v)
        elif(v[0] == 'jgt'):
            jgt(v)
        elif (v[0] == 'jmp'):
            jmp(v)
        elif(v[0] == 'jlt'):
             jlt(v)
out.close()
