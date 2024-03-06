from advent.runner import register
from functools import reduce
import operator

def process_packet(binary_string, version_sum):
    version = int(binary_string[:3], 2)
    version_sum += version
    type_id = int(binary_string[3:6], 2)

    if type_id == 4:
        start_packet = 6
        bits = []
        bit_counter = 0
        last_packet = False
        while not last_packet:
            if binary_string[start_packet + bit_counter] == "0":
                last_packet = True
            bits.append(binary_string[start_packet + bit_counter + 1: start_packet + bit_counter + 5])
            bit_counter += 5

        end_is_padding = True
        for char in binary_string[start_packet + bit_counter:]:
            if char != "0":
                end_is_padding = False
                break
        
        if end_is_padding:
            return int(''.join(bits), 2), "", version_sum
        return int(''.join(bits), 2), binary_string[start_packet + bit_counter:], version_sum
    else:
        length_type = binary_string[6]
        if length_type == "0":
            length = int(binary_string[7:7 + 15], 2)

            sub_packets = []

            sub_string = binary_string[7 + 15: 7 + 15 + length] 

            while len(sub_string) > 0:  
                sub_packet, sub_string, version_sum = process_packet(sub_string, version_sum)

                sub_packets.append(sub_packet)
            
            end_is_padding = True
            for char in binary_string[7 + 15 + length:]:
                if char != "0":
                    end_is_padding = False
                    break
            
            if end_is_padding:
                binary_string = ""
            else:
                binary_string = binary_string[7 + 15 + length:]
        else:
            length = int(binary_string[7:7 + 11], 2)

            sub_packets = []

            binary_string = binary_string[7 + 11:] 

            while len(sub_packets) < length:  
                sub_packet, binary_string, version_sum = process_packet(binary_string, version_sum)

                sub_packets.append(sub_packet)
            
            end_is_padding = True
            for char in binary_string:
                if char != "0":
                    end_is_padding = False
                    break
            
            if end_is_padding:
                binary_string = ""

        value = 0
        print(type_id)
        match type_id:
            case 0:
                value = sum(sub_packets)
            case 1:
                value = reduce(operator.mul, sub_packets)           
            case 2:
                value = reduce(min, sub_packets)      
            case 3:
                value = reduce(max, sub_packets)      
            case 5:
                if len(sub_packets) != 2:
                    raise Exception("Invalid length")
                
                if sub_packets[0] > sub_packets[1]:
                    value = 1
                else:
                    value = 0
            case 6:
                if len(sub_packets) != 2:
                    raise Exception("Invalid length")
                
                if sub_packets[0] < sub_packets[1]:
                    value = 1
                else:
                    value = 0
            case 7:
                if len(sub_packets) != 2:
                    raise Exception("Invalid length")
                
                if sub_packets[0] == sub_packets[1]:
                    value = 1
                else:
                    value = 0
            case _ :
                raise Exception("Invalid type")

        return value, binary_string, version_sum              
        


def initial_process(text):
    return format(int(text, 16), "b")

@register(16, 2021, 1)
def packet_decoder_1(text):
    binary_string = initial_process(text)

    version_sum = 0

    while len(binary_string) > 0:  
        value, binary_string, version_sum = process_packet(binary_string, version_sum)

    return version_sum

@register(16, 2021, 2)
def packet_decoder_2(text):
    binary_string = initial_process(text)

    version_sum = 0

    while len(binary_string) > 0:  
        value, binary_string, version_sum = process_packet(binary_string, version_sum)

    return value