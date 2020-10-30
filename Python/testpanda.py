import pandas as pd

from_url = pd.read_table("http://touchstone.conviva.com/ui?client=2943402.2293828.1786993.12345695&session=1438110720&pub=0&before=1462290200.8481",
                         sep= "\t")
print from_url.head(10)