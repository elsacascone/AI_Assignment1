# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions
from typing import List

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # Initialize the frontier with the start state and an empty path
    frontier = util.Stack()
    start_state = problem.getStartState()
    # We store tuples of (current_state, actions_to_reach_state)
    frontier.push((start_state, []))
    
    # Keep track of visited states to avoid cycles and redundant work
    visited = set()

    while not frontier.isEmpty():
        # Pop the deepest node from the stack
        current_state, actions = frontier.pop()

        # Goal check
        if problem.isGoalState(current_state):
            return actions

        # Graph Search: Only expand if the state hasn't been visited
        if current_state not in visited:
            visited.add(current_state)
            
            # Expand successors
            for successor, action, cost in problem.getSuccessors(current_state):
                if successor not in visited:
                    # Create the new path list for this successor
                    new_actions = actions + [action]
                    frontier.push((successor, new_actions))

    # Return empty list if no solution is found
    return []
    #util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # BFS uses a Queue (First-In, First-Out)
    frontier = util.Queue()
    start_state = problem.getStartState()
    frontier.push((start_state, []))
    
    # Graph search: keep track of visited states
    visited = []

    while not frontier.isEmpty():
        current_state, actions = frontier.pop()

        if problem.isGoalState(current_state):
            return actions

        if current_state not in visited:
            visited.append(current_state)
            
            for successor, action, cost in problem.getSuccessors(current_state):
                if successor not in visited:
                    # Create the new path for this successor
                    new_actions = actions + [action]
                    frontier.push((successor, new_actions))

    return []
    #util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # PriorityQueue requires: (item, priority)
    frontier = util.PriorityQueue()
    start_state = problem.getStartState()
    
    # Push (state, actions, cumulative_cost) with priority 0
    frontier.push((start_state, [], 0), 0)
    
    # Graph search: keep track of visited states
    visited = {} # Using a dict to store the best cost found to a state

    while not frontier.isEmpty():
        current_state, actions, current_cost = frontier.pop()

        # Goal check
        if problem.isGoalState(current_state):
            return actions

        # If we haven't visited or found a cheaper way to this state
        if (current_state not in visited) or (current_cost < visited[current_state]):
            visited[current_state] = current_cost
            
            for successor, action, step_cost in problem.getSuccessors(current_state):
                new_actions = actions + [action]
                new_cost = current_cost + step_cost
                
                # The priority is the total cumulative cost
                frontier.push((successor, new_actions, new_cost), new_cost)

    return []
    #util.raiseNotDefined()

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
