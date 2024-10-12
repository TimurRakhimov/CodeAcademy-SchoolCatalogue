class School:
  def __init__(self, name, level, num_students):
    self.name = name
    self.level = level
    self.numberOfStudents = num_students

  def get_name(self):
    return self.name
  
  def get_level(self):
    return self.level

  def get_num_students(self):
    return self.numberOfStudents

  def set_num_students(self, new_num_students):
    self.numberOfStudents = new_num_students

  def __repr__(self):
    return f'A {self.level} school named {self.name} with {self.numberOfStudents} students'

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, "primary", numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def get_pickup(self):
    return self.pickupPolicy

  def __repr__(self):
    return super().__repr__() + f". The pickup policy is '{self.pickupPolicy}'"

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, "high", numberOfStudents)
    self.sportsTeams = sportsTeams

  def get_team(self):
    return self.sportsTeams

  def __repr__(self):
    teams = ', '.join(self.sportsTeams)
    return super().__repr__() + f". Sports teams of this school are: {teams}"


tamos = School('Tamos', 'high', 3500)

print("Testing repr:")
print(tamos)

print("\nTesting getters:")
print(tamos.get_name())
print(tamos.get_level())
print(tamos.get_num_students())

print("\nTesting setter:")
tamos.set_num_students(3550)
print(tamos.get_num_students())

miras = PrimarySchool('Miras', 2000, 'Pickup Allowed')

print("\nTesting primary school class:")
print(miras)

print("\nTesting getter:")
print(miras.get_pickup())

tru = HighSchool("TRU", 9000, ["Wolfpack Soccer", "Wolfpack Basketball", "Wolfpack Voleyball"])

print("\nTesting high school class:")
print(tru)

print("\nTesting getter:")
print(tru.get_team())
