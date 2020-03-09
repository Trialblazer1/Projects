/**
	localizer.cpp

	Purpose: implements a 2-dimensional histogram filter
	for a robot living on a colored cyclical grid by
	correctly implementing the "initialize_beliefs",
	"sense", and "move" functions.	
*/

#include "localizer.h"
#include "helpers.cpp"
#include <stdlib.h>
#include "debugging_helpers.cpp"

using namespace std;

/**
    Initializes a grid of beliefs to a uniform distribution.

    @param grid - a two dimensional grid map (vector of vectors
    	   of chars) representing the robot's world. For example:

    	   g g g
    	   g r g
    	   g g g

		   would be a 3x3 world where every cell is green except
		   for the center, which is red.

    @return - a normalized two dimensional grid of floats. For
           a 2x2 grid, for example, this would be:

           0.25 0.25
           0.25 0.25
*/
vector< vector <float> > initialize_beliefs(vector< vector <char> > grid) {

  int ro = grid.size();
  int co = grid[0].size();
  int ar = ro * co;
  const float bel = 1.0 / ar;

  vector< vector <float> > newGrid;

  for (int i = 0; i < ro; i++) {
    vector <float> row;
    row.clear();
    for (int j = 0; j < co; j++){
      row.push_back(bel);
    }
    newGrid.push_back(row);
  }

	// your code here


	return newGrid;
}

/**
  
    Implements robot motion by updating beliefs based on the
    intended dx and dy of the robot.

    For example, if a localized robot with the following beliefs

    0.00  0.00  0.00
    0.00  1.00  0.00
    0.00  0.00  0.00

    and dx and dy are both 1 and blurring is 0 (noiseless motion),
    than after calling this function the returned beliefs would be

    0.00  0.00  0.00
    0.00  0.00  0.00
    0.00  0.00  1.00

  @param dy - the intended change in y position of the robot

  @param dx - the intended change in x position of the robot

    @param beliefs - a two dimensional grid of floats representing
         the robot's beliefs for each cell before sensing. For
         example, a robot which has almost certainly localized
         itself in a 2D world might have the following beliefs:

         0.01 0.98
         0.00 0.01

    @param blurring - A number representing how noisy robot motion
           is. If blurring = 0.0 then motion is noiseless.

    @return - a normalized two dimensional grid of floats
         representing the updated beliefs for the robot.
*/
vector< vector <float> > move(int dy, int dx,
  vector < vector <float> > beliefs,
  float blurring)
{
  int r = beliefs.size();
  int c = beliefs[0].size();
  int new_r = 0;
  int new_c = 0;

  vector < vector <float> > newGrid (r, vector <float> (c, 0));

  for (int i = 0; i < r; i++) {
    for (int j = 0; j < c; j++) {

      new_r = (i+ dy + c) % c;
      new_c = (j + dx + r) % r;
      newGrid[new_r][new_c] = beliefs[i][j];
    }
  }


  return blur(newGrid, blurring);
}


/**
    Implements robot sensing by updating beliefs based on the
    color of a sensor measurement

	@param color - the color the robot has sensed at its location

	@param grid - the current map of the world, stored as a grid
		   (vector of vectors of chars) where each char represents a
		   color. For example:

		   g g g
    	   g r g
    	   g g g

   	@param beliefs - a two dimensional grid of floats representing
   		   the robot's beliefs for each cell before sensing. For
   		   example, a robot which has almost certainly localized
   		   itself in a 2D world might have the following beliefs:

   		   0.01 0.98
   		   0.00 0.01

    @param p_hit - the RELATIVE probability that any "sense" is
    	   correct. The ratio of p_hit / p_miss indicates how many
    	   times MORE likely it is to have a correct "sense" than
    	   an incorrect one.

   	@param p_miss - the RELATIVE probability that any "sense" is
    	   incorrect. The ratio of p_hit / p_miss indicates how many
    	   times MORE likely it is to have a correct "sense" than
    	   an incorrect one.

    @return - a normalized two dimensional grid of floats
    	   representing the updated beliefs for the robot.
*/
vector< vector <float> > sense(char color,
	vector< vector <char> > grid,
	vector< vector <float> > beliefs,
	float p_hit,
	float p_miss)
{
  int roww = grid.size();
  int coll = grid[0].size();

  vector< vector <float> > newGrid (roww, vector <float> (coll, 0));

  for (int i = 0; i < roww; i++) {
    for (int j = 0; j < coll; j++) {
      newGrid[i][j] = grid[i][j];
      if (grid[i][j] == color) {
        newGrid[i][j] *= newGrid[i][j] * p_hit;
      }
      else {
        newGrid[i][j] *= newGrid[i][j] * p_miss;
      }
    }
  }
	return normalize(newGrid);
}
