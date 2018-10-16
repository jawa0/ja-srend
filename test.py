import struct


def draw_test_pattern():
	WIDTH = 800
	HEIGHT = 600
	SIDE = min(WIDTH, HEIGHT)
	radius = SIDE // 2
	cx = WIDTH // 2
	cy = HEIGHT // 2

	with open('test-image-float32-800x600.rgba', 'wb') as fout:
		for y in range(HEIGHT):
			for x in range(WIDTH):
				u = x - cx
				v = cy - y

				rgba = [0.0, 0.0, 0.0, 0.0]
				
				if v >= 0:
					rgba[0] = 1.0
				else:
					rgba[1] = 1.0

				if u >= 0:
					rgba[2] = 1.0

				if u*u + v*v < radius*radius:
					rgba[3] = 1.0
				else:
					rgba[3] = 0.0

				fout.write(struct.pack('f'*len(rgba), *rgba))



def main():
	draw_test_pattern()


if __name__=='__main__':
	main()
