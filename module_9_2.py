first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(word) for word in first_strings if len(word) >= 5]
print(first_result)

second_result = [(word_1, word_2) for word_1 in first_strings for word_2 in second_strings if
                 len(word_1) == len(word_2)]
print(second_result)

third_result = {word: len(word) for word in first_strings + second_strings if len(word) % 2 == 0}
print(third_result)
