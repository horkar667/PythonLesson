class Student:

  def __init__(self, name):
    self.name = name

  def avg(self, math, english):
    print((math + english)/2)

a001 = Student("sato")
print(a001.name)
a001.avg(30,70)

a002 = Student("tanaka")
print(a002.name)