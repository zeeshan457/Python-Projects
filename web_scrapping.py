import re, bs4, requests


# def GetPage(url):
#     res = requests.get(url)
#     res.raise_for_status()
#
#     Parse = bs4.BeautifulSoup(res.text, 'html.parser')
#     elements = Parse.select('body')
#     FirstElement = (elements[0].text.strip())
#     return FirstElement
#
#
# def FindPrice(page):
#     # £1,200 | £279.99 |
#     regex = re.compile(r'(£)(\d,\d\d\d|\d\d\d\d|\d\d\d.\d\d)')
#     match = regex.findall(page)
#
#     if match:
#         with open('prices.txt', 'w') as WritePrice:
#             for i in range(len(match)):
#                 data = 'index: ' + str(i) + ' match found: ' + str(match[i]) + ' length: ' + str(len(match[i]))
#                 WritePrice.write(data + '\n')
#
#     else:
#         print('no matches found')
#
#
# page = GetPage('https://www.ebay.co.uk/itm/303177104113?epid=28029464956&_trkparms=ispr%3D1&hash=item4696c37af1:g')
#
# page = ''.join([s for s in page.splitlines(True) if s.strip()])
# print(page + '\n')
# FindPrice(page)


def GetPage(StringUrl):
    res = requests.get(StringUrl)
    res.raise_for_status()

    parse = bs4.BeautifulSoup(res.text, 'html.parser')
    SelectElement = parse.select()
    element = (SelectElement[0].text.strip())
    return element


def FindNumbers(text):
    regex = re.compile()
    match = regex.findall(text)

    if match:
        print('')
    else:
        print('')


GetPage()
FindNumbers()
