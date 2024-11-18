class FactorialCalculator:
    cache = {0: 1, 1: 1}

    @staticmethod
    def calculate(n):
        if n in FactorialCalculator.cache:
            return FactorialCalculator.cache[n]

        result = n * FactorialCalculator.calculate(n - 1)

        FactorialCalculator.cache[n] = result
        return result


if __name__ == "__main__":
    print(FactorialCalculator.calculate(5))
    print(FactorialCalculator.calculate(3))
    print(FactorialCalculator.calculate(6))
    print(FactorialCalculator.cache)