key = [int(k) for k in input().split()]

key_idx = 0
results = []

text = input()
while text != "find":
    result = ""
    for character in text:
        if key_idx >= len(key):
            key_idx = 0
        result += chr(ord(character) - key[key_idx])
        key_idx += 1

    results.append(result)
    result, key_idx = "", 0
    text = input()

for location in results:
    material_start = location.index("&") + 1
    material_end = location.index("&", material_start + 1)
    coordinate_start = location.index("<") + 1
    coordinate_end = location.index(">")
    print(f"Found {location[material_start:material_end]} at {location[coordinate_start:coordinate_end]}")



# import re
#
# treasure_pattern = r"&([A-Za-z]+)&"
# location_pattern = r"<([A-Z0-9]+)>"
#
# key = [int(k) for k in input().split()]
# idx_of_keys = 0
# results = []
# while True:
#     result = ""
#     text = input()
#     if text == "find":
#         break
#     for character in text:
#         if idx_of_keys >= len(key):
#             idx_of_keys = 0
#         result += chr(ord(character) - key[idx_of_keys])
#         idx_of_keys += 1
#
#     results.append(result)
#     result = ""
#     idx_of_keys = 0
#
# for count, location in enumerate(results):
#
#     treasure_match = re.findall(treasure_pattern, results[count])
#     location_match = re.findall(location_pattern, results[count])
#     print(f"Found {treasure_match[0]} at {location_match[0]}")
