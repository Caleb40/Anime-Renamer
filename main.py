from engine import run

url = input('Google search, "list of episodes (anime to be renamed), i.e "List of episodes black clover", click the '
            'wikipedia link (usually the 1st or 2nd result) then paste the url here:\n')
path = input('\nEnter the file path to the anime (note can\'t work on nested folders.: ')

if __name__ == '__main__':
    run(url, path)
