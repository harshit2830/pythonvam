 //1) WAP to create a class BCA.

#include <iostream>
using namespace std; 
class BCA
{
    int age, reg_no;

    public:
    void getdata(int ,int );
    void putdata();
};
    void BCA:: getdata(int a, int r)
{
    age = a;
    reg_no = r;
}
    void BCA::putdata()
{
    cout<< "age" <<age<<endl;
    cin>>age;
    cout<< "reg_no:" << reg_no << endl;
    cin>>reg_no;
}
    int main()
{
    BCA b1, b2;
    b1.getdata(1,2);
    b2.getdata(3,4);
    b1.putdata();
    b2.putdata();
    return 0;
}




//  2) WAP to create a class of rectangle.


/*
#include<iostream>
using namespace std;
class rectangle
{
private:
int length,breath;
public:
void getdata();
void putinfo();
};
void rectangle::getdata()
{
cout<<"Enter the lenght of rectangle:";
cin>>length;
cout<<"Enter the breath of rectangle:";
cin>>breath;
}
void rectangle::putinfo()
{
cout<<"The length of rectangle is "<<length<<endl;
cout<<"The breath of rectangle is "<<breath<<endl;
}
int main()
{
    rectangle r1,r2;
    r1.getdata();
    r2.getdata();
    r1.putinfo();
    r2.putinfo();
    return 0;
}
*/




//  3) WAP to create a class of circumference.


/*
#include<iostream>
using namespace std;

class circle
{
private:
int radius;
public:
void area();
void circumference();
};
float pie = 3.14;
void circle::area()
{
    float area;
    cout<<"Enter the radius of circle:";
    cin>>radius;
    area=pie*radius*radius;
    cout<<"area:"<<area;

}
void circle::circumference()
{
    float circumference;
    cout<<"Enter the radius of circle:";
    cin>>radius;
    circumference=2*pie*radius;
    cout<<"circumference:"<<circumference<<endl;
}
int main()
{
    circle c1,c2;
    c1.area();
    c1.circumference();
    c2.area();
    c2.circumference();

    return 0;
}
*/

//  4) WAP to create a class college, private Data member course N and ID and in public Data function getinfo() or putinfo()


/*
#include<iostream>
using  namespace std;
class college
{
    private:
    
    //course name as A
    //Id variable as B
    
    char A[20];
    int B;
    
    public:
    
    void getinfo();
    void putinfo();
};

void college:: getinfo(void)
{
    cout<<"ENter the course name ";
    cin>>A;
    cout<<"Enter the ID ";
    cin>>B;
}
void college::putinfo()
{
    cout<<"The course name is "<<A<<endl;
    cout<<"The ID number is "<<B<<endl; 

}
int main()
{
    college c1;
    c1.getinfo();
    c1.putinfo();
    
    return 0;
}
*/




//  6)  WAP to create a class with static Data member. class name item.



/*
#include<iostream>
using name std;
class item
{
    static int count;
    int number;
    public:
    void getdata()
{
    number=a;
    count++;
}
void getcount(void)
{
    cout<<"The count is "<<count;
}
};
int item::count;
int main()
{
    item a,b,c;
    a.getcount();
    b.getcount();
    c.getcount();

    a.getdata();
    b.getdata();
    c.getdata();

    cout<<"After reading Data";

    a.getcount();
    b.getcount();
    c.getcount();

return 0;
}
*/


//  7)WAP to create a class with static Data member. class name item.


/*
#include<iostream>
using namespace std;
class item
{
      static int count;
      int number;
      public:
      void getdata(int a)
    {
        number=a;
        count++;
    }
      void getcount(void)
    {
      cout<<" count "<<count<<endl;

    }
};
int item::count;
int main()
{
    item a,b,c;
    cout<<"Before reading Data"<<endl;
    a.getcount();
    b.getcount();
    c.getcount();
    
    a.getdata(1);
    b.getdata(2);
    c.getdata(3);

    cout<<"After reading data"<<endl;
    a.getcount();
    b.getcount();
    c.getcount();
    
    return 0;
} 

*/                       



//  8)  WAP to make a class using static member function from class name test


/*
#include<iostream>
using namespace std;
class test
{
  static int count;
  int code;
  public:
  void setcode(void)
  {
     code=count++;
  }
  void showcode(void)
  {
    cout<<"Object code: "<<code<<", count: "<<count<<endl;
  }
  static void showcount()
  {
    cout<<"Count: "<<count<<endl;
  }
};

int test::count;
int main()
{
    test t1,t2,t3;
    cout<<"Before reading Data"<<endl;
    t1.setcode();   
    t2.setcode();
    t3.setcode();

    test::showcount();
    cout<<"After reading data"<<endl;
    test t4;
    t4.setcode();
    test::showcount();
    t1.showcode();
    t2.showcode();
    t3.showcode();
    t4.showcode();

    return 0;
}

*/


//  9) WAP to make a class student having private rollno and public getrollno
//   and also a class BCA having private data marks and three public functions are there that is getmarks(), getresult() and display.

/*
#include<iostream>
using namespace std;

class student
{
private:
    int roll_no;

public:
    void getrollno();
};

class BCA : public student
{
private:
    int marks;

public:
    void getmarks();
    void display();
};

void student::getrollno()
{
    cout << "Enter roll no: ";
    cin >> roll_no;
}

void BCA::getmarks()
{
    cout << "Enter marks: ";
    cin >> marks;
}

void BCA::display()
{
    if (marks > 80)
    {
        cout << "Passed" << endl;
    }
    else
    {
        cout << "Failed" << endl;
    }
}

int main()
{
    BCA s;
    s.getrollno();
    s.getmarks();
    s.display();
    return 0;
}

*/

//WAP to make a class of an employee to print details using an array of objects


/*
#include<iostream>
using namespace std;

class employee
{
    char name[50];
    float age;

public:
    void getdata();
    void putdata();
};

void employee ::getdata(void)
{
    cout << "Enter name: ";
    cin>>name;
    cout << "Enter age: ";
    cin>>age;
}

void employee ::putdata(void)
{
    cout<<"Name: "<<name<<endl;
    cout<<"Age: "<<age<<endl;
}

int main()
{
    const int size=3;
    employee manager[size];
    for(int i=0;i<size;i++)
    {
        cout<<"\n Details of manager "<<i+1<<endl;
        manager[i].getdata();
    }
    cout<<"\n";
    for(int i=0;i<size;i++)
    {
        cout<<"\n Manager: "<< i+1<<endl;
        manager[i].putdata();
    }
    return 0;
}

*/