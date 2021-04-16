class Error(Exception):
    def __init__(self, string):
        self.string = string

class Account(object):
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1
    
    def transfer(self, amount):
        self.value += amount

class Bank(object):
    """The bank"""
    def __init___(self):
        self.account = []
    
    def add(self, account):
        try:
            if not isinstance(account, Account):
                raise Error("Instance must be an Account.")
            self.account.append(account)
        except Error as e:
            print(e.string)

    def transfer(self, origin, dest, amount):
        og = find_account(origin)
        dst = find_account(dest)
        if og and dst and og != dst:
            if amount in range(0, og.value):
                og.transfer(-amount)
                dst.transfer(amount)
            return True
        return False

    def find_account(self, ident):
        if isinstance(ident, int):
            found = [acc for acc in self.account if acc.id == ident]
        elif isinstance(ident, str):
            found = [acc for acc in self.account if acc.id == ident]
            if len(found) > 1:
                print("There are several accounts with the same name. Try with account ID.")
                return None
        return found[0]

    def fix_account(self, account):