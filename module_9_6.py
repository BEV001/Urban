def all_variants(text):

    stop_i = 1
    while stop_i <= len(text):
        start_i = 0
        while start_i+stop_i <= len(text):
            element = text[start_i:start_i+stop_i]
            yield element
            start_i += 1
        stop_i += 1

a = all_variants('abcd')
for i in a:
    print(i)
