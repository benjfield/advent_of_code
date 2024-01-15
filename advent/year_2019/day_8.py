from advent.runner import register

@register(8, 2019, 1)
def image_1(text):
    layer_counts = []
    for layer_number in range(int(len(text)/150)):
        layer_counts.append({})
        for char_number in range(0, 150):
            digit = text[layer_number*150 + char_number]
            layer_counts[layer_number][digit] = layer_counts[layer_number].get(digit, 0) + 1

    lowest_zeroes = 10000
    answer = 0
    for layer_number, layer_count in enumerate(layer_counts):
        if layer_count.get("0", 0) < lowest_zeroes:
            lowest_zeroes = layer_count.get("0", 0) 
            answer = layer_count.get("1", 0) * layer_count.get("2", 0)

    return answer

@register(8, 2019, 2)
def image_2(text):
    picture = []

    for row in range(6):
        picture.append([])
        for column in range(25):
            picture[row].append(" ")

    number_of_layers = int(len(text)/150)

    for layer_number in reversed(range(number_of_layers)):
        for row in range(6):
            for column in range(25):
                digit = text[layer_number*150 + row*25 + column]
                if digit == "1":
                    picture[row][column] = "I"
                elif digit == "0":
                    picture[row][column] = " "


    for row in picture:
        row_text = "".join(row)
        print(row_text)