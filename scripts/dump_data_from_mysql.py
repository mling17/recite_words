import pandas as pd
from utils.mysql_tool import engine

sql = ''' select * from word_words; '''
sql = ''' select * from word_lesson; '''
sql = ''' select * from word_word; '''
df = pd.read_sql_query(sql, engine)
df.to_csv('./files/word_word_template.csv', index=False)
print('Completed!')
