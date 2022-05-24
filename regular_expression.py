import re, pyperclip, pprint

message = 'yjytjyt 313-232-3823 tyjytyt'
message2 = 'djfndjs djsnfjkds batman bat bat'
bat_example = 'batwoman batman'
num_word = '12 dsfdsfds 82 dsfsdds 83 kdmfkdsmf 83 dfnkdfnjd'
student = 'student name: zeeshan id: 2747836 jfijdisojfsido id: 74987621'
student_list = ['student name: zeeshan id: 2747836 jfijdisojfsido id: 74987621'],

text = '''Chancellor of Jonesboro Dr. Tim Hudson870-972-3030870-972-3465Utimhudson@astate.eduU     CampusChief of 
StaffMs. Shawnie Carrier870-972-3030870-972-3465shawniecarrier@astate.eduUAssistant to the ChancellorMs. Sherry 
Johnson870-972-3030870-972-3465Usjohnson@astate.eduUProvost and Vice ChancellorDr. Lynita Cooksey870-972-2 030 
870-972-2036Ulcooksey@astate.eduVC for Finance and AdministrationDr. Len 
Frey870-972-3303870-972-3972Ulfrey@astate.eduUVC for University AdvancementDr. Jason 
Penry870-972-2060870-972-3684Ujpenry@astate.eduUVC for Student AffairsDr. Rick 
Stripling870-972-2048870-972-3002Uricks@astate.eduUDirector of Intercollegiate AthleticsMr. Terry Mohajir 
870-972-3882870-972-3886Utmohajir@astate.eduUAssociate VC for Academic Services Dr. Gina 
Hogue870-972-2030870-972-2036Ughogue@astate.eduUAssociate VC for BusinessDr. Russ 
Hannah870-972-3303870-972-3972Urhannah@astate.eduUand Finance Assistant VC Human ResourcesMs. Lori 
Winn870-972-3454870-972-3337Ulwinn@astate.eduUChief Information OfficerMr. Henry 
Torres870-972-3033870-972-3839Uhtorres@astate.eduUAssociate VC for Student AffairsDr. Lonnie Williams870-972-2048 
870-972-3002 Ulonniew@astate.eduUAssistant VC for Budget PlanningMs. Donna 
McMillin870-972-3700870-972-3818Umcmillin@astate.eduUand DevelopmentAssistant VC for Student AffairsDr. Craig 
Johnson870-972-2852870-972-3989Ucrjohnso@astate.eduUAssistant VC for Facilities Mr. Al 
Stoverink870-972-2066870-972-3691Uastoverink@astate.eduUManagementVice Provost for Research and Dr. Andrew 
Sustich870-972-2414870-972-3857Usustich@astate.eduUGraduate StudiesDean of Agri and TechnologyDr. Tim Burcham 
870-972-2085 870-972-3885tburcham@astate.eduDean of BusinessDr. Shane 
Hunt870-972-3035870-972-3744Ushunt@astate.eduUDean of Media and Communication   Dr. Brad 
Rawlins870-972-2468870-972-3856Ubrawlins@astate.edu9 07097237930 87097923530 87097923030 
zeeshan456@gmail.comzeeshan6546@gmail.com '''

emails = []
numbers = []


# this is a function for a regex that contains specific numerical string values
def NumberRegex(string):
    regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    var = regex.search(string)

    if var:
        print('match found: ' + var.group())

    else:
        print('no match found in this string: ' + string)


# this is a function for a regex contains bat followed by specific words
def WordRegex(string):
    regex = re.compile(r'bat(|man|woman|bat|animal)')
    match = regex.search(string)

    if match:
        print('correct pattern: ' + match.group())
    else:
        print('incorrect pattern for this string: ' + string)


# this is a function for a regex that contains man or woman
def MultipleWordsRegex(string):
    regex = re.compile(r'bat(man|woman|bat)')
    match = regex.findall(string)

    if match:
        print('correct pattern: ' + str(match))

    else:
        print('incorrect pattern - this is the string: ' + string)


def NumberWordRegex(string):
    regex = re.compile(r'\d+\s+\w+')
    match = regex.findall(string)

    if match:
        print('match found: ' + str(match))

    else:
        print('no match found - in this string: ' + string)


def SpecificAreaRegex(string):
    regex = re.compile(r'\w+:\s+\d\d\d\d\d\d\d')
    match = regex.findall(string)

    if match:
        print('match found: ' + str(match))

        # looping the match which returns a list
        for i in range(len(match)):
            print('index: ' + str(i) + ' values: ' + match[i] + ' length: ' + str(len(match[i])))

        # looping the match and converting it to a string then appending to a list
        for students in match:
            print(students)

    else:
        print('no match found - in this string: ' + string)


def Email_Regex(email):
    regex_email = re.compile(r'\w+@\w+.\w\w\w')
    match_email = regex_email.findall(email)

    if match_email:
        for i in range(len(match_email)):
            emails.append(match_email[i])

    else:
        print('no matches found')


def phone_number_regex(number):
    regex = re.compile(r'\d\d\d\d\d\d\d\d\d\d\d|\d\d\d-\d\d\d-\d\d\d\d')
    match = regex.findall(number)

    if match:
        for i in range(len(match)):
            numbers.append(match[i])

    else:
        print('no matches found')


Email_Regex(text)
print('')
phone_number_regex(text)


for email in emails:
    print(email)

for number in numbers:
    print(number)
