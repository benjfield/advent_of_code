from advent.runner import register

class GPSNumber:
    def __init__(
        self,
        number,
        left,
        right,
        id
    ): 
        self.number = number
        self.left = left
        self.right = right
        self.id = id

    def __eq__(self, value: object) -> bool:
        if self.id == value.id:
            return True
        return False

@register(20, 2022, 1, True)
def grove_positioning_system_1(split_text):
    numbers = [int(x) for x in split_text]

    linked_numbers = [
        GPSNumber(
            number=numbers[0],
            left=-1,
            right=1,
            id=0
        )
    ]

    for i in range(1, len(numbers) - 1):
        linked_numbers.append(
            GPSNumber(
                number=numbers[i],
                left=linked_numbers[i - 1],
                right=i+1,
                id=i
            )
        )

    linked_numbers.append(
        GPSNumber(
            number=numbers[-1],
            left=linked_numbers[len(numbers) - 2],
            right=linked_numbers[0],
            id=len(numbers) - 1
        )   
    )

    linked_numbers[0].left = linked_numbers[len(numbers) - 1]
    
    for i in range(len(numbers) - 1):
        linked_numbers[i].right = linked_numbers[i + 1]

    for gps_number in linked_numbers:
        number_to_iterate = abs(gps_number.number) % (len(numbers) - 1)
        if number_to_iterate != 0:
            gps_number.right.left = gps_number.left
            gps_number.left.right = gps_number.right
            
            if gps_number.number > 0:
                number_to_right = gps_number.right

                for i in range(number_to_iterate):
                    number_to_left = number_to_right
                    number_to_right = number_to_right.right
            else:
                number_to_left = gps_number.left

                for i in range(number_to_iterate):
                    number_to_right = number_to_left
                    number_to_left = number_to_left.left

            if number_to_left == gps_number or number_to_right == gps_number:
                raise Exception

            number_to_right.left = gps_number
            gps_number.right = number_to_right

            number_to_left.right = gps_number
            gps_number.left = number_to_left

    for gps_number in linked_numbers:
        if gps_number.number == 0:
            next_number = gps_number
            break
    total = 0
    for i in range(1, 3001):
        next_number = next_number.right

        if i % 1000 == 0:
            total += next_number.number

    return total


@register(20, 2022, 2, True)
def grove_positioning_system_2(split_text):
    numbers = [int(x) for x in split_text]

    linked_numbers = [
        GPSNumber(
            number=numbers[0] * 811589153,
            left=-1,
            right=1,
            id=0
        )
    ]

    for i in range(1, len(numbers) - 1):
        linked_numbers.append(
            GPSNumber(
                number=numbers[i] * 811589153,
                left=linked_numbers[i - 1],
                right=i+1,
                id=i
            )
        )

    linked_numbers.append(
        GPSNumber(
            number=numbers[-1] * 811589153,
            left=linked_numbers[len(numbers) - 2],
            right=linked_numbers[0],
            id=len(numbers) - 1
        )   
    )

    linked_numbers[0].left = linked_numbers[len(numbers) - 1]
    
    for i in range(len(numbers) - 1):
        linked_numbers[i].right = linked_numbers[i + 1]

    for i in range(10):
        for gps_number in linked_numbers:
            number_to_iterate = abs(gps_number.number) % (len(numbers) - 1)
            if number_to_iterate != 0:
                gps_number.right.left = gps_number.left
                gps_number.left.right = gps_number.right
                
                if gps_number.number > 0:
                    number_to_right = gps_number.right

                    for i in range(number_to_iterate):
                        number_to_left = number_to_right
                        number_to_right = number_to_right.right
                else:
                    number_to_left = gps_number.left

                    for i in range(number_to_iterate):
                        number_to_right = number_to_left
                        number_to_left = number_to_left.left

                if number_to_left == gps_number or number_to_right == gps_number:
                    raise Exception

                number_to_right.left = gps_number
                gps_number.right = number_to_right

                number_to_left.right = gps_number
                gps_number.left = number_to_left

    for gps_number in linked_numbers:
        if gps_number.number == 0:
            next_number = gps_number
            break
    total = 0
    for i in range(1, 3001):
        next_number = next_number.right

        if i % 1000 == 0:
            total += next_number.number

    return total