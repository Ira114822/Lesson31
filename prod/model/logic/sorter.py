from prod.model.entity import *


class Sorter:

    @staticmethod
    def sort(park):
        if isinstance(park, Parking):
            for i in range(len(park) - 1):
                for index in range(len(park) - 1 - i):
                    if park[index].number > park[index + 1].number:
                        temp = park[index]
                        park[index] = park[index + 1]
                        park[index + 1] = temp


park = Parking()
park.add(Transport(1, 1, "AAA"))
park.add(Transport(1, 1, "fff"))
park.add(Transport(1, 1, "ggg"))
park.add(Transport(1, 1, "sss"))

print(park)
