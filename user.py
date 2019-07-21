class User:
  def __init__(self, firstName, lastName, email):
    self.firstName = firstName
    self.lastName = lastName
    self.email = email
    self.bankAccount = None

  @property
  def fullname(self):
      return '{} {}'.format(self.firstName, self.lastName)

  # @property
  # def email(self):
  #   return '{}.{}@email.com'.format(self.first, self.last)