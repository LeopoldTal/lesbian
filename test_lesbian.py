import pytest
from lesbian import letter_to_colour, phrase_to_letters, draw_flag

class TestColour:
	def test_exists(self):
		assert letter_to_colour('N') == '#a30262'
		assert letter_to_colour('B') == '#ffffff'
	
	def test_not_exists(self):
		with pytest.raises(ValueError):
			letter_to_colour('X')

@pytest.mark.parametrize('phrase, expected', [
	('', []),
	('alien', ['A', 'L', 'I', 'E', 'N']),
	("Lil' Nas!", ['L', 'I', 'L', 'N', 'A', 'S']),
	("BEN10", ['B', 'E', 'N']),
])
def test_phrase(phrase, expected):
	assert phrase_to_letters(phrase) == expected

def test_phrase():
	with pytest.raises(ValueError):
		phrase_to_letters('@_42')

def test_draw_flag():
	colours = ['#ff0000', '#00ff00', '#0000ff']
	im = draw_flag(colours, 4, 2)
	assert im.size == (4, 6)
	px = im.load()
	for x in range(4):
		assert px[x,0] == (255, 0, 0)
		assert px[x,1] == (255, 0, 0)
		assert px[x,2] == (0, 255, 0)
		assert px[x,3] == (0, 255, 0)
		assert px[x,4] == (0, 0, 255)
		assert px[x,5] == (0, 0, 255)
