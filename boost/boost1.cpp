#include <string>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <stdio.h>

#include <boost/version.hpp>
#include <boost/config.hpp>
using namespace std;

int main(int argc, char *argv[])
{
    cout << BOOST_VERSION << endl;
    cout << BOOST_LIB_VERSION << endl;
    cout << BOOST_PLATFORM << endl;
    cout << BOOST_COMPILER  << endl;
    cout << BOOST_STDLIB << endl;
    getchar();
    return 0;
}
