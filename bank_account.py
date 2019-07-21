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
    self.balance -= amount
    return amount

  def deposit(self, amount):
    if amount < 0:
      raise ValueError('You cannot deposit an amount of below 0')
    self.balance += amount
    return amount
    
  def applyAgreedOverdraft(self, preArrangeLimit):
    if (preArrangeLimit > 0):
      raise ValueError('Overdraft Credit limit should not be greater than the amount of 0')
    self.preArrangeOverdraft = preArrangeLimit
    return self

# Amount: 5000
# Remaining Balance is 2000. 
# Overdraft Limit is -10,000

# We know that 5000 is greater than 2000
# We know that 5000 is greater than -10,000

# What if the amount is 12,000
# We know that 13,000 is greater than 2000
# We know that 2,000 - 13,000 is equal to -11,000

# We know that -13,000 is less than -10,000