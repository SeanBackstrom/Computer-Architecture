"""CPU functionality."""


import sys
# registers hold a single byte
HLT = 0b00000001 #store as binary
LDI = 0b10000010
PRN = 0b01000111
MUL = 0b10100010

class CPU:
    """Main CPU class."""


    def __init__(self):
        """Construct a new CPU."""
        self.register = [0] * 8
        self.ram = [0] * 256
        self.halted = False
        self.PC = 0

        #self.MAR = []
        #self.FL = 0
    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, value, address):
        MAR = address
        MDR = value
        self.ram[MAR] = MDR

    def load(self):
        """Load a program into memory."""
        print(sys.argv[1])
        file = sys.argv[1]
        address = 0

        if len(sys.argv) != 2:
	        print("usage: comp.py progname")
	        sys.exit(1)

        try:
            with open(file) as f:
                for line in f:
                    line = line.strip()

                    if line == '' or line[0] == '#':
                        continue

                    try:
                        str_value = line.split('#')[0]
                        value = int(str_value, 2)

                    except ValueError:
                        print(f"Invalid number: {str_value}")
                        sys.exit(1)
                    self.ram[address] = value
                    address += 1


        except FileNotFoundError:
            print(f"File not found: {file}")
            sys.exit(2)
        
        

        # For now, we've just hardcoded a program:



    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.register[reg_a] += self.register[reg_b]
        elif op == 'MULT':
            self.register[reg_a] *= self.register[reg_b]
        else:
            raise Exception("Unsupported ALU operation")



    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.PC,
            #self.fl,
            #self.ie,
            self.ram_read(self.PC),
            self.ram_read(self.PC + 1),
            self.ram_read(self.PC + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        #read whatever is in IR[PC]

        while not self.halted:

            IR = self.ram[self.PC]

            operand_a = self.ram_read(self.PC + 1)
            operand_b = self.ram_read(self.PC + 2)
            
            if IR == LDI:
                #put operand b into register[operand_a]
                self.register[operand_a] = operand_b
                self.PC += 2

            if IR == PRN:
                print(self.register[operand_a])
                self.PC +=1
            
            if IR == MUL:
                self.alu('MULT', operand_a, operand_b)
                self.PC += 2


            if IR == HLT:
                sys.exit(1)
                self.halted = True
            
            else:
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