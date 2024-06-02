#include<iostream>
using namespace std;
class S
{
    public : 
        S()
        {
            cout<<"from the Default Constructor.\n";
            // ~S()
            // {
            //     cout<<"from the Default Distructor.\n";
            // }
        }
        void Disp()
        {
            cout<<"from the Default Function.\n";

        }
        ~S()
        {
            cout<<"from the Default Distructor.\n";
        }
};
int main()
{
    S a;
    a.Disp();
    return 0;
}