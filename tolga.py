import re
def tolga(x):
    return re.findall("[a-zA-Z]", input(f"please guess {x} your first letter:"))

