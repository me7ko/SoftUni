def sorting_cheeses(**kwargs):
    result = ""
    sorted_dict = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    for key, value in sorted_dict:
        sorted_value = sorted(value, key=lambda x: -x)
        final = "\n".join([str(quantity) for quantity in sorted_value])
        result += key + "\n" + final + "\n"
    return result


print(
 sorting_cheeses(
 Parmesan=[102, 120, 135],
 Camembert=[100, 100, 105, 500, 430],
 Mozzarella=[50, 125],
 )
)