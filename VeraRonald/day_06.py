def add_subroutine(file):
    try:
        with open(file, 'r') as file:
            lines  = file.readlines()
            characters = lines[-1].strip()
            datastream_for_packets = characters[::]
            datastream_for_messages = characters[::]
            communication_system = {
                "packets":[],
                "messages": [],
            }
            while len(datastream_for_packets) != 0 or len(datastream_for_messages) != 0:
                if len(datastream_for_packets) != 0:
                    marker_packet = getMarkerPacket(datastream_for_packets)
                    index_marker_packet = characters.index(marker_packet)
                    characters_before_marker_packet = datastream_for_packets[:index_marker_packet]

                    communication_system["packets"].append({"previous_characters":characters_before_marker_packet, "marker":marker_packet})

                    datastream_for_packets = datastream_for_packets[index_marker_packet + len(marker_packet):]

                if len(datastream_for_messages) != 0:
                    marker_message = getMarkerMessage(datastream_for_messages)
                    index_marker_message = characters.index(marker_message)
                    characters_before_marker_message = datastream_for_messages[:index_marker_message]

                    communication_system["messages"].append({"previous_characters":characters_before_marker_message, "marker":marker_message})

                    datastream_for_messages = datastream_for_messages[index_marker_message + len(marker_message):]

            return communication_system
    except FileNotFoundError:
        print('File not found')

def getMarkerPacket(datastream):
    marker = []
    for character in datastream:
        if character not in marker:
            marker.append(character)
            if len(marker) == 4:
                break
        else:
            marker = marker[marker.index(character)+1:]
            marker.append(character)
    return "".join(marker)

def getMarkerMessage(datastream):
    marker = []
    for character in datastream:
        if character not in marker:
            marker.append(character)
            if len(marker) == 14:
                break
        else:
            marker = marker[marker.index(character)+1:]
            marker.append(character)
    return "".join(marker)

# PART 1
characters_detected_before_first_marker = len("".join(list(add_subroutine("input.txt")["packets"][0].values())))
print(characters_detected_before_first_marker)
# PART 2
characters_detected_before_first_message = len("".join(list(add_subroutine("input.txt")["messages"][0].values())))
print(characters_detected_before_first_message)