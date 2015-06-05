from pandas import *


df= read_table('Cakile.compiled.data.txt')
f = open('Newbam1.js','w')
f.write('var Newworld = [\n')
for lat, long1, sci  in zip(df['latitude'], df['longitude'], df['verbatim_scientific_name']):
	temp = "[%s, %s, \"%s\"]," % (long1, lat, sci)
	f.write(temp + '\n')
f.write('];')

