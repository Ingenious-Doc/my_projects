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
                for i in range(1,len(self.operations)):
                    if self.operands[self.operations[-2]]>=self.operands[self.operations[-1]] :
                        operator=self.operations.pop(-2)
                        self.equation.append(operator)
            else:
                self.equation.append(int(my_input[i]))
        while self.operations:
            self.equation.append(self.operations.pop())
        return self.calculate(self.equation)
        # return self.equation
    def calculate(self,equation):
        my_stack=[]
        for num in equation:
            if num not in self.operands:
                my_stack.append(num)
            else:
                num1=my_stack.pop()
                num2=my_stack.pop()
                if num=="/":
                    my_stack.append(num2/num1)
                elif num=='*':
                    my_stack.append(num2*num1)
                elif num=='-':
                    my_stack.append(num2-num1)
                elif num=='+':
                    my_stack.append(num2+num1)
                else:
                    pass

        return str(my_stack)



#1 * 2 - 3 * 4
#1 2 * 3 4 * -
cal=Calculator().converter("7 + 4 - 6 * 12 - 5 + 6")
print(cal)
