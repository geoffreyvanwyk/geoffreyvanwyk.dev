SITENAME = "Geoffrey van Wyk"
SITESUBTITLE = "Computer Programmer"
SITEURL = ""
AUTHOR = "Geoffrey Bernardo van Wyk"

DEFAULT_LANG = "en"
TIMEZONE = "Africa/Johannesburg"

PATH = "content"
ARTICLE_PATH = ["articles"]
STATIC_PATHS = ["images", "extra"]
EXTRA_PATH_METADATA = {
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/CNAME": {"path": "CNAME"},
    "extra/logo.jpg": {"path": "logo.jpg"},
}

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {},
    },
    "output_format": "html5",
}

THEME = "./themes/windy"
MENUITEMS = [("Home", "/")]
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_PAGINATION = 10
FONT_AWESOME_KIT = "4e9b15fd57"

from datetime import datetime

YEAR = datetime.now().strftime("%Y")


# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
