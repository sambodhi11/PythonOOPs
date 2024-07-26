class P:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def display(self):
    print(self.firstname, self.lastname)

class S(P):
  pass

x = S("Sambodhi","Kotekar")
x.display()