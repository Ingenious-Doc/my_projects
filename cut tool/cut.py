the_command=input("Enter the command")


def command_prompter(my_command):
    command = my_command.split(" ")
    field_no = []
    for it in command:
        if  it[0]=="-":



def tab_file_parser(file):
    my_file = open("sample.tsv","r")
    my_content = my_file.read()
    file = my_content.split('\n')
    matrix = []
    for i in range(len(file)):
        matrix.append(file[i].split("\t"))
    return matrix


command_prompter(the_command)