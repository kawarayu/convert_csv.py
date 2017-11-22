import pandas as pd
import numpy as np
from datetime import datetime
day = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
input_file = 'user.csv'
output_file = day + '_user.csv'
c1 = ['ログイン名', '名前']
c2 = ['login_name', 'name']
#df = pd.read_csv(input_file, encoding='utf-8')
with codecs.open(input_file, 'r', 'shift-jis', 'ignore') as f:
  df = pd.read_table(f, delimiter=',')
# ENCODING = 'cp932'
df2 = df.loc[:, c1]
df2.columns = c2
df2.to_csv(output_file, encoding='utf-8', index=False)
