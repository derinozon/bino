#include "ui.h"

WINDOW* CreateTextBox (int height, int width, int posY, int posX, char* text) {
	WINDOW* win = newwin(height, width, posY, posX);
	box(win, 0, 0);

	int xi, yi;
	xi = 1; yi = 1;

	for (int i = 0; i < strlen(text); i++) {
		mvwaddch(win, yi, xi, text[i]);
		xi++;
		if (xi >= width-2) {
			xi=1;
			yi++;
		}
		if (yi >= height-1) {
			break;
		}
	}

	refresh();
	wrefresh(win);
	return win;
}

WINDOW* CreateBox (int height, int width, int posY, int posX, char* text, bool selected) {
	WINDOW* win = newwin(height, width, posY, posX);
	box(win, 0, 0);

	if (selected) wattron(win, A_REVERSE);
	mvwprintw(win, height/2, (width/2) - (strlen(text)/2), text);
	wattroff(win, A_REVERSE);

	refresh();
	wrefresh(win);
	keypad(win, true);
	return win;
}