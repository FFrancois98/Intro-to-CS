birth_month = input('Enter birth month: ')
birth_day = int(input('Enter birth day: '))
birth_month = birth_month.lower()

def GetZodiacSign(birth_month, birth_day):
    if birth_month == 'march':
        if birth_day <= 20:
            zodiac = 'pisces'
        if 21 <= birth_day <= 31:
            zodiac = 'aries'
    if birth_month == 'april':
        if birth_day <= 19:
            zodiac = 'aries'
        if 20 <= birth_day <= 30:
            zodiac = 'taurus'
    if birth_month == 'may':
        if birth_day <= 20:
            zodiac = 'taurus'
        if 21 <= birth_day <= 31:
            zodiac = 'gemini'
    if birth_month == 'june':
        if birth_day <= 20:
            zodiac = 'gemini'
        if 21 <= birth_day <= 30:
            zodiac = 'cancer'
    if birth_month == 'july':
        if birth_day <= 22:
            zodiac = 'cancer'
        if 23 <= birth_day <= 31:
            zodiac = 'leo'
    if birth_month == 'august':
        if birth_day <= 22:
            zodiac = 'leo'
        if 23 <= birth_day <= 31:
            zodiac = 'virgo'
    if birth_month == 'september':
        if birth_day <= 22:
            zodiac = 'virgo'
        if 23 <= birth_day < 30:
            zodiac = 'libra'
    if birth_month == 'october':
        if birth_day <= 22:
            zodiac = 'libra'
        if 23 <= birth_day <=31:
            zodiac = 'scorpio'
    if birth_month == 'november':
        if birth_day <= 21:
            zodiac = 'scorpio'
        if 22 <= birth_day <= 30:
            zodiac = 'sagittarius'
    if birth_month == 'december':
        if birth_day <= 21:
            zodiac = 'sagittarius'
        if 22 <= birth_day < 31:
            zodiac = 'capricorn'
    if birth_month == 'january':
        if birth_day <= 19:
            zodiac = 'capricorn'
        if 20 <= birth_day <= 31:
            zodiac = 'aquarius'
    if birth_month == 'february':
        if birth_day <= 18:
            zodiac = 'aquarius'
        if 19 <= birth_day <= 28:
            zodiac = 'pisces'
    return zodiac

zo_sign = GetZodiacSign(birth_month, birth_day)
print(zo_sign)
