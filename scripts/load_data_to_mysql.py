import pandas as pd
from utils.mysql_tool import engine

path = './files/word_lesson_20220121.csv'
table = 'word_lesson'

path = './files/word_word_data.csv'
table = 'word_word'

path = './files/input/quiz_quiz_data.csv'
table = 'quiz_quiz'
df = pd.read_csv(path)
df.to_sql(table, engine, if_exists='append', index=False)
