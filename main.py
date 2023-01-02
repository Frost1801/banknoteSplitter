import counter

if __name__ == '__main__':
    banknotes = [5] * 14
    c = counter.Counter(banknotes)
    c.printNumberOfBanknotes(0.76)

