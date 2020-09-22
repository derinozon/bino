#pragma once

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#define ARRAY_SIZE(arr)     (sizeof(arr) / sizeof((arr)[0]))

char** str_split(char* a_str, const char a_delim);
char* ClearNL (char* text);
int ClampIndex (int index, int maxIndex);