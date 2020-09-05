import datetime
import time

_OFFSET = datetime.timedelta(hours=-3)
BUG_TZ = datetime.timezone(_OFFSET, "Africa/Buganda")

DAYS = ["Bbalaza", "Lwakubiri","Lwakusatu","Lwakuna","Lwakutaano","Lwamukaaga","Ssande"]
TRAD_MONTHS = [
        'Gatonnya',
        'Mukutulansanja',
        'Mugulansigo',
        'Kafuumuulampawu',
        'Muzigo',
        'Sseebaaseka',
        'Kasambula',
        'Muwakanya',
        'Mutunda',
        'Mukulukusa',
        'Museenene',
        'Ntenvu'
        ]

COMMON_MONTHS = [
        'Ogusooka',
        'Ogwokubiri',
        'Ogwokusatu',
        'Ogwokuna',
        'Ogwokutaano',
        'Ogwomukaaga',
        'Ogwomusanvu',
        'Ogwomunaana',
        'Ogwomwenda',
        'Ogwekkumi',
        'Ogwekkuminogumu',
        'Ogwekkuminebiri'
        ]

def lgtr_ctime(dt):
    '''
    Luganda traditional time in ctime
    e.g Ssa Muw 30 20:32:17 2020
    '''
    if dt.weekday() == 0 or dt.weekday() == 6:
        wday = DAYS[dt.weekday()][:3]
    else :
        wday = "Lw"+str(dt.weekday()+1)

    if dt.month == 2:
        month = 'Mkt'
    elif dt.month == 3:
        month = 'Mkl'
    else:
        month = TRAD_MONTHS[dt.month-1][:3]

    day = dt.day
    hour = str(dt.hour).zfill(2)
    minute = str(dt.minute).zfill(2)
    second = str(dt.second).zfill(2)
    year = dt.year

    return f'{wday} {month} {day} {hour}:{minute}:{second} {year}'

def lg_ctime(dt):
    '''
    Luganda common time in ctime
    e.g Lw3 Og2 30 20:32:17 2020
    '''
    
    if dt.weekday() == 0 or dt.weekday() == 6:
        wday = DAYS[dt.weekday()][:3]
    else:
        wday = "Lw"+str(dt.weekday()+1)

    month = "Og"+str(dt.month)
    day = dt.day
    hour = str(dt.hour).zfill(2)
    minute = str(dt.minute).zfill(2)
    second = str(dt.second).zfill(2)
    year = dt.year

    return f'{wday} {month} {day} {hour}:{minute}:{second} {year}'

def lg_strftime(dt):
    '''
    Translate datetime object to str in luganda
    '''
    pass

