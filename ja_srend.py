import array
import struct


class PixelBuffer(object):
	"""Rectangular array of pixels. Format is RGBA, and each component is a float (32 bit)."""
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.buffer = array.array('f', [0.0] * (width * height * 4))

	def get_pixel(x, y):
		pass
		
	def set_pixel(self, x, y, r, g, b, a):
		"""Set the red, green, blue, and alpha components of the pixel at location (x, y).
		The top-left pixel of the buffer has x-y coordinate (0, 0), and the bottom-right is
		at (width-1, height-1)."""
		
		i = 4 * (y * self.width + x)
		self.buffer[i : i + 4] = array.array('f', struct.pack('ffff', r, g, b, a))

	def to_bytes(self):
		"""Return a string of bytes suitable for output as a binary file or stream. Pixels are output
		row by row, from top-left to bottom-right. For each pixel, components are output in RGBA order."""
		return self.buffer.tobytes();



def draw_test_pattern():
	WIDTH = 800
	HEIGHT = 600
	SIDE = min(WIDTH, HEIGHT)
	radius = SIDE // 2
	cx = WIDTH // 2
	cy = HEIGHT // 2

	s = PixelBuffer(WIDTH, HEIGHT)

	with open('test-image-float32-800x600.rgba', 'wb') as fout:
		for y in range(HEIGHT):
			for x in range(WIDTH):
				u = x - cx
				v = cy - y

				rgba = [0.0, 0.0, 0.0, 0.0]

				# Set the four quadrants of the image to different colours.
				if v >= 0:
					rgba[0] = 1.0
				else:
					rgba[1] = 1.0

				if u >= 0:
					rgba[2] = 1.0

				# Make a centred circle opaque, and the borders transparent.
				if u*u + v*v < radius*radius:
					rgba[3] = 1.0
				else:
					rgba[3] = 0.0

				s.set_pixel(x, y, rgba[0], rgba[1], rgba[2], rgba[3])

		fout.write(s.to_bytes())


