from PIL import Image, ImageDraw

# These could be args if needed
WIDTH = 420 # px
STRIPE_HEIGHT = 40 # px

COLOURS = {
	'L': '#d52d00',
	'E': '#ef7627',
	'S': '#ff9a56',
	'B': '#ffffff',
	'I': '#d162a4',
	'A': '#b55690',
	'N': '#a30262',
}

def letter_to_colour(letter: str):
	if letter in COLOURS:
		return COLOURS[letter]
	else:
		raise ValueError(f'{letter} is not in {"".join(COLOURS.keys())}')

def phrase_to_letters(phrase: str):
	letters = [ letter for letter in phrase.upper() if letter.isalpha() ]
	if not letters:
		raise ValueError(f'There are no letters in "{phrase}"')
	return letters

def draw_flag(colours: list[str], width: int, stripe_height: int):
	height = len(colours) * stripe_height
	im = Image.new('RGB', (width, height))
	draw = ImageDraw.Draw(im)
	for (index, colour) in enumerate(colours):
		start_height = index * stripe_height
		top_left = (0, start_height)
		
		end_height = start_height + stripe_height
		bottom_right = (width, end_height)
		
		box = (top_left, bottom_right)
		draw.rectangle(box, fill = colour)
	return im

def phrase_to_flag(phrase: str):
	colours = [
		letter_to_colour(letter)
		for letter in phrase_to_letters(phrase)
	]
	return draw_flag(colours, WIDTH, STRIPE_HEIGHT)

def main():
	from os import path
	from sys import argv
	
	phrase = ' '.join(argv[1:]) or 'lesbian'
	flag = phrase_to_flag(phrase)
	
	fname = phrase.replace('/', '').replace('\\', '')
	fpath = path.join('examples', fname + '.png')
	flag.save(fpath)
	
	flag.show()

if __name__ == '__main__':
	main()
