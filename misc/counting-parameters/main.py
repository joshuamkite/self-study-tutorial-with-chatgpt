
# technically correct but rejected at https://pythonprinciples.com/challenges/Counting-parameters/

# def param_count(**kwargs):
#     return len(kwargs)

# required to actually get a pass with online linter

def param_count(*args, **kwargs):
    return len(args) + len(kwargs)
