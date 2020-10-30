import time
from time import ctime
from datetime import datetime

captured_time = datetime.fromtimestamp(1585650864175.47998046875/1000)
current_time = datetime.fromtimestamp(time.time())
diff_time = current_time - captured_time
print(captured_time)
print(current_time)
print(str(diff_time).split(":")[0])