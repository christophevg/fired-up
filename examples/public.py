from fired_up import FiredUp, Group

class Test(Group):
  def public1(self):
    return "abc"                  # return value is "copied", self is returned

  def public2(self):
    print(self.public1().paste()) # returns the return value of public

  def public3(self):
    return self.public1()         # returns self, which is "pasted" as last result

FiredUp(test=Test)
