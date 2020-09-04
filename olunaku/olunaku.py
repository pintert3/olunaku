import datetime
import time

today = datetime.datetime.now()
OFFSET = datetime.timedelta(hours=-3)
BUG = datetime.timezone(OFFSET, "Africa/Buganda")

leero = datetime.datetime.now(BUG)

print(leero) # DEBUG


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
    e.g Sun Aug 30 20:32:17 2020
    '''
    if dt.weekday() == 0 or dt.weekday() == 6:
        wday = DAYS[dt.weekday()][:3]
    else :
        wday = "Lw"+str(dt.weekday()+1)
    month = TRAD_MONTHS[dt.month-1][:3]
    day = dt.day
    hour = str(dt.hour).zfill(2)
    minute = dt.minute
    second = dt.second
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
    minute = dt.minute
    second = dt.second
    year = dt.year

    return f'{wday} {month} {day} {hour}:{minute}:{second} {year}'

randomday = datetime.datetime.now()+datetime.timedelta(3)

print(lgtr_ctime(leero))
print(lgtr_ctime(today))
print(lgtr_ctime(randomday))
print('')
print(lg_ctime(leero))
print(lg_ctime(today))
print(lg_ctime(randomday))
