#include <iostream>

using namespace std;

int main() {
    int radiant = 0, dire = 0, i = 0, counter = 0;
    string s;
    cin >> s;
    int Size = s.length();
    int is_dead[Size];
    for (int j = 0; j < Size; j++) {
        if (s[j] == 'D')
            dire++;
        else
            radiant++;
        is_dead[j] = 0;
    }

    while ((dire > 0) && (radiant > 0)) {
        if (is_dead[i] == 0) {
            if (s[i] == 'D') {
                if (counter > 0) {
                    is_dead[i] = 1;
                    dire--;
                }
                counter--;
            } else if (s[i] == 'R') {
                if (counter < 0) {
                    is_dead[i] = 1;
                    radiant--;
                }
                counter++;
            }
        }
        i = (i + 1) % Size;
    }
    if (radiant == 0)
        cout << "Dire";
    else
        cout << "Radiant";
    return 0;
}
