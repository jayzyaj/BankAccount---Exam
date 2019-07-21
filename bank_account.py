from helpers.formatter import formatMoney

class BankAccount:
  def __init__(self, name, accountName, accountNumber, initialDeposit = formatMoney(0)):
    self.name = name
    self.accountName = accountName
    self.accountNumber = accountNumber
    self.pin = 123456
    self.balance = formatMoney(initialDeposit)
    self.preArrangeOverdraft = formatMoney(0)

  @property
  def displayBalance(self):
    return 'Your current balance is: {}'.format(formatMoney(self.balance))

  def withdraw(self, amount):
    if amount < 0:
      raise ValueError('You cannot withdraw an amount of below 0')
    if amount > self.balance and (self.balance - amount) < self.preArrangeOverdraft:
      raise ValueError('You cannot withdraw an amount greater than the pre arranged overdraft limit')
    newBalance = formatMoney(self.balance - amount)
    self.balance = newBalance
    return amount

  def deposit(self, amount):
    if amount < 0:
      raise ValueError('You cannot deposit an amount of below 0')
    newBalance = formatMoney(self.balance + amount)
    self.balance = newBalance
    return amount
    
  def applyAgreedOverdraft(self, preArrangeLimit):
    if (preArrangeLimit > 0):
      raise ValueError('Overdraft Credit limit should not be greater than the amount of 0')
    self.preArrangeOverdraft = formatMoney(preArrangeLimit)
    return self