#dictionary

"""
dictionary with history tracker 
current features
1. in memory history tracker
"""
import logging
import sqlite3 as sqlite


class word_dictionary:

	db_filename = 'dictionary.db'
	
	def __init__(self):
		self.cached = {}
		self.history =[]
		self.setup_db()
		logging.basicConfig(level=logging.INFO)

	def setup_db(self):
		try:
			self.db_connection=sqlite.connect(self.db_filename)
			logging.debug('connected to database')
		except Exception as ex:
			logging.error('error connecting to database')
			print("error connecting to database")

	def validate(self,word=None):
		if word is None or len(word)<1:
			raise Exception("invalid word")

	def lookup_word(self,word):
		try:
			return tuple(word,self.cached[word])
		except Exception as ex:
			logging.debug("cache miss")
			return self.lookup_database(word)	

	def lookup_database(self,word):
		cursor = self.db_connection.cursor()
		cursor.execute(self.get_query_for_word(word))
		result = cursor.fetchall()
		cursor.close()
		logging.debug("for word {}, found {} records".format(word,len(result)))
		self.cached[word]=result
		return result


	def get_query_for_word(self,word):
		temp ='select * from {} where word like "{}";'
		return temp.format(word[0],word)


dict = word_dictionary()

while True:
	word:str = input('\nenter word to lookup!\n')
	result_list = dict.lookup_word(word)
	index =1 
	for i in result_list:
		print("{}::{}".format(index,i[1]))
		index += 1
	


