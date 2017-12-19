/*
Implementation of section 5.3 in

*/

#include <bits/stdc++.h>
#include <random>
using namespace std;

#define pb push_back

/*
Input in command line:
v e p lopt
*/

int main(int argc, char **argv)
{
    // for(int i=1;i<=4;++i)
    // {cout<<argv[i]<<" ";}cout<<endl;

int n=atoi(argv[1]);//number of nodes/tasks
int e=atoi(argv[2]);//number of edges
int p=atoi(argv[3]);//number of processors
int lopt=atoi(argv[4]);//optimal length of schedule


int x[p],l=n;
default_random_engine generator;
uniform_int_distribution<int> distribution(2,(2*n)/p);
for(int i=0;i<p-1;++i)
{
    x[i]=distribution(generator);
    l-=x[i];
    if(l<0)
    {cerr<<"Error occured, no nodes left for later processors\n";}
}
x[p-1]=l;

// cerr<<"x[i]s decided\n";
//dividing into x[i] parts

vector<pair<int,pair<int,int> > >tasks;
for(int i=0;i<p;++i)
{
    if(x[i]==0)
    {
        //No task for this processor
    }
    else if(x[i]==1)
    {tasks.pb({i,{0,lopt}});}
    else if(x[i]>1)
    {
        default_random_engine generator;
        uniform_int_distribution<int> distribution(1,1.4*(lopt)/x[i]);
        int st=0;
        for(int j=1;j<x[i];++j)
        {
            int l=distribution(generator);
            tasks.pb({i,{st,st+l}});
            st+=l;
        }
        tasks.pb({i,{st,lopt}});
        if(st>=lopt)
        {cerr<<"exceded lopt\n";}
    }
    else
    {
        cerr<<"x[i] has the wrong value\n";
    }
}

// cerr<<"tasks vector made\n";

vector<pair<int,int> >all_edges;
for(int i=0;i<tasks.size();++i)
{
    for(int j=0;j<tasks.size();++j)
    {
        if(tasks[j].second.first>=tasks[i].second.second)
        {all_edges.pb({i,j});}
    }
}
shuffle(all_edges.begin(),all_edges.end(), generator);
shuffle(all_edges.begin(),all_edges.end(), generator);

if(all_edges.size()<e)
{cerr<<"e is greater than the maximum number of edges possible\n";}

vector<pair<int,int> >edges;
default_random_engine g;
uniform_int_distribution<int> distribution2(0,all_edges.size()-1);
for(int i=0;i<e;++i)
{
    edges.pb(all_edges[i]);
}

if(tasks.size()!=n)
{cerr<<"Number of nodes is not same as n";}
if(edges.size()!=e)
{cerr<<"Number of edges is not same as e";}


//output
cout<<n<<' '<<e<<' '<<p<<'\n';
for(int i=0;i<n;++i)
{cout<<tasks[i].second.second-tasks[i].second.first;if(i<n-1){cout<<' ';}}
cout<<'\n';
for(int i=0;i<e;++i)
{cout<<edges[i].first<<' '<<edges[i].second<<'\n';}


return 0;
}
