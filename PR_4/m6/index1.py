OP_NAMES = {0: 'push', 1: 'op', 2: 'call', 3: 'is', 4: 'to', 5: 'exit'}

def not_implemented(vm):
    raise RuntimeError('Not implemented!')

LIB = {
    '+': not_implemented,
    '-': not_implemented,
    '*': not_implemented,
    '/': not_implemented,
    '%': not_implemented,
    '&': not_implemented,
    '|': not_implemented,
    '^': not_implemented,
    '<': not_implemented,
    '>': not_implemented,
    '=': not_implemented,
    '<<': not_implemented,
    '>>': not_implemented,
    'if': not_implemented,
    'for': not_implemented,
    '.': not_implemented,
    'emit': not_implemented,
    '?': not_implemented,
    'array': not_implemented,
    '@': not_implemented,
    '!': not_implemented
}

def disasm(bytecode):
    pc = 0
    result = []
    while pc < len(bytecode):
        op = bytecode[pc] >> 29
        arg = bytecode[pc] & 0x1FFFFFFF
        if op == 0:  # push
            result.append('push {}'.format(arg))
        elif op == 1:  # op
            result.append('op {}'.format(LIB.keys()[arg]))
        elif op == 2:  # call
            result.append('call')
        elif op == 3:  # is
            result.append('is')
        elif op == 4:  # to
            result.append('to')
        elif op == 5:  # exit
            result.append('exit {}'.format(arg))
        else:
            raise RuntimeError('Unknown opcode: {}'.format(op))
        pc += 1
    return '\n'.join(result)

if __name__ == "__main__":
    bytecode = [0, 16, 16, 1, 121, 5]
    print(disasm(bytecode))
