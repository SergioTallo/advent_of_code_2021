def parse_file(file_name: str) -> list:
    with open(file_name) as f:
        rows = [i.replace('\n', '') for i in f.readlines()]
        numbers = []

        for i in rows:
            number = [bin(int(j, base=16)) for j in i]
            number_parsed = []
            for j in number:
                j = j.replace('0b', '')
                if len(j) == 3:
                    j = '0' + j
                elif len(j) == 2:
                    j = '00' + j
                elif len(j) == 1:
                    j = '000' + j
                number_parsed.append(j)
            final_number = ''
            for k in number_parsed:
                final_number += k

            numbers.append(final_number)

    return numbers


def decode_packets(number: str):
    position = 0
    values = []
    packet_version_list = []

    while position < len(number) - 1:
        packet_version, value, position = packet(number=number, position=position)
        packet_version_list.append(packet_version)
        values.append(value)

        while position % 4 != 0 and position < len(number) - 1:
            position += 1

    return sum(packet_version_list), sum(values)


def packet(number: str, position: int) -> tuple:

    packet_version = ''
    for i in range(position, position + 3):
        packet_version += number[i]
    position += 3
    packet_version = int(packet_version, 2)

    packet_type = ''
    for i in range(position, position + 3):
        packet_type += number[i]
    position += 3
    packet_type = int(packet_type, 2)

    if packet_type != 4:
        length_type_ID = number[position]
        position += 1

        if length_type_ID == '0':
            length_subpackets = ''
            for i in range(position, position + 15):
                length_subpackets += number[i]
            position += 15

            length_subpackets = int(length_subpackets, 2)

            position_finished = position + length_subpackets

            packet_versions = [packet_version]

            literal_values = []
            while position < position_finished:
                packet_version_ret, value, position = packet(number=number, position=position)
                packet_versions.append(packet_version_ret)
                literal_values.append(value)

            return sum(packet_versions), sum(literal_values), position

        else:
            number_subpackets = ''
            for i in range(position, position + 11):
                number_subpackets += number[i]
            position += 11

            number_subpackets = int(number_subpackets, 2)

            literal_values = []

            packet_versions = [packet_version]

            for i in range(0, number_subpackets):
                packet_version_ret, value, position = packet(number=number, position=position)
                packet_versions.append(packet_version_ret)
                literal_values.append(value)

            return sum(packet_versions), sum(literal_values), position

    else:
        return literal_value(number=number, position=position, packet_version=packet_version)


def literal_value(number: str, position: int, packet_version: int) -> tuple:
    stop = 0
    literal_value = ''

    while stop == 0:
        part_literal_value = ''
        for i in range(position, position + 5):
            part_literal_value += number[i]

        position += 5
        if part_literal_value[0] == '0':
            stop = 1

        literal_value += part_literal_value[1:]

    literal_value_int = int(literal_value, 2)

    return packet_version, literal_value_int, position


numbers = parse_file(file_name='input.txt')

total_values = []

for i in numbers:
    total_values.append(decode_packets(i))

print(total_values)

