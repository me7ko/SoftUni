first_line = input().split(", ")
beggar_count = int(input())

beggars_list = [0] * beggar_count

for idx in range(len(first_line)):
    beggars_idx = idx % beggar_count
    num = int(first_line[idx])
    beggars_list[beggars_idx] += num
    
print(beggars_list)