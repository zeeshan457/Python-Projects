import sys, webbrowser, pyperclip, re


def search(search_in_google):
    try:
        # regex = re.compile(
        #     r'^https://\w{4,20}.(com|co.uk)$')  # https:// (word between 4 and 20 letters) (.com | .co.uk)
        # match = regex.findall(search_google)

        regex = re.compile(r'^[a-zA-Z1-9+/.*_@?%$£()&#-]+')
        match_search = regex.findall(search_in_google)

        if match_search:
            open_google = webbrowser.open('https://google.com/search?q=' + search_in_google)

        else:
            print('error: incorrect regex for search \n')

    except ValueError:
        print('not a correct search')


while True:
    search_input = input('Type here for google search: ')

    if search(str(search_input)):
        break

    else:
        continue
