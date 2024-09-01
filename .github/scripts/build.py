import datetime

with open('build.txt', 'w+') as f:
  f.write(f'{datetime.datetime.now()}')
