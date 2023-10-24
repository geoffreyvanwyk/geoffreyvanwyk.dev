SITENAME = "Geoffrey van Wyk"
SITESUBTITLE = "Computer Programmer"
SITEURL = ""
AUTHOR = "Geoffrey Bernardo van Wyk"

DEFAULT_LANG = "en"
TIMEZONE = "Africa/Johannesburg"

PATH = "content"

THEME = "windy"
MENUITEMS = [("Home", "/")]
DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = 10

from datetime import datetime

YEAR = datetime.now().strftime("%Y")

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = [
    {
        "page": "About",
        "image": "https://m.media-amazon.com/images/I/31F7DqnXj2L._SX342_SY445_.jpg",
        "link": "https://www.amazon.com/PHP-MySQL-Server-side-Web-Development/dp/1119149223/ref=sr_1_5?crid=2ES77QDQ2G2B4&amp;keywords=PHP&amp;qid=1698165441&amp;sprefix=php%252Caps%252C395&amp;sr=8-5&_encoding=UTF8&tag=geoffreyvanwy-20&linkCode=ur2&linkId=7ac40f22638cb5ff73b3ddfab712e9dc&camp=1789&creative=9325",
        "title": "PHP & MySQL: Server-side Web Development",
    },
    {
        "page": "About",
        "image": "https://m.media-amazon.com/images/I/61Sa4KP+2dL._SY466_.jpg",
        "link": "https://www.amazon.com/Moodle-Learning-Course-Development-instructional/dp/180107903X/ref=sr_1_1?crid=2UUMOAPCSZG6G&amp;keywords=moodle&amp;qid=1698165650&amp;sprefix=mood%252Caps%252C386&amp;sr=8-1&_encoding=UTF8&tag=geoffreyvanwy-20&linkCode=ur2&linkId=ac1935e49f41aece4933b098f5f29671&camp=1789&creative=9325",
        "title": "Moodle 4 E-Learning Course Development",
    },
    {
        "page": "About",
        "image": "https://m.media-amazon.com/images/I/81xqW9qnF0L._SY466_.jpg",
        "link": "https://www.amazon.com/FORTRAN-SCIENTISTS-ENGINEERS-Stephen-Chapman/dp/0073385891/ref=sr_1_4?crid=12OU4QB598H4B&amp;keywords=fortran&amp;qid=1698160040&amp;sprefix=fortran%252Caps%252C552&amp;sr=8-4&_encoding=UTF8&tag=geoffreyvanwy-20&linkCode=ur2&linkId=631d6dc95c0e522a442eeabd3f752b4e&camp=1789&creative=9325",
        "title": "Fortran for Scientists and Engineers",
    },
    {
        "page": "About",
        "image": "https://m.media-amazon.com/images/I/61svjW8j07L._SY466_.jpg",
        "link": "https://www.amazon.com/Excel-2019-Power-Programming-VBA/dp/1119514924/ref=sr_1_3?crid=2DAYXXMJ07CNM&amp;keywords=excel+power+programming+with+vba&amp;qid=1698164260&amp;sprefix=excel+power+programming+with+vba%252Caps%252C388&amp;sr=8-3&_encoding=UTF8&tag=geoffreyvanwy-20&linkCode=ur2&linkId=f1a72b3eda74acd8db59acc0b71f9701&camp=1789&creative=9325",
        "title": "Excel 2019 Power Programming with VBA",
    },
    {
        "page": "About",
        "image": "https://m.media-amazon.com/images/I/917mjITnNoL._SY466_.jpg",
        "link": "https://www.amazon.com/Learning-Visual-Basic-Jesse-Liberty/dp/0596003862/ref=sr_1_2?crid=2H6C172SLZMPS&amp;keywords=visual+basic+.net&amp;qid=1698165000&amp;sprefix=visual+basic+.n%252Caps%252C453&amp;sr=8-2&_encoding=UTF8&tag=geoffreyvanwy-20&linkCode=ur2&linkId=54529950832f3f67cf2177f12b6dc27e&camp=1789&creative=9325",
        "title": "Learning Visual Basic .Net",
    },
    {
        "page": "About",
        "image": "https://m.media-amazon.com/images/I/51CxdWNJ+OL._SY445_SX342_.jpg",
        "link": "https://www.amazon.com/Think-Python-Like-Computer-Scientist/dp/1491939362/ref=sr_1_1?crid=3JDQ258WUIZZQ&amp;keywords=think+python+how+to+think+like+a+computer+scientist&amp;qid=1698165277&amp;sprefix=think+python%252Caps%252C551&amp;sr=8-1&_encoding=UTF8&tag=geoffreyvanwy-20&linkCode=ur2&linkId=9245829fde9a4887527648e9c7c34ee2&camp=1789&creative=9325",
        "title": "Think Python",
    },
]

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
