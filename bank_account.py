class BankAccount:
  def __init__(self, name, accountName, accountNumber, initialDeposit = round(0, 2)):
    self.name = name
    self.accountName = accountName
    self.accountNumber = accountNumber
    self.balance = initialDeposit
    self.overdraft = False