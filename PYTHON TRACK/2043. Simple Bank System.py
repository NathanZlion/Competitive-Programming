class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.balances = balance
        self.length = len(self.balances)
    
    def validateAcc(self, accountNo):
        return 0 < accountNo <= self.length

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """

        if not (self.validateAcc(account1) and self.validateAcc(account2)):
            return False

        if self.balances[account1-1] < money:
            return False

        self.balances[account1-1] -= money
        self.balances[account2-1] += money
        return True

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """

        if not self.validateAcc(account):
            return False

        self.balances[account-1] += money
        return True        

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if not self.validateAcc(account):
            return False

        if self.balances[account-1] < money:
            return False

        self.balances[account-1] -= money
        return True        

        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
