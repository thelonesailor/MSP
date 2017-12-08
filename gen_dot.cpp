#include <bits/stdc++.h>
#include <time.h>
using namespace std;

#define MIN_PER_RANK 9 /* Nodes/Rank: How 'fat' the DAG should be.  */
#define MAX_PER_RANK 11
#define MIN_RANKS 9    /* Ranks: How 'tall' the DAG should be.  */
#define MAX_RANKS 11
#define PERCENT 10     /* Chance of having an Edge.  */

int edge[MAX_PER_RANK*MAX_RANKS+1][MAX_PER_RANK*MAX_RANKS+1];
int p=7;

int main (int argc, char** argv)
{
  p=atoi(argv[1]);

  int i, j, k,nodes = 0;
  srand (time (NULL));

  int ranks = MIN_RANKS
              + (rand () % (MAX_RANKS - MIN_RANKS + 1));

  // printf ("digraph {\n");
  for (i = 0; i < ranks; i++)
    {
      /* New nodes of 'higher' rank than all nodes generated till now.  */
      int new_nodes = MIN_PER_RANK
                      + (rand () % (MAX_PER_RANK - MIN_PER_RANK + 1));

      /* Edges from old nodes ('nodes') to new ones ('new_nodes').  */
      for (j = 0; j < nodes; j++)
        for (k = 0; k < new_nodes; k++)
          if ( (rand () % 100) < PERCENT)
            {//printf ("  %d -> %d;\n", j, k + nodes);
              edge[j][k+nodes]=1;    } /* An Edge.  */

      nodes += new_nodes; /* Accumulate into old node set.  */
    }

  for(int i=0;i<nodes;++i)
  {
    for(int j=0;j<nodes;++j)
    {
      if(edge[i][j]==1)
      {
        for(int k=0;k<nodes;++k)
        {
          if(edge[j][k]==1)
          {edge[i][k]=0;}
        }
      }
    }
  }  

int m=0;
  for(int i=0;i<nodes;++i)
  {
    for(int j=0;j<nodes;++j)
    {
      if(edge[i][j]==1)
        {++m;}
    }
}

cout<<nodes<<' '<<m<<' '<<p<<'\n';
for(int i=0;i<nodes;++i)
  {
    cout<<(rand()%50+1);
    if(i<nodes-1)
      {cout<<' ';}
  }
  cout<<'\n';

  for(int i=0;i<nodes;++i)
  {
    for(int j=0;j<nodes;++j)
    {
      if(edge[i][j]==1)
        {cout<<i<<' '<<j<<'\n';}
    }
}


return 0;
}