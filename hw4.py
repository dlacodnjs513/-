def rep_char(char, length):
    return char * length

def draw_line_string(msg):
    line = rep_char('-', len(msg) + 4)
    return line

def get_name():
    name = input("input his/her name: ")
    return name.title()

def print_message(name):
    msg1 = f"Hello {name},"
    msg2 = "Welcome to Seoul."
    
    line_length = len(msg1) if len(msg1) > len(msg2) else len(msg2)
    line = draw_line_string(msg1 if len(msg1) > len(msg2) else msg2)
    
    print(line)
    print(msg1)
    print(msg2)
    print(line)

name = get_name()
print_message(name)
