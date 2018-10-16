#pragma once


#include <stdint.h>

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
}