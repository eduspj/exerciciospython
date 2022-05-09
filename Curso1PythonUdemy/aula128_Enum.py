from enum import Enum, auto


class Directions(Enum):
    right = auto()
    left = auto()
    up = auto()
    down = auto()


def move(direction):
    if not isinstance(direction, Directions):
        raise ValueError('Direção não existe')
    return f'Moving {direction.name}'


if __name__ == '__main__':
    print(move(Directions.right))
    print(move(Directions.left))
    print(move(Directions.right))
    print(move(Directions.left))
    # print(move('up'))
    # print(move('down'))
