
import datetime


def validateHour(hour: str):
  try:
    datetime.datetime.strptime(hour, '%H:%M').time()
    return 'valid'
  except:
    return 'not valid'
