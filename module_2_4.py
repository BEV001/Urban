#module_2_4

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primers, not_primers = [], []

for dividend in numbers:
    is_primer = True
    for divider in range(2, dividend):
        if dividend % divider == 0:
            is_primer = False
            break

    if dividend == 1:
        continue
    elif is_primer == True:
        primers.append(dividend)
    else:
        not_primers.append(dividend)

print("Primers: ", primers)
print("Not primers: ", not_primers)