import calendar
from datetime import datetime

yy = datetime.now().year
mm = datetime.now().month


print("\n" + calendar.month(yy, mm))
