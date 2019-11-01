#include <iostream>
#include <string>
#include <sstream>
using namespace std;


void start_swiper()
{
    while(true) 
    {
        string input;
        string holder;
        string student_id;
        string student_name;
        string student_card;
        cout<<"Please swipe your student ID now:"<<endl;
        cin>>input;
        if(input=="q")
        {
            break;
        }
        stringstream ss(input);
        getline(ss,holder, '=');
        student_card= holder.erase(0,2);
        getline(ss,holder, '=');
        student_id= holder;
        getline(ss,holder, '=');
        string holder2;
        stringstream iss(holder);
        getline(iss, holder2,'/');
        student_name= holder2;
        getline(iss, holder2, '/');
        student_name= student_name + " " + holder2;
        cout<< endl;
        cout<< endl;
        cout<< endl;
        cout<<"Name: "<<student_name<<endl;
        cout<<"ID: "<<student_id<<endl;
        cout<<"Card Number: "<< student_card;
        cout<<endl;
        cout<< "thank you for swiping, this event will apear in your history within the next 24 hours"<<endl;
        cout<< endl;
        cout<< endl;
        cout<< endl;

    }


}

void associate(string id, string user, string pass)
{
    //associate id with account.
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






