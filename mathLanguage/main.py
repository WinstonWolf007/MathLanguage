import math


var = {
    "pi": [math.pi, 'from math package', None]
}

func = {
    'int': lambda x: int(x),
    'float': lambda x: float(x),
    'pow': lambda x: x*x,
    'root': lambda x: math.sqrt(x),
    'set0': lambda x: 0
}

cond = {
    '#'
}

all_line = []


with open('test', 'r+') as file:
    for line in file:
        line = line.replace(' ', '').replace('\n', '')
        if line:
            all_line.append(line)


for line in all_line:
    if line[0:1] == '//':
        pass
    elif line[0:2] == '#!':
        equ = input(str(line[2:])+": ")
        var[line[2:]] = [eval(equ), equ, None]
    elif line[0] == '#':
        var[line[1:]] = None
    elif line[0] == ':':
        print(var[line[1:]][0])
    elif line[0] == ';':
        print(var[line[1:]][1])
    elif line[0] == '$':
        var[line[1:-1]][2] = line[-1]
    else:
        for el in var:
            allVar = "}".join(line.split('{')).split('}')
            line = ""
            for v in allVar:
                if v in var:
                    line += str(var[v][0])
                elif v != '':
                    line += str(v)

            allFunc = "]".join(line.split('[')).split(']')
            line = ""
            for f in allFunc:
                f = f.split(':')
                if len(f) == 2 and f[0] in func:
                    line += str(func[f[0]](float(f[1])))
                else:
                    line += str(''.join(f))

            if var[el] is None:
                var[el] = [eval(line), line, None]
                break
            if var[el][2] is not None and var[el][2] in '-+*/^':
                if var[el][2] == '-':
                    var[el] = [eval(line)-var[el][0], f'{var[el][1]}-{line}', None]
                elif var[el][2] == '+':
                    var[el] = [eval(line)+var[el][0], f'{var[el][1]}+{line}', None]
                elif var[el][2] == '*':
                    var[el] = [eval(line)*var[el][0], f'{var[el][1]}*{line}', None]
                elif var[el][2] == '/':
                    var[el] = [eval(line)/var[el][0], f'{var[el][1]}/{line}', None]
                break

