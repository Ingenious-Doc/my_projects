class Calculator():
    def __init__(self):
        self.operands = {'*':3,'/':3, '-':1, '+':1 }
        self.numbers=[]
        self.equation=[]
        self.operations =[]

    def converter(self,my_input):
        num_stack=[]
        my_input=my_input.split()
        order=0
        for i in range(len(my_input)):
            # 1 - 2 * 3 / 4
            if my_input[i] in self.operands:
                self.operations.append(my_input[i])
                if (self.operands[my_input[i]]<self.operands[self.operations[0]]) and len(self.operations)>1:
                    operator=self.operations.pop()
                    self.equation.append(operator)
            else:
                self.equation.append(my_input[i])
        while self.operations:
            self.equation.append(self.operations.pop())
        return "".join(self.equation)
    def calculate(self):



#1 * 2 - 3 * 4
#1 2 * 3 4 * -
cal=Calculator().parser("1 - 2 * 3 / 4")
print(cal)
