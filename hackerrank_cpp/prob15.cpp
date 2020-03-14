#include<bits/stdc++.h>

using namespace std;

class Box
{
    int l, b, h;
    public:
    Box()
    {
        l= 0;
        b= 0;
        h= 0;
    }
    Box(int x, int y, int z)
    {
        l= x;
        b= y;
        h= z;
    }
    Box(Box &A)
    {
        l= A.l;
        b= A.b;
        h= A.h;
    }
    int getLength()
    {
        return l;
    }
    int getBreadth()
    {
        return b;
    }
    int getHeight()
    {
        return h;
    }
    long long CalculateVolume()
    {
        return long(l)* long(b)* long(h);
    }
    bool operator<(Box &a)
    {
        if(l< a.l) return true;
        else if((l== a.l)&&(b< a.b)) return true;
        else if((l== a.l)&&(b== a.b)&& (h< a.h)) return true;
        else return false;
    }
    friend ostream& operator<<(ostream& os, const Box& bx);
};
ostream& operator<<(ostream& os, const Box& bx)
    {
        os << bx.l << ' ' << bx.b << ' ' << bx.h;
        return os;
    }


void check2()
{
	int n;
	cin>>n;
	Box temp;
	for(int i=0;i<n;i++)
	{
		int type;
		cin>>type;
		if(type ==1)
		{
			cout<<temp<<endl;
		}
		if(type == 2)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			temp=NewBox;
			cout<<temp<<endl;
		}
		if(type==3)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			if(NewBox<temp)
			{
				cout<<"Lesser\n";
			}
			else
			{
				cout<<"Greater\n";
			}
		}
		if(type==4)
		{
			cout<<temp.CalculateVolume()<<endl;
		}
		if(type==5)
		{
			Box NewBox(temp);
			cout<<NewBox<<endl;
		}

	}
}

int main()
{
	check2();
}
