#pragma once

#include <string>
#include <sstream>
#include <vector>
#include <iterator>
#include <algorithm>
#include <functional>
#include <cctype>
#include <locale>

using namespace std;

template<typename Out>
void split(const string &s, char delim, Out result);

vector<string> split(const string &s, char delim);

string &ltrim(string &s);
string &rtrim(string &s);
string &trim(string &s);
