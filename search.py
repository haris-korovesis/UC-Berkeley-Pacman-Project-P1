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


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


#function for depth first search
def dfs2(problem,root):
    # Create a moves stack that mirrors the visited stack 
    # So i can keep track of the moves in the correct order
    visited = set()
    path = []
    stack = util.Stack()
    movesStack = util.Stack()
    tempPath = []

    # Add the first node
    stack.push(root)
    movesStack.push(root)
    visited.add(root)


    while stack.isEmpty() == False:

        t = stack.pop()

        #check if goal
        if problem.isGoalState(t) == True:
            #print("Object Found!")
            return path

        #check visited
        if t not in visited:
            #print(t)
            visited.add(t)

        #if the next node is unvisited
        #push it in the stack
        next = problem.getSuccessors(t)
        for j,d,c in next:
            if (j not in visited):
                stack.push(j)
                tempPath = path + [d]
                movesStack.push(tempPath)

        #pop the moves
        path = movesStack.pop()

    return

def depthFirstSearch(problem):
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

    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    
    # create an empty list and call the funct
    path = []
    node = problem.getStartState()
    path = dfs2(problem,node)
    return path


# Breadth First Search function
def BFSAlg(problem,root):
    # Create a moves queue that mirrors the visited stack 
    # So i can keep track of the moves in the correct order

    visited = set()
    path = []
    q = util.Queue()
    movesQueue = util.Queue()
    tempPath = []

    # push the first node 
    q.push(root)
    #movesQueue.push(root)
    visited.add(root)

    while q.isEmpty() == False:
        
        t = q.pop()

        #check if goal
        if problem.isGoalState(t) == True:
            #print("Object Found!")
            return path
        

        # if next node not in visited
        next = problem.getSuccessors(t)
        for j,d,c in next:
            if j not in visited:
                #print(movesQueue.list)
                visited.add(j)
                q.push(j)
                tempPath = path + [d]
                movesQueue.push(tempPath)
        
        path = movesQueue.pop()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"


    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    
    # Call my bfs function and return the moves path
    path = []
    node = problem.getStartState()
    path = BFSAlg(problem,node)
    return path

# My uniformCostSearch function
def uniformCostSearchAlg(problem,root):
    # Create a priority Queue for nodes and a mirror one for moves 
    visited = set()
    path = []
    prqueue = util.PriorityQueue()
    movesprqueue = util.PriorityQueue()
    tempPath = []
    

    t = (0,0)
    prqueue.push(root,t)
    # visited.add(root)

    t = prqueue.pop()

    # while the goal is not achieved 
    while problem.isGoalState(t) == False:
        
        # take actions only if the node is not visited 
        if t not in visited:
            visited.add(t)

            next = problem.getSuccessors(t)
            for j,d,c in next:
                    tempPath = path + [d]
                    cost = problem.getCostOfActions(tempPath)
                    if j not in visited:
                        visited.add(t)
                        prqueue.push(j,cost)
                        movesprqueue.push(tempPath,cost)

        # pop mirror queues
        t = prqueue.pop()
        path = movesprqueue.pop()
    
    return path

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    path = []
    node = problem.getStartState()
    path = uniformCostSearchAlg(problem,node)
    return path


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0



def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    # Create PriorityQueues

    PRqueue = util.PriorityQueue()
    visited = set()

    # Incert the root
    root = problem.getStartState()

    # Node , Path , Cost / Priority Number
    PRqueue.push( (root,[],0) , 0)

    while PRqueue.isEmpty() == False:

        # split the tuple
        node, path, cost = PRqueue.pop()

        # only if the node is not visited 
        if node not in visited:
            visited.add(node)

            # if goal state return and end
            if problem.isGoalState(node) == True:
                return path

            next = problem.getSuccessors(node)
            for j,d,c in next:
                if j not in visited:
                    heuristicCost = cost + c + heuristic(j,problem)
                    PRqueue.push( (j,path+[d],cost+c),heuristicCost)

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
