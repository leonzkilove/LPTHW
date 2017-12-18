class Song(object):
	def __init__(self,lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			print "\n"

hundred_day_song = Song(["Hundred days have made me colder","When I last saw your face","Beautiful girl I always wanted you this way"])

jack_and_jill = Song(["Jack and jill","Went up the hill","To fetch a pail of water"])

hundred_day_song.sing_me_a_song()
jack_and_jill.sing_me_a_song()
