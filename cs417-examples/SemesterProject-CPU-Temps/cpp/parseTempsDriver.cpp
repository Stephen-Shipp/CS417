#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <list>
#include <utility>

#include "parseTemps.h"

using namespace std;

//------------------------------------------------------------------------------
int main(int argc, char** argv)
{
    // Input validation
    if (argc < 2) {
        cout << "Usage: " << argv[0] << " input_file_name" << "\n";
        return 1;
    }

    ifstream input_temps(argv[1]);
    if (!input_temps) {
        cout << "ERROR: " << argv[1] << " could not be opened" << "\n";
        return 2;
    }
    // End Input Validation

    // vector
    auto readings = parse_raw_temps<std::vector>(input_temps);

    // list
    // auto readings = parse_raw_temps<std::list<CoreTempReading>>(input_temps);

    //--------------------------------------------------------------------------
    // Output everything to match the Python version
    //--------------------------------------------------------------------------
    for (const CoreTempReading& theReading : readings) {
        cout << "(" << theReading.first << ", [";

        const vector<double>& coreTemps = theReading.second;
        for (int i = 0; i < coreTemps.size() - 1; i++) {
            cout << coreTemps[i] << ", ";
        }
        cout << *(coreTemps.end() - 1) << "])" << "\n";
    }

    //--------------------------------------------------------------------------
    // Split into separate vectors
    //--------------------------------------------------------------------------
    /*
    std::vector<double> times = {};
    std::vector<double> readingsCore0 = {};
    std::vector<double> readingsCore1 = {};
    std::vector<double> readingsCore2 = {};
    std::vector<double> readingsCore3 = {};
    for (const CoreTempReading& theReading : readings) {
        // Split the reading into time and temperatures
        const double time = theReading.first;
        const std::vector<double>& coreReadings = theReading.second;

        times.push_back(time);
        readingsCore0.push_back(coreReadings[0]);
        readingsCore1.push_back(coreReadings[1]);
        readingsCore2.push_back(coreReadings[2]);
        readingsCore3.push_back(coreReadings[3]);
    }

    // Output the data (in the same format as before)
    const int numReadings = times.size();
    for (int i = 0; i < numReadings; ++i) {
        cout << "(" << times[i] << ", [";
        cout << readingsCore0[i] << ", ";
        cout << readingsCore1[i] << ", ";
        cout << readingsCore2[i] << ", ";
        cout << readingsCore3[i] << "])" << "\n";
    }
    */

    //--------------------------------------------------------------------------
    // Split into separate vectors, but set up a 2D vector for core temperatures
    //--------------------------------------------------------------------------
    std::vector<double> times = {};
    std::vector<std::vector<double>> allCoreTemperatures = {};
    allCoreTemperatures.resize(4); // Create the 4 empty inner vectors

    for (const CoreTempReading& theReading : readings) {
        // Split the reading into time and temperatures
        const double time = theReading.first;
        const std::vector<double>& coreReadings = theReading.second;

        times.push_back(time);
        for (int coreIdx = 0; coreIdx < coreReadings.size(); ++coreIdx) {
            allCoreTemperatures[coreIdx].push_back(coreReadings[coreIdx]);
        }
    }

    // Output the data (in the same format as before)
    const int numReadings = times.size();
    for (int i = 0; i < numReadings; ++i) {
        cout << "(" << times[i] << ", [";

        const int lastCoreIdx = allCoreTemperatures.size() - 1;
        for (int coreIdx = 0; coreIdx < lastCoreIdx; ++coreIdx) {
            cout << allCoreTemperatures[coreIdx][i] << ", ";
        }
        cout << allCoreTemperatures[lastCoreIdx][i] << "])" << "\n";
    }

    return 0;
}
