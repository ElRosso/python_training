__author__ = 'solomina'
print "Iterators and Generators"
#*******************************
#iterator and iterable
def print_iterable(iterable):
    iterator = iter(iterable)
    try:
        while True:
            print iterator.next()
    except StopIteration:
        print "End of Collection"

print_iterable([1, 2, 3, 4, "7wqf"])

#*******************************
#generator to calculating
def squares_generation(n):
    num = 1
    while num <= n:
        yield (num, num **2)
        num += 1

for i in squares_generation(20): print i

#*******************************
#summarize cubes of values from [1:3000000]
def cubes_generation(n):
    num = 1
    while num <= n:
        yield num**3
        num += 1
print "Calculating sum. Please, wait"
print sum(i for i in cubes_generation(3000000))

#*******************************
#Create generator from file. String should be returned from generator by condition
def file_parsing(fname, parse_line):
    try:
        with open(fname,'r') as f:
            while True:
                line = f.readline()
                if line:
                    if line.find(parse_line) > -1:
                        yield line
                else:
                    break
    except Exception:
        print "File not Found"

print "Generator from file:"
for i in file_parsing("D:\\Riverbedgit_training\\python_training\\comprehension.py", "def"):
    print i

#*******************************
#Create set of combinations from name
import itertools
print __author__
for i in itertools.combinations(__author__, len(__author__)-1):
    print i