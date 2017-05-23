#include <iostream>
#include <vector>
#include <stdio.h>
#include <limits.h>
using namespace std;
// the set of vertices not yet included in shortest path tree
int minDistance(vector<int> dist, vector<bool> sptSet, int V)
{
   // Initialize min value
   int min = INT_MAX, min_index;

   for (int v = 0; v < V; v++)
     if (sptSet[v] == false && dist[v] <= min)
         min = dist[v], min_index = v;

   return min_index;
}

int printSolution(vector<int> dist, int V, int n, int periodo)
{

   int optimo=INT_MAX;
   for (int i = n; i < V; i=i+periodo)
      if (dist[i]<optimo) optimo=dist[i];
if (optimo==INT_MAX) cout<<"-1"<<endl; else
 cout<<optimo<<endl;
}

// Funtion that implements Dijkstra's single source shortest path algorithm
// for a graph represented using adjacency matrix representation
void dijkstra(vector<vector<int>> graph, int V, int dest,int src, int periodo)
{
    vector<int> dist(V,0);     // The output array.  dist[i] will hold the shortest
                      // distance from src to i

    vector<bool> sptSet(V,0); // sptSet[i] will true if vertex i is included in shortest
                     // path tree or shortest distance from src to i is finalized

     // Initialize all distances as INFINITE and stpSet[] as false
    for (int i = 0; i < V; i++)
        dist[i] = INT_MAX, sptSet[i] = false;

     // Distance of source vertex from itself is always 0
        dist[src] = 0;

     // Find shortest path for all vertices
    for (int count = 0; count < V-1; count++)
    {
       // Pick the minimum distance vertex from the set of vertices not
       // yet processed. u is always equal to src in first iteration.
        int u = minDistance(dist, sptSet,V);

       // Mark the picked vertex as processed
        sptSet[u] = true;

       // Update dist value of the adjacent vertices of the picked vertex.
    for (int v = 0; v < V; v++)

         // Update dist[v] only if is not in sptSet, there is an edge from
         // u to v, and total weight of path from src to  v through u is
         // smaller than current value of dist[v]
        if (!sptSet[v] && graph[u][v] && dist[u] != INT_MAX && dist[u]+graph[u][v] < dist[v])
            dist[v] = dist[u] + graph[u][v];
     }

     // print the constructed distance array
     printSolution(dist, V, dest, periodo);
}

int main()
{

    int V,E;
    V=1;
    E=1;
    while (V>=0)
    {

        cin>>V>>E;
        if (V>=0)
        {

            int origen, destino, k;
            cin>>origen>>destino>>k;
            vector<int> auxiliar(V*(k+1),0);
            vector<vector<int>> graph (V*(k+1),auxiliar);

             for (int i=0;i<E;i++)
           {
               int c1,c2,p,d;
               cin>>c1>>c2>>p>>d;
               if (p==0)
               {
                    for (int j=c1;j<V*(k+1);j=j+V)
                    {
                        graph[j][c2]=d;
                        graph[c2][j]=d;
                        c2=c2+V;
                    }

               } else
               {
                    for (int j=c1;j<V*(k);j=j+V)
                    {
                        graph[j][c2+V]=d;
                        graph[c2][j+V]=d;
                        c2=c2+V;
                    }
               }

           }


            dijkstra(graph, V*(k+1), destino, origen,V);

        }
    }
    return 0;
}
