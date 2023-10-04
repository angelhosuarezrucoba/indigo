from typing import List


class Statistic:
    def __init__(self, numbers: List[int]) -> None:
        super().__init__()
        self.numbers: List[int] = numbers

    def less(self, number: int) -> int:
        return self.numbers[number - 1]

    def greater(self, number: int) -> int:
        return self.numbers[-1] - self.numbers[number]

    def between(self, start: int, end: int) -> int:
        return self.numbers[-1] - (self.less(start) + self.greater(end))


class DataCapture:
    def __init__(self) -> None:
        super().__init__()
        self.data: List[int] = [0] * 1000
        self.numbers: List[int] = [0] * 1000

    def add(self, value) -> None:
        self.data[value] += 1

    def build_stats(self) -> Statistic:
        self.numbers[0] = self.data[0]
        for index in range(1, len(self.data)):
            self.numbers[index] = self.numbers[index - 1] + self.data[index]
        return Statistic(self.numbers)
