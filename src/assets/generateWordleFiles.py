import sqlite3
import json
import os

conn = sqlite3.connect('db-2021-11-12.sqlite')
cursor = conn.cursor()
cursor.execute('select upper(notone_romanization) from pengim, definition where pengim.definition_id = definition.id and length(notone_romanization) == 6')
results = cursor.fetchall()

result_array = [row[0] for row in results]

if not os.path.exists('json'):
    os.makedirs('json')

file_name = 'json/drawable-words.json'
with open(file_name, 'w') as file:
    json.dump(result_array, file)

file_name = 'json/playable-words.json'
with open(file_name, 'w') as file:
    json.dump(result_array, file)

cursor.execute('select upper(notone_romanization), chinese_char from pengim, definition where pengim.definition_id = definition.id and length(notone_romanization) == 6')
results = cursor.fetchall()

file_name = 'chinese.js'

with open(file_name, 'w') as file:
	file.write("export const map = new Map();\n")
	for row in results:
		formatted_row = "map.set('{0}', '{1}');\n".format(row[0], row[1].replace("'", "\\'"))
		file.write(formatted_row)

cursor.execute('select upper(notone_romanization), def_en from pengim, definition where pengim.definition_id = definition.id and length(notone_romanization) == 6')
results = cursor.fetchall()
conn.close()

file_name = 'definitions.js'

with open(file_name, 'w') as file:
	file.write("export const map = new Map();\n")
	for row in results:
		formatted_row = "map.set('{0}', '{1}');\n".format(row[0], row[1].replace("'", "\\'"))
		file.write(formatted_row)


