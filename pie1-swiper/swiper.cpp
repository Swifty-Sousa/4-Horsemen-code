#include <iostream>
using namespace std;


void start_swiper()
{
    while(true) 
    {
        string input;
        cout<<"Would you like to swipe card or enter ID"<< endl;
        cin>>input;
        if(input=="swipe")
        {
            cout<<"Please swipe card now">>endl;
            cin>> input;
            if(!fetch(input))
            {
                string des;
                cout<<"Card not associated with account, Do you have an account? (Y/N)"<<endl;
                cin>>des;
                des= tolower(des);
                if(des=="y")
                {
                    string user;
                    string pass;
                    cout<<"Enter Username (Identikey@colorado.edu):"<<endl;
                    cin>>user;
                    cout>>"Enter your [PRODUCT NAME HERE] password:"<<endl;
                    cin>>pass;
                    associate(des, user, pass)
                }
            }
            else
            {
                // account exsists and is associated.
                // add event to students event data.
            }
        }
        else
        {
            cout<<"Do you have an account with us"
        }
    }

}
void associate(string id, string user, string pass)
{
    //associate id with account.
}
void createaccount()
{
    string user;
    string pass;
    cout<<"Enter Username (Identikey@colorado.edu):"<<endl;
    cin>>user;
    cout>>"Enter your [PRODUCT NAME HERE] password:"<<endl;
    cin>>pass;

}

string fetch(string id)
{
    //fetch from database 
    return "failure";
}
int main(void)
{
    start_swiper();
}






