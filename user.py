from bank_account import BankAccount

class User:
  def __init__(self, firstName, lastName, email):
    self.firstName = firstName
    self.lastName = lastName
    self.email = email
    self.bankAccount = None

  @property
  def fullname(self):
      return '{} {}'.format(self.firstName, self.lastName)

  def open_account(self, bankName, accountNumber, initialDeposit):
    if self.bankAccount != None:
      raise ValueError('User has an existing bank account!')

    self.bankAccount = BankAccount(
      bankName,
      '{} {}'.format(self.firstName, self.lastName),
      accountNumber,
      initialDeposit,
    )
    return self.bankAccount

  def close_account(self):
    if self.bankAccount == None:
      raise ValueError('User has no existing bank account!')
    if (self.bankAccount.balance < 0):
      raise ValueError('You cannot close an account with negative balance. Please arrange your overdraft fees!')
    self.bankAccount = None
    return self.bankAccount

  # @property
  # def email(self):
  #   return '{}.{}@email.com'.format(self.first, self.last)