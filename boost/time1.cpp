#include <string>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <stdio.h>
#include <fstream>

#include <boost/timer.hpp>
#include <boost/progress.hpp>

using namespace std;
using namespace boost;

int main()
{
    timer t;
    progress_timer t1;
    vector<string> v(100);
    ofstream fs("test.txt");
    progress_display pd(v.size());
    for (int  i = 0; i < v.size(); i++)
    {
        fs << v[i] << endl;
        ++pd;
    }
    cout << "max time span:" << t.elapsed_max() /3600 << "h" << endl;
    cout << "min time:" << t.elapsed_min() << "s" << endl;
    cout << "now time :" << t.elapsed() << "s" << endl;
    cout << "progess time:" << t1.elapsed() << endl; 
    getchar();
}