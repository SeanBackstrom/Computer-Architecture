"""CPU functionality."""


import sys
# registers hold a single byte
class CPU:
    """Main CPU class."""


    def __init__(self):
        """Construct a new CPU."""
        register = [0] * 8
        memory = [0] * 256
        ram = [0] * 8
        self.ram = ram

        self.PC = 0
        self.IR = [0] * 8
        self.MAR = []
        self.FL = 0
    def ram_read(self, address):
        return ram[address]

    def ram_write(self, value, address):
        MAR = address
        MDR = value
        ram[MAR] = MDR
        return  ram[MAR]

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        #read whatever is in IR[PC]
        IR = [0]*8
        halted = False
        HLT = 1
        LDI = 130
        PRN = 71


        for i in self.ram:
            if i != 0:
                IR[self.PC] = i
                self.PC +=1
        #print(IR)
        self.PC = 0

        while not halted:
            
            operand_a = IR[self.PC+1]
            operand_b = IR[self.PC+2]
            
            if IR[self.PC] == PRN:
                print(IR[self.PC])
                self.PC +=1

            if IR[self.PC] == HLT:
                sys.exit(1)
                halted = True
            else:
                print("unknown value")
                self.PC += 1
        

# read program data
address = 0
"""
#need mod, specifiy base of value when converting to string
if len(sys.argv) != 2:
    print("usage: comp.py progname")
    sys.exit(1)

try:
    with open(sys.argv[1]) as f:
        for line in f:
            line = line.strip()

            if line == '' or line[0] == '#':
                continue
            try:
                str_value = line.split("#")[0]
                value = int(str_value, 10) #need in base 2 because binary is base 2

            except ValueError:
                print(f"invalid number: {str_value}")
                sys.exit(1)

            memory[address] = value
            address += 1

except FileNotFoundError:
    print(f"File not found: {sys.argv[1]}")
    sys.exit(2)
"""