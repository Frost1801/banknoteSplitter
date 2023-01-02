class Counter:
    def __init__(self, initialBanknotes):
        self.cuts = [500, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
        # checks if the input array has the right values for initial banknotes
        if len(initialBanknotes) != len(self.cuts):
            raise ValueError
        self.availableBanknotes = {}

        for i in range(0, len(initialBanknotes)):
            self.availableBanknotes[self.cuts[i]] = initialBanknotes[i]

    def __getNumberOfBanknotes(self, toSplit):
        counter = 0
        results = [0] * len(self.cuts)
        while toSplit != 0 and counter != len(self.cuts):
            if toSplit >= self.cuts[counter]:
                n = int((toSplit / self.cuts[counter]))
                if n <= self.availableBanknotes[self.cuts[counter]]:
                    toSplit = round(toSplit - self.cuts[counter] * n, 3)
                    results[counter] = n
                    self.availableBanknotes[self.cuts[counter]] -= n
            counter += 1
        if int(toSplit) != 0:
            raise Exception("No valid banknotes combination")
        return results

    def printNumberOfBanknotes(self, toSplit):
        try:
            results = self.__getNumberOfBanknotes(toSplit)
            self.__printResults(results)
        except Exception as e:
            print(e)

    def __printResults(self, results):
        total = 0
        counter = 0
        print("There are ")
        for n in results:
            if n != 0:
                print(str(n) + " pieces of " + str(self.cuts[counter]) + "$")
                total += n * self.cuts[counter]
            counter += 1
        print("In " + str(total) + "$")
