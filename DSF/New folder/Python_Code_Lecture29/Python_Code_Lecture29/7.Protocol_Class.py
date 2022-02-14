from typing import Protocol


class Flyer(Protocol):
    def fly(self) -> None:
        print("A Flyer can fly")

class FlyingHero:
    print("This hero can fly, which is BEAST.")
    def fly(self):
        print("Like superman")


class RunningHero:
    print("This hero can run. Better than nothing!")
    def run(self):
        print("Like Flash")


class Board:
    print("An imaginary game board that doesn't do anything.")
    def make_fly(self, obj: Flyer) -> None:   #<- Here's the magic
        print("Make an object fly.")
        return obj.fly()


def main() -> None:
    board = Board()
    board.make_fly(FlyingHero())
    board.make_fly(RunningHero())  # <- Fails mypy type-checking!


if __name__ == '__main__':
    main()

