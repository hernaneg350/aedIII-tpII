#include <vector>
#include "util.h"

#include "InputReader.h"
#include "InstanceReader.h"

using namespace TPII;
using namespace std;

vector<Graph> InputReader::ReadFromInput(istream& inputStream)
{
    vector<Graph> instances;

    bool keepReading = true;
    while (keepReading)
    {
        string instanceSizeString;
        getline(inputStream, instanceSizeString);

        vector<string> instanceSize = split(instanceSizeString, ' ');

        int n = stoi(trim(instanceSize[0]));

        if (n == -1)
        {
            keepReading = false;
            break;
        }

        int m = stoi(trim(instanceSize[1]));

        InstanceReader instanceReader;
        Graph instance = instanceReader.ReadFromInput(n, m, inputStream);
        instances.push_back(instance);
    }

    return instances;
}
