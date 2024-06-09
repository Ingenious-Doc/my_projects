import re
the_command=input("Enter the command")


def command_prompter(input_command):
    command=input_command.split("|")
    my_commands=[]
    for split_commands in command:
        my_commands.append(split_commands)
    fields=[]
    delimiter=""
    file=""
    lines=""
    commands=[]
    for func in my_commands:
        if '-f"' in func:
            for string in func:
                
        else:
            function=func.split(" ")
            function.remove("")
            commands.append(function.pop(0))
            for item in function:
                if item[0:2]=="-f":
                    fields=item[2:].split(",")
                elif item[0:2]=="-d":
                    delimiter=item[2]
                elif item[0:2]=="-n":
                    lines=item[2]
                else:
                    file=item


def tab_file_parser(file):
    my_file = open("sample.tsv","r")
    my_content = my_file.read()
    file = my_content.split('\n')
    matrix = []
    for i in range(len(file)):
        matrix.append(file[i].split("\t"))
    return matrix


def field_picker(matrix,fields):
    pass
command_prompter(the_command)