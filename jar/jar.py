import sys

class Jar:
    def __init__(self, capacity=12):
        self._capacity = self.check_capacity(capacity)
        self.cookies = 0

    def __str__(self):
        return f'{"🍪" * self.cookies}'

    def deposit(self, n):
        self.cookies = self.check_deposit(n)

    def withdraw(self, n):
        self.cookies = self.check_withdraw(n)

    def check_capacity(self, capacity):
        if capacity > 0:
            return capacity
        else:
            raise ValueError

    def check_deposit(self, n):
        if n + self.cookies <= self.capacity:
            return n + self.cookies
        else:
            raise ValueError

    def check_withdraw(self, n):
        if n <= self.cookies:
            return self.cookies - n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies

def main():
    j = Jar()

    print(j)

if __name__ == '__main__':
    main()
