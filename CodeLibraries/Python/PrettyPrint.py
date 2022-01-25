# Print out a json document with indentations

def pretty_print(klass, indent=0):
    print(' ' * indent + type(klass).__name__ + ':')
    indent += 4
    for k,v in klass.__dict__.items():
        if '__dict__' in dir(v):
            pretty_print(v,indent)
        elif isinstance(v, list):
            for item in v:
                pretty_print(item, indent)
        else:
            print(' ' * indent + k + ': ' + str(v))