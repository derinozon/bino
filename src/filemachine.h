#ifndef FILEMACHINE_H
#define FILEMACHINE_H

void Test();
bool DirectoryExists (char* path);
char* ReadFile (char* path);
void WriteFile (char* path, char* content);
char* ListDirectory (char* path, bool showHidden);
#endif