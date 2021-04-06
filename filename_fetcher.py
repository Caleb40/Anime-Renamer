import os
import re


class GetName:
    def __init__(self, filepath):
        files = os.walk(filepath)
        self.ext = []
        for path, directory, file in files:
            for i in file:
                self.ext.append(i)

    def extract_numbers(self):
        number_re = re.compile(r'((\d\d?\d?)|(\d\.?\d?\.?\d?))')
        a = []
        for x in self.ext:
            match = number_re.search(x)
            res = match.group(1)
            a.append(int(res))
        matches = dict(zip(a, self.ext))
        return matches


new = GetName("F:\Anime\Angel Beats")
new.extract_numbers()
