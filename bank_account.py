class BankAccount:
  def __init__(self, name, accountName, accountNumber, initialDeposit = round(0, 2)):
    self.name = name
    self.accountName = accountName
    self.accountNumber = accountNumber
    self.pin = 123456
    self.balance = round(initialDeposit, 2)
    self.preArrangeOverdraft = round(0, 2)

  @property
  def displayBalance(self):
    return 'Your current balance is: {}'.format(round(self.balance, 2))

  def withdraw(self, amount):
    if amount < 0:
      raise ValueError('You cannot withdraw an amount of below 0')
    if amount > self.balance and (self.balance - amount) < self.preArrangeOverdraft:
      raise ValueError('You cannot withdraw an amount greater than the pre arranged overdraft limit')
    newBalance = float("{0:.2f}".format(self.balance - amount))
    self.balance = newBalance
    return amount

  def deposit(self, amount):
    if amount < 0:
      raise ValueError('You cannot deposit an amount of below 0')
    newBalance = float("{0:.2f}".format(self.balance + amount))
    self.balance = newBalance
    return amount
    
  def applyAgreedOverdraft(self, preArrangeLimit):
    if (preArrangeLimit > 0):
      raise ValueError('Overdraft Credit limit should not be greater than the amount of 0')
    self.preArrangeOverdraft = round(preArrangeLimit, 2)
    return self