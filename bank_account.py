class BankAccount:
  def __init__(self, name, accountName, accountNumber, initialDeposit = round(0, 2)):
    self.name = name
    self.accountName = accountName
    self.accountNumber = accountNumber
    self.pin = 123456
    self.balance = round(initialDeposit, 2)
    self.agreedOverdraft = False

  @property
  def displayBalance(self):
    return 'Your current balance is: {}'.format(round(self.balance, 2))

  def withdraw(self, amount):
    if amount < 0:
      raise ValueError('You cannot withdraw an amount of below 0')
    if amount > self.balance and self.agreedOverdraft == False:
      raise ValueError('You cannot withdraw an amount greater than balance if you have no agreed overdraft')
    self.balance -= amount
    return amount

  def deposit(self, amount):
    if amount < 0:
      raise ValueError('You cannot deposit an amount of below 0')
    self.balance += amount
    return amount
    
  def applyAgreedOverdraft(self):
    if (self.agreedOverdraft == True):
      raise('You already applied for an agreed overdraft')
    self.agreedOverdraft = True
    return self