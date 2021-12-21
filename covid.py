# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available
• `{i}covid country name`
    Gets the Covid-19 Status of a given Country.
"""

from covid import Covid

from . import *


@ultroid_cmd(pattern="covid")
async def coronish(event):
    covid = Covid()
    text = event.text
    okie = text.split(" ", maxsplit=1)
    try:
        country = okie[1]
    except IndexError:
        await eor(event, "Give a country name to Search for it's Covid Cases!")
        return
    try:
        cases = covid.get_status_by_country_name((country).lower())
        act = cases["active"]
        conf = cases["confirmed"]
        dec = cases["deaths"]
        rec = cases["recovered"]
        await eor(
            event,
            f"**Country:** **{country.capitalize()}**\n**Active:** {act}\n**Confirmed:** {conf}\n**Recovered:** {rec}\n**Deceased:** {dec}",
        )
    except ValueError:
        await eor(event, f"It seems that Country {country} is invalid!")
