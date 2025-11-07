from collections import defaultdict

def int_code(ns, in_val):
    ns = defaultdict(int, enumerate(map(int, ns)))
    #opcodes   x 1 2 3 4 5 6 7 8 9
    lengths = [0,4,4,2,2,3,3,4,4,2]
    output = []
    ip = 0
    rb = 0
    inp_iter = iter(in_val)
    while True:
        opc = ns[ip]
        modes = [opc // (10**i) % 10 for i in range(2, 5)]
        #0 for position mode, 1 for immediate mode, #2 for relative mode
        opc = opc % 100
        if opc == 99:
            return output
        # parameters: 1-3 numbers directly related to this opcode
        params = [ns[ip+i] for i in range(1, lengths[opc]) ]
        read = [0, 0, 0] #values, no locations
        write_to = [0,0,0] #locations
        for i in range(len(params)):
            if modes[i] == 0: #possition
                read[i] = ns[params[i]]
                write_to[i] = params[i]
            elif modes[i] == 1: #immediate
                read[i] = params[i]
                #write ie never immediate
            if modes[i] == 2: #relative
                read[i] = ns[params[i]+rb]
                write_to[i] = params[i]+rb
        if opc == 1: #add up
            ns[write_to[2]] = read[0] + read[1]
        elif opc == 2: #multiple
            ns[write_to[2]] = read[0] * read[1]
        elif opc == 3: #input
            ns[write_to[0]] = next(inp_iter)
        elif opc == 4: #output
            output.append(read[0])
        elif opc == 5: #jump if true
            if read[0] != 0: ip = read[1] - 3
        elif opc == 6: #jump if false
            if read[0] == 0: ip = read[1] - 3
        elif opc == 7: #less than
            ns[write_to[2]] = 1 if read[0] < read[1] else 0
        elif opc == 8: #equals
            ns[write_to[2]] = 1 if read[0] == read[1] else 0
        elif opc == 9:
            rb += read[0]
        ip += lengths[opc]