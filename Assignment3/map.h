//
//  map.h
//  assignment3_AI
//
//  Created by Kartik Rattan on 11/8/19.
//  Copyright © 2019 Kartik Rattan. All rights reserved.
//

#ifndef map_h
#define map_h

#include "point.h"
#include <vector>

using namespace std;

class map
{
public:
    map()
    {
        map_env.resize(50,{});
        map_prob.resize(50,{});
        double initial_belief = 1.0 / (50.0 * 50.0);
        cout << "Initial belief: " << initial_belief << endl;
        for(int i=0; i<map_env.size(); i++)
        {
            map_env[i].resize(50);
            map_prob[i].resize(50,initial_belief);
        }
        generate_environment(map_env);
    };
    
    void generate_environment(vector<vector<point>> &map_env)
    {
        int dim = 50;
        int size_map = dim*dim;
        vector<double> num_terrain_cells = {0.2 * size_map,0.3 * size_map,0.2 * size_map,0.3 * size_map};
        for(int i = 0; i < num_terrain_cells.size(); i++)
            cout << num_terrain_cells[i]<<endl;
        
        vector<int> set;
        set.resize(size_map);
        
        vector<int> check_size = {0,0,0,0};
        for(int i=0; i<set.size(); i++)
        {
            if(i<num_terrain_cells[0])
            {
                set[i] = 0;
                check_size[0]++;
            }
            else if(i>=num_terrain_cells[0] && i< num_terrain_cells[0] + num_terrain_cells[1])
            {
                set[i] = 1;
                check_size[1]++;

            }
            else if(i>=num_terrain_cells[0] + num_terrain_cells[1] && i< num_terrain_cells[0] + num_terrain_cells[1] + num_terrain_cells[2])
            {
                set[i] = 2;
                check_size[2]++;

            }
            else
            {
                set[i] = 3;
                check_size[3]++;

            }
        }
        for(int i = 0; i<4; i++)
        {
            cout << i<<"." << check_size[i]<<endl;
        }
        
//        for (int i = 0; i < 2500; i++)
//        {
//            if(i%50==0)
//                cout << endl;
//            cout << set[i] << " ";
//
//        }
        cout << endl;
        
        for(int i = 0; i < size_map; i++)
        {
            if(rand() % 2 == 0)
            {
                int x = i;
                
                int x_ran = rand() % size_map;
                
                swap(x,x_ran,set);
            }
        }
        
        for(int i = 0; i < size_map; i++)
        {
            int y = i % dim;
            int x = i / dim;
            
            (map_env[y][x]).terrain_type = set[i];
        }
        
    }
    void swap(int x, int x_ran, vector<int> &set)
    {
        int temp = set[x];
        set[x] = set[x_ran];
        set[x_ran] = temp;
    }
    
    void print_board()
    {
        cout << "Printing Map:" << endl << endl;
        for (int i = 0; i < 50; i++)
        {
            for (int j = 0; j < 50; j++)
            {
                cout << map_env[i][j].terrain_type << " ";
            }
            cout << endl;
        }
        cout << endl;
    }
    void print_probability_board()
    {
        cout << "Printing Probability Map:" << endl << endl;
        for (int i = 0; i < 50; i++)
        {
            for (int j = 0; j < 50; j++)
            {
                cout << map_prob[i][j] << " ";
            }
            cout << endl;
        }
        cout << endl;
    }
    
private:
    
    vector<vector<point>>  map_env;
    vector<vector<double>> map_prob;
};


#endif /* map_h */
