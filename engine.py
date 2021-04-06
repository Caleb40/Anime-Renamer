import os
from filename_fetcher import GetName
from web_crawler import scrape_wiki


def run(url, path):
    file_info = GetName(path)
    info = file_info.extract_numbers()
    anime_names = scrape_wiki(url)
    # print(anime_names)

    nums = list(info.keys())
    paths = list(info.values())

    old_paths = [os.path.join(path, i) for i in paths]
    for ext in old_paths:
        ext_ext = os.path.splitext(ext)[1]
        global new_names
        new_names = [str(j) + " " + anime_names[j - 1] + ext_ext for j in nums]
        global new_paths
        new_paths = [os.path.join(path, k) for k in new_names]
    print(f"""Renaming:
            {paths}
    To:
            {new_names}
        """)

    def prompt():
        ans = input("Proceed, enter (y or n): ")
        return ans
    while True:
        ask = prompt()
        if ask.lower() == "y":
            for n in zip(old_paths, new_paths):
                try:
                    os.rename(n[0], n[1])
                except FileExistsError:
                    continue
            print("Done!")
            break
        elif ask.lower() == "n":
            print("Exit!")
            break
        else:
            print("Invalid input")
            prompt()
