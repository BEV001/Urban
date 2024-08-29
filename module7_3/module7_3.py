class WordsFinder():
    def __init__(self, *files_name):
        self.files_name = list(files_name)

    def get_all_words(self):
        all_words = {}
        removing_sing = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for key in self.files_name:
            item = []
            with open(key, encoding='utf-8') as file:
                for line in file:
                    for sing in removing_sing:
                        line = line.replace(sing, ' ').lower()
                    item += line.split()
                all_words.update({key: item})
        return all_words

    def find(self, word):
        results_find = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                results_find.update({name: words.index(word.lower())+1})
            else:
                continue
        return results_find

    def count(self, word):
        results_count = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                counts = words.count(word.lower())
                results_count.update({name: counts})
            else:
                continue
        return results_count




if __name__ == "__main__":
    finder = WordsFinder('test_file.txt', 'Mother Goose - Monday’s Child.txt', 'Rudyard Kipling - If.txt', 'Walt Whitman - O Captain! My Captain!.txt')
    print(finder.get_all_words())
    print(finder.find('the'))
    print(finder.count('THE'))
