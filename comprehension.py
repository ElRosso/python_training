__author__ = 'solomina'

print "List Comprehensions"
#*******************************
#comprehensions: list of tuples [(num, num^2, num^3),...] where 1 <= num <= 20
def num_powers(n):
    return [(i, i*i, i**3) for i in range(1, n, 1)]

l = num_powers(20)
print type(l), l

#*******************************
#comprehensions: set of cubes of even numbers where 1 <= num <= 20
def cubes_of_evens(n):
    return {num**3 for num in range(2, n, 2)}

s = cubes_of_evens(20)
print type(s), s

#*******************************
#comprehensions: create a dictionary from string/ Example: "string" => {'s':115,'n':110,...}
def string_to_dict(s):
    return {a:ord(a) for a in s}

d = string_to_dict("this is a string")
print type(d), d

#*******************************
#comprehensions: create a dictionary {num: num^3} where num%2 == 0 && num%10 != 0
def dict_of_cubes(start, end):
    return {n:n**3 for n in range (start, end) if n % 2 == 0 and n % 10 != 0}

print (dict_of_cubes(10,1000))

