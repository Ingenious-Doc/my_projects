import re

the_command = input("Enter the command")


def command_prompter(input_command):
    command = input_command.split("|")
    my_commands = []
    for split_commands in command:
        my_commands.append(split_commands)
    fields = []
    delimiter = ""
    file = ""
    lines = ""
    start =""
    # cut -d, -f"1 2" fourchords.csv | head -n5
    #cut -d, -f1,2 fourchords.csv | head -n5
    for func in my_commands:
        if '-f"' in func:
            fields=func.split('"')[1::2]
            fields=fields[0].split(" ")
            func=func.replace('-f"'+fields[0]+'"',"")
            func=func.split(" ")
            if "" in func:
                # print("we're in")
                func.remove("")
            if func[0] == "head" or func[0] == "tail":
                start = func.pop(0)

            for item in func:
                if item[0:2] == "-d":
                    delimiter = item[2]
                elif item[0:2] == "-n":
                    lines = item[2]
                elif (".csv" or ".tsv") in item:
                    file = item
                else:
                    pass
        else:
            function = func.split(" ")
            if "" in function:
                function.remove("")
            if function[0] == "head" or function[0] == "tail":
                start = function.pop(0)
            for item in function:
                if item[0:2] == "-f":
                    fields = item[2:].split(",")
                elif item[0:2] == "-d":
                    delimiter = item[2]
                elif item[0:2] == "-n":
                    lines = item[2]
                elif (".csv" or ".tsv") in item:
                    file = item
    return file, delimiter, lines,fields,start

def tab_file_parser(file):
    my_file = open(f"{file}", "r",encoding="utf-8")
    my_content = my_file.read()
    file = my_content.split('\n')
    matrix = []
    for i in range(len(file)):
        matrix.append(file[i].split("\t"))
    return matrix


def comma_file_parser(file):
    my_file = open(f"{file}", "r",encoding='utf-8')
    my_content = my_file.read()
    file = my_content.split('\n')
    matrix = []
    for i in range(len(file)):
        matrix.append(file[i].split(","))
    return matrix

def field_picker(matrix, fields, lines=0,tail=""):
    if lines>0:
        if tail=="tail":
            matrix=matrix[::-1]
            print(matrix)
            for i in range(len(fields)):
                for k in range(lines,0,-1):
                    print(matrix[k][int(fields[i])-1])
        else:
            for i in range(len(fields)):
                for k in range(lines):
                    print(matrix[k][int(fields[i])-1])





my_file,mydelimiter,mylines,myfields,mystart=command_prompter(the_command)
mymatrix=comma_file_parser(my_file)
print(mystart)
field_picker(mymatrix,myfields,int(mylines),mystart)
