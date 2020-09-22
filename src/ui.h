#pragma once

#include <string.h>
#include <ncurses.h>

WINDOW* CreateTextBox (int height, int width, int posY, int posX, char* text);
WINDOW* CreateBox (int height, int width, int posY, int posX, char* text, bool selected);