# Ultroid Userbot
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -

• `{i}apod``
    Get Astronomy Picture of Day by NASA
"""

import requests as r
from bs4 import BeautifulSoup as bs

from . import *


@ultroid_cmd(pattern="apod$")
async def aposj(e):
    link = "https://apod.nasa.gov/apod/"
    C = r.get(link).content
    m = bs(C, "html.parser", from_encoding="utf-8")
    try:
        try:
            img = m.find_all("img")[0]["src"]
            img = link + img
        except IndexError:
            img = None
        expla = m.find_all("p")[2].text.replace("\n", " ")
        expla = expla.split("     ")[0]
        if len(expla) > 3000:
            expla = expla[:3000] + "..."
        expla = "__" + expla + "__"
        await e.reply(expla, file=img)
        if e.out:
            await e.delete()
    except Exception as E:
        return await eod(e, str(E))
