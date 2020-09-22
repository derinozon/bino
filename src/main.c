#include "main.h"

int main (int argc, char** argv) {
	initscr();
	noecho();
	cbreak();
	curs_set(0);

	getmaxyx(stdscr, yMax, xMax);

	MainMenuSel();
	return 0;
}

void MainMenuSel () {
	int choice = MainMenu();
	if (choice == -1) return;
	if (choice == 0) {
		choice = SelectionMenu();
		if (choice == -1) {
			MainMenuSel();
		}
		if (choice == 0) {
			system("cd ./software/SearchCLI/ && python3 searchcli.py google");
		}
		if (choice == 1) {
			system("cd ./software/SearchCLI/ && python3 searchcli.py stack");
		}
		if (choice == 1) {
			system("cd ./software/Cipher/ && python3 cipher.py");
		}
	}
	if (choice == 1) {
		InfoMenu();
		MainMenuSel();
	}
}

void InfoMenu () {
	int height = yMax-2;
	int width = xMax-2;
	
	WINDOW* txtbox = CreateTextBox(height, width, 0, 0, ClearNL(ReadFile("./res/info.md")));
	wgetch(txtbox);

	werase(txtbox);
	wrefresh(txtbox);
}

int SelectionMenu () {
	int height = yMax-2;
	int width = xMax;

	WINDOW* win = newwin(height, width/2, 0, 0);
	box(win, 0, 0);

	refresh();
	wrefresh(win);
	keypad(win, true);

	char* arr[] = {
		"AskGoogle",
		"AskStackOverflow",
		"Encoder"
	};

	char* txt[] = {
		ReadFile("./software/SearchCLI/README.md"),
		ReadFile("./software/SearchCLI/README.md"),
		ReadFile("./software/Cipher/README.md")
	};

	int arrlen = ARRAY_SIZE(arr);
	
	int key;
	int choice = 0;

	while (1) {

		WINDOW* txtbox = CreateTextBox(height, width/2, 0, width/2, ClearNL(txt[choice]));
		
		for (int i = 0; i < arrlen; i++) {
			bool selected = i == choice;

			if (selected) wattron(win, A_REVERSE);
			
			mvwprintw(win, i+1, 1, arr[i]);
			wattroff(win, A_REVERSE);
			
			wrefresh(win);
			refresh();
		}
		
		key = wgetch(win);

		if (key == KEY_UP) choice--;
		if (key == KEY_DOWN) choice++;
		if (key == 10) break;
		if (key == KEY_BACKSPACE||key == 127) {
			werase(win);
			wrefresh(win);
			werase(txtbox);
			wrefresh(txtbox);
			return -1;
		};

		choice = ClampIndex(choice, arrlen);
	}
	endwin();
	return choice;
}

int MainMenu () {
	int BoxH = yMax/2;
	int BoxW = yMax;
	int margin = 2;

	WINDOW* arr[3];

	int key;
	int choice = 0;

	char* headers[] = {
		"Software", "Info", "Exit"
	};
	

	int arrlen = ARRAY_SIZE(headers);
	while (1) {
		for (int i = 0; i < arrlen; i++) {
			bool selected = i == choice;
			arr[i] = CreateBox(BoxH, BoxW, margin, margin+BoxW*i, headers[i], selected);
			
			wrefresh(arr[i]);
			refresh();
		}
		
		key = wgetch(arr[0]);

		if (key == KEY_LEFT) choice--;
		if (key == KEY_RIGHT) choice++;
		if (key == 10) break;
		if (key == KEY_BACKSPACE||key == 127) {
			endwin();
			return -1;
		};

		choice = ClampIndex(choice, arrlen);
	}

	
	for (int i = 0; i < arrlen; i++) {
		werase(arr[i]);
	}
	endwin();
	return choice;
}