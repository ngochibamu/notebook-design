import datetime

last_id = 0

class Note:
	
	 ### Represent a note in the nodebook.
	 def __init__(self, memo, tags = ''):
	 	self.memo = memo
	 	self.tags = tags 
	 	self.creation_date = datetime.date.today()
	 	global last_id
	 	last_id += 1
	 	self.id = last_id

	 def match(self, filter):
	 	return filter in self.memo or filter in self.tags


class Notebook:
	### Represent a collection of notes that can be tagged, modfified,and searched

	def __init__(self):
		### Initialize a notebook with an empty list.
		self.notes = []

	def new_note(self, memo, tags=''):
		### Create a note and add it to the list
		self.notes.append(Note(memo, tags))

	def modify_memo(self, note_id, memo = ''):
		### Modify memo of node identified by note_id
		self._find_note(self, note_id).memo = memo

	def modify_tags(self, note_id, tags):
		### Find the note with the given id and change its tags to the give value
		self._find_note(self, note_id).tags = tags

	def search(self, filter):
		### Find all notes that match the given filter
		return [note for note in self.notes if note.match(filter)]

	def _find_note(self, note_id):
		### Locate the note with the given id...
		for note in self.notes:
			if note.id == note_id:
				return note

		return None
