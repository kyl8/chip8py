class CHIP8:
    def __init__(self):
        # setting up the properties of the cpu
        self.vx = 0
        self.vy = 0
        self.DISPLAY = [0]*64*32
        self.MEMORY = [0]*4096
        self.REGISTERS = [0]*16
        self.KEY = [0]*16
        self.STACK = []
        self.SOUND_TIMER = 0
        self.DELAY_TIMER = 0
        self.INDEX_REGISTER = 0
        self.PC_COUNTER = 0
        self.STACK_POINTER = 0
        self.OPCODE = 0
        self.FONTSET = [0xF0, 0x90, 0x90, 0x90, 0xF0,  # 0
        0x20, 0x60, 0x20, 0x20, 0x70,  # 1
        0xF0, 0x10, 0xF0, 0x80, 0xF0,  # 2
        0xF0, 0x10, 0xF0, 0x10, 0xF0,  # 3
        0x90, 0x90, 0xF0, 0x10, 0x10,  # 4
        0xF0, 0x80, 0xF0, 0x10, 0xF0,  # 5
        0xF0, 0x80, 0xF0, 0x90, 0xF0,  # 6
        0xF0, 0x10, 0x20, 0x40, 0x40,  # 7
        0xF0, 0x90, 0xF0, 0x90, 0xF0,  # 8
        0xF0, 0x90, 0xF0, 0x10, 0xF0,  # 9
        0xF0, 0x90, 0xF0, 0x90, 0x90,  # A
        0xE0, 0x90, 0xE0, 0x90, 0xE0,  # B
        0xF0, 0x80, 0x80, 0x80, 0xF0,  # C
        0xE0, 0x90, 0x90, 0x90, 0xE0,  # D
        0xF0, 0x80, 0xF0, 0x80, 0xF0,  # E
        0xF0, 0x80, 0xF0, 0x80, 0x80]  # F

    # initializing the cpu
    def initialize(self):
        DISPLAY = [0]*64*32
        MEMORY = [0]*4096
        REGISTERS = [0]*16
        KEY = [0]*16
        STACK = []
        SOUND_TIMER = 0
        DELAY_TIMER = 0
        INDEX_REGISTER = 0
        STACK_POINTER = 0
        OPCODE = 0
        PC_COUNTER = 0x200

        #loading fontset
        i = 0
        while i < 80:
            self.MEMORY[i] = self.FONTSET[i]
            i += 1

    # loading rom to memory
    def load_rom(self, path):
        with open(path, "rb") as rom:
            for i, byte in enumerate(rom.read()):
                self.MEMORY[0x200 + i] = byte
        return True

    def fetch_opcode(self):
        self.opcode = self.MEMORY[self.PC_COUNTER] << 8 | self.MEMORY[self.PC_COUNTER + 1]
        return self.opcode

    #TO-DO write the rest of opcodes
    def execute_opcode(self, opcode):
        #bitwise operations to decode the opcodes
        self.vx = (self.opcode & 0x0F00) >> 8
        self.vy = (self.opcode & 0x00F0) >> 4

        #clear screen
        if (self.opcode & 0xF000 == 0x0000):
            if (self.opcode == 0x00E0):
                self.DISPLAY = [0]*64*32
                self.draw = True

    
    def emulate(self):

        if DELAY_TIMER > 0:
            DELAY_TIMER -= 1
        if SOUND_TIMER > 0:
            SOUND_TIMER -= 1
            if SOUND_TIMER == 0:
                print("BEEP")
