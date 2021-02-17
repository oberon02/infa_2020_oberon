#include <iostream>
#include<cmath>

using namespace std;

#include <iostream>
#include<cmath>

using namespace std;

1 ok
int main()
{
    int a;
    cin >> a;
    int b;
    cin >> b;
    int c;
    cin >> c;
    if(a + b < c || b + c < a || a + c < b){
        cout << "unreal"<< endl;
    }
    if(a*a + b*b == c*c || b*b + c * c == a * a || a * a + c * c == b * b){
        cout << "right" << endl;
    }
    if(a*a + b*b > c*c && b*b + c * c > a * a && a * a + c * c > b * b){
        cout << "tup"<< endl;
    } else {
        cout << "ostr"<< endl;
    }

}

2 ok
int main()
{
    int a;
    cin >> a;
    int b;
    b = a / 100;
    int c;
    c = (a - 100 * b) / 10;
    int d;
    d = (a - 100 * b - 10 * c);
    cout << b;
    cout << " ";
    cout << c;
    cout << " ";
    cout << d;
}

3 ok
int main()
{
    int a;
    cin >> a;
    int i;
    for (i = 2; i <= sqrt(a); i++){
        while (a % i == 0){
            a = a / i;
            cout << i;
            cout << "\n";
        }
    }
    if (a != 1) {
    cout << a;
    cout << "\n";
  }
}

4
int prime(int n){
        int g = 0;
        int y = 0;
        int k = n;
        int pr = 0;
        int i;
        int j;
        for(i = 2; i <= n * n; i++){
            y = 0;
            for(j = 1; j <= i; j++){
                if(i % j == 0){
                    y--;
                }
            }
            if(y == 0){
                k--;
                pr = i;
            }
             if (k == 0){
                break;
            }
        }
        return pr;
    }
int main()
{
    int n;
    cin >> n;
    int k;
    k = prime(n);
    cout << k;

}

5 ok
int main() {
  int n;
  int n2;
  int x;
  int y;
  int z;
  int t;
  cin >> n;
  n2 = n;
  x = sqrt(n2);
  n2 = n2 - x*x;
  y = sqrt(n2);
  n2 = n2 - y*y;
  z = sqrt(n2);
  n2 = n2 - z*z;
  t = sqrt(n2);
  if (x*x + y*y + z*z + t*t == n) {
    cout << x << ", " << y << ", " << z << ", " << t;;
  }
}

6 ok
int main()
{
    int a;
    a = 1;
    int m;
    m = 0;
    int n;
    n = 0;
    while(a != 0){
        cin >> a;
        if (a > m){
            m = a;
            n = 0;
        }
        if (a == m){
            n++;
        }
    }
    cout << m << " " << n;
}

7 ok
int main()
{
    int a,b,c,d,e;
    cin >> a;
    e = 1;
    for(b = 0; b <= a && e != 0; b++){
        for(c = 0; c <= a && e != 0; c++){
            if ( b*b*b + c*c*c == a){
                e = 0;
                cout << b << "\n" << c;
            }
        }
    }
    if (e != 0) {
        cout << "impossible";
    }
}

8 ok
int main()
{
    int a,b,m,i,y;
    cin >> a;
    cin >> b;
    cin >> m;
    a = a % m;
    b = b % m;
    y = 0;
    for (i = 1; i <= m; i++){
        if((a * i) % m == b){
            cout << i << "\n";
            y--;
        }
    }
    if (y == 0) {
        cout << -1;
    }
}

9 ok
int main()
{
    int N,x,i;
    int bm, m, lmi, mi;
    bm = m = -10000;
    mi = lmi = 10000;
    cin >> N;
    for(i = 0; i < N; i++){
        cin >> x;
        if (x > bm){
            m = bm;
            bm = x;
        } else if (x > m) {
        m = x;}

        if (x < lmi){
            mi = lmi;
            lmi = x;

        } else if (x < mi){
        mi = x;}

    }
    cout << bm << " " << m << "\n";
    cout << lmi << " " << mi;

}
