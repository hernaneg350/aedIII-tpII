#include "util.h"

using namespace std;

template<typename Out>
void split(const string &s, char delim, Out result) {
    stringstream stringStream;
    stringStream.str(s);
    string item;
    while (std::getline(stringStream, item, delim)) {
        *(result++) = item;
    }
}

vector<string> split(const string &s, char delim) {
    vector<string> elems;
    split(s, delim, back_inserter(elems));
    return elems;
}

string &ltrim(string &s) {
    s.erase(s.begin(), find_if(s.begin(), s.end(),
            not1(ptr_fun<int, int>(isspace))));
    return s;
}

string &rtrim(string &s) {
    s.erase(find_if(s.rbegin(), s.rend(),
            not1(ptr_fun<int, int>(isspace))).base(), s.end());
    return s;
}

string &trim(string &s) {
    return ltrim(rtrim(s));
}
