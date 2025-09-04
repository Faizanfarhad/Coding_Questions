import re
def to_camel_case(text):
    s = re.sub(r"[^a-zA-Z]", " ",text)
    l = s.split()
    out= []
    
    for i in range(len(l)):
        if i == 0:
            out.append(l[i])
        else:
            out.append(l[i].capitalize())
    
    return "".join(out)
