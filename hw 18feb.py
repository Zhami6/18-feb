from __future__ import annotations


class RomanicNumber:
    def __init__(self, value: int) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"RomanicNumber({self.value})"

    def __str__(self) -> str:
        return self.to_roman()

    def __add__(self, other: RomanicNumber) -> RomanicNumber:
        return RomanicNumber(self.value + other.value)

    def __sub__(self, other: RomanicNumber) -> RomanicNumber:
        return RomanicNumber(self.value - other.value)

    def __mul__(self, other: RomanicNumber) -> RomanicNumber:
        return RomanicNumber(self.value * other.value)

    def __floordiv__(self, other: RomanicNumber) -> RomanicNumber:
        return RomanicNumber(self.value // other.value)

    def __eq__(self, other: RomanicNumber) -> bool:
        return self.value == other.value

    def __lt__(self, other: RomanicNumber) -> bool:
        return self.value < other.value

    def __le__(self, other: RomanicNumber) -> bool:
        return self.value <= other.value

    def __gt__(self, other: RomanicNumber) -> bool:
        return self.value > other.value

    def __ge__(self, other: RomanicNumber) -> bool:
        return self.value >= other.value

    @staticmethod
    def from_arabic(arabic_number: int) -> RomanicNumber:
        return RomanicNumber(arabic_number)

    def to_roman(self) -> str:
        roman_numerals = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }

        result = ""
        for value, numeral in sorted(roman_numerals.items(), reverse=True):
            while self.value >= value:
                result += numeral
                self.value -= value
        return result


a = RomanicNumber.from_arabic(int(input("Введите число a: ")))
b = RomanicNumber.from_arabic(int(input("Введите число b: ")))

print("Сумма:", a + b)
print("Разность:", a - b)
print("Произведение:", a * b)
print("Целочисленное деление:", a // b)
print("Равны ли:", a == b)
print("Больше или равно:", a >= b)
print("Больше:", a > b)
print("Меньше или равно:", a <= b)
print("Меньше:", a < b)
