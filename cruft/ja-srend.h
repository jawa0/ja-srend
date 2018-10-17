#pragma once


#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// really?
uint16_t min(uint16_t a, uint16_t b)
{
	return (a < b) ? a : b;
}


void draw_test_pattern()
{
	const uint16_t width = 800;
	const uint16_t height = 600;
	const uint16_t side = min(width, height);
	const uint16_t radius = side/2;
	const uint16_t cx = width / 2;
	const uint16_t cy = height / 2;
	
	FILE * fp = fopen("test-image-float32-800x600.rgba", "wb");
	if (!fp)
	{
		exit(-1);
	}

	float rgba[4];

	for (uint16_t y = 0; y < height; ++y)
	{
		for (uint16_t x = 0; x < width; ++x)
		{
			int16_t u = x - cx;
			int16_t v = cy - y;

			rgba[0] = 0.0f;
			rgba[1] = 0.0f;
			rgba[2] = 0.0f;
			rgba[3] = 0.0f;

			if (v >= 0) 
			{
				rgba[0] = 1.0f;				
			}
			else
			{
				rgba[1] = 1.0f;
			}

			if (u >= 0) 
			{
				rgba[2] = 1.0f;				
			}

			if (u*u + v*v < radius*radius)
			{
				rgba[3] = 1.0f;
			}
			else
			{
				rgba[3] = 0.0f;
			}

			fwrite(rgba, sizeof(float), 4, fp);
		}
	}

	fclose(fp); fp = 0;
}