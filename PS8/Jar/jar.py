class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if n < 0:
            raise ValueError
        if self._size + n > self._capacity:
            raise ValueError
        self._size += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError
        if n > self._size:
            raise ValueError
        self._size -= n

    def capacity(self):
        return self._capacity

    def size(self):
        return self._size

def main():
    j = Jar()
    print(j)

if __name__=='__main__':
    main()
