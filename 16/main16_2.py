import math


# Parse the Hexadecimal code store in the file to a list of strings containing the same hexadecimal code
# but translated into binary code
def parse_file(file_name: str) -> list:
    with open(file_name) as f:
        rows = [i.replace('\n', '') for i in f.readlines()]
        numbers = []

        for i in rows:
            number = [bin(int(j, base=16)) for j in i]
            binary_code = ''

            for j in number:
                j = j.replace('0b', '')
                if len(j) == 3:
                    j = '0' + j
                elif len(j) == 2:
                    j = '00' + j
                elif len(j) == 1:
                    j = '000' + j

                binary_code = binary_code + j

            numbers.append(binary_code)

    return numbers


def decode_packets(number: str):
    position = 0
    values = []

    while position < len(number) - 1:
        value, position = packet(number=number, position=position)
        values.append(value)

        while position % 4 != 0 and position < len(number) - 1:
            position += 1

    return sum(values)


def packet(number: str, position: int) -> tuple:
    position += 3

    packet_type = ''
    for i in range(position, position + 3):
        packet_type += number[i]
    position += 3
    packet_type = int(packet_type, 2)

    if packet_type != 4:
        return operator(number=number, position=position, packet_type=packet_type)

    else:
        return literal_value(number=number, position=position)


def operator(number: str, position: int, packet_type: int) -> tuple:
    length_type_ID = number[position]
    position += 1

    if length_type_ID == '0':
        length_subpackets = ''
        for i in range(position, position + 15):
            length_subpackets += number[i]
        position += 15

        length_subpackets = int(length_subpackets, 2)

        position_finished = position + length_subpackets

        literal_values = []
        while position < position_finished:
            value, position = packet(number=number, position=position)
            literal_values.append(value)

    else:
        number_subpackets = ''
        for i in range(position, position + 11):
            number_subpackets += number[i]
        position += 11

        number_subpackets = int(number_subpackets, 2)

        literal_values = []

        for i in range(0, number_subpackets):
            value, position = packet(number=number, position=position)
            literal_values.append(value)

    return type_id[packet_type](literal_values), position


def literal_value(number: str, position: int) -> tuple:
    literal_value = ''

    while True:
        part_literal_value = ''
        for i in range(position, position + 5):
            part_literal_value += number[i]

        position += 5
        literal_value += part_literal_value[1:]

        if part_literal_value[0] == '0':
            break

    return int(literal_value, 2), position


type_id = {
    0: sum,
    1: math.prod,
    2: min,
    3: max,
    5: lambda x: int(x[0] > x[1]),
    6: lambda x: int(x[0] < x[1]),
    7: lambda x: int(x[0] == x[1])
}

numbers = parse_file(file_name='input.txt')

total_values = []

for n in numbers:
    total_values.append(decode_packets(n))

print(sum(total_values))
