# coding=UTF-8
__author__ = 'solomina'

# =========================================================
# Create a function printing any name
# Create several decorators to wrap output into <div>, <span>, <a>
def div_decor(f):
    def wrapper(*args, **kwargs):
        return "<div>" + f(*args, **kwargs)+ "</div>"
    return wrapper

def a_decor(f):
    def wrapper(*args, **kwargs):
        return "<a>" + f(*args, **kwargs) + "</a>"
    return wrapper

def span_decor(f):
    def wrapper(*args, **kwargs):
        return "<span>"+ f(*args, **kwargs)+ "</span>"

    return wrapper


@div_decor
@span_decor
@a_decor
def inside_func(body):
    return body

print inside_func("Marya")

# =========================================================
# Decorator to escape unicode (non-latin) symbols
def escaper(f):
    def wrapper(*args,**kwargs):
        a = f(*args,**kwargs)
        res = ''.join([ch for ch in a if 19 < ord(ch) < 127])
        return res
    return wrapper

@escaper
def some_non_latin_string(s):
    return s

print some_non_latin_string("This is авоыпывдп - OK")

# =========================================================
# Decorator with parameter
def tag_decor(tagname):
    def decor(f):
        def wr(*args,**kwargs):
            return "<{}>".format(tagname)+f(*args,**kwargs)+"</{}>".format(tagname)
        return wr
    return decor

@tag_decor("div")
@tag_decor("span")
@tag_decor("a")
def insider(name):
    return name

print insider("SSSSSSSSSSSSSSSSS")
