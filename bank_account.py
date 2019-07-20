class BankAccount:
  def __init__(self, name, accountName, accountNumber):
    self.name = name
    self.accountName = accountName
    self.accountNumber = accountNumber
    self.overdraft = False