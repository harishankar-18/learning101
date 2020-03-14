#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
    string a, b;
    std::cin>>a>>b;
    std::cout<<a.size()<<" "<<b.size();
    std::cout<<'\n'<<a+b;
    char temp;
    temp= b[0];
    b[0]=a[0];
    a[0]=temp;
    std::cout<<'\n'<<a<<' '<<b;
    return 0;
}
