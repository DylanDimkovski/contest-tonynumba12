# myTeam.py
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

import random, util

from captureAgents import CaptureAgent
from game import Directions
from game import Actions
from util import nearestPoint
from util import PriorityQueue
import math

#####################
# SEARCH HEURISTICS #
#####################

def manDist(x, y ):
  return abs( x[0] - y[0] ) + abs( x[1] - y[1] )

def avoidGhost(ghosts, state, danger):
  heuristic = 0
  
  if ghosts and state == ghosts[0].getPosition():
    heuristic -= danger**2

  if ghosts is not None:    
    heuristic += (danger - ghosts[1]) ** danger

  return heuristic

def patrolHeuristic(state, gameState, agent):
  ghosts    = agent.getNearestOpponent(gameState)
  danger    = 2
  heuristic = 0

  heuristic += avoidGhost(ghosts, state, danger)
  heuristic = -agent.getMazeDistance(state, agent.getGuardPosition())

  return heuristic

def guardHeuristic(state, gameState, agent):
  ghosts    = agent.getNearestOpponent(gameState)
  invaders  = agent.getInvaders(gameState)
  danger    = 1
  heuristic = 0

  heuristic += avoidGhost(ghosts, state, danger)
  
  if invaders is not None:
    heuristic = -agent.getMazeDistance(state, invaders[0].getPosition())

  return heuristic

def foodHeuristic(state, gameState, agent):
  food      = agent.getFood(gameState).asList()
  heuristic = 0

  if agent.target:
    
    if agent.red and state[0] < agent.halfway:
      heuristic -= 100
    elif state[0] > agent.halfway:
      heuristic -= 100

    heuristic -= agent.getMazeDistance(state, agent.target)
  else:
    heuristic -= agent.getNearest(state, food)

  return heuristic

def trackHeuristic(state, gameState, agent):
  ghosts    = agent.getNearestOpponent(gameState)
  danger    = 5
  heuristic = 0

  heuristic += avoidGhost(ghosts, state, danger)
  heuristic = -agent.getMazeDistance(state, agent.lastEaten)

  return heuristic

def escapeHeuristic(state, gameState, agent):
  ghosts    = agent.getNearestOpponent(gameState)
  danger    = 3
  heuristic = 0

  heuristic -= agent.getNearest(state, agent.boundaries)

  heuristic += avoidGhost(ghosts, state, danger)

  return heuristic

def evasiveHeuristic(state, gameState, agent):
  capsules  = agent.getCapsules(gameState)
  ghosts    = agent.getNearestOpponent(gameState)
  danger    = 15
  heuristic = 0

  d1 = agent.getNearest(state, agent.boundaries)
  d2 = agent.getNearest(state, capsules)

  heuristic -= min(d1, d2)
  heuristic += avoidGhost(ghosts, state, danger)

  return heuristic

def martyrHeuristic(state, gameState, agent):
  ghosts    = agent.getNearestOpponent(gameState)
  danger    = 5
  heuristic = 0
  
  if ghosts is not None and len(ghosts) > 0:
    heuristic += agent.getMazeDistance(state, ghosts[0].getPosition()) ** danger

  return heuristic

#######################
# A* SEARCH ALGORITHM #
#######################

def aStar(problem, gameState, agent, heuristic):
  
  frontier = PriorityQueue()
  start = problem.getStartState()
  visited = []

  frontier.push((start, [], 0), heuristic(start, gameState, agent))

  while not frontier.isEmpty():
    node = frontier.pop()

    if node[0] not in visited:
      visited.append(node[0])
      
      if problem.isGoalState(node[0]):
        return node[1]

      for successor in problem.getSuccessors(node[0]):
        path = list(node[1])
        state = successor[0]
        action = successor[1]
        
        if state not in visited:
          path.append(action)
          next = (state, path, successor[2] + node[2])
          frontier.push(next, successor[2] + node[2] + heuristic(state, gameState, agent))

  return []

############################
# ABSTRACT SEARCH PROBLEMS #
############################

class SearchProblem:

  def __init__(self, gameState, agent):
    self.startState = gameState.getAgentPosition(agent.index)
    self.walls      = gameState.getWalls()
    self.boundaries = agent.getBoundaries(gameState)

    self.food      = agent.getFood(gameState).asList()
    self.capsules  = agent.getCapsules(gameState)
    self.carrying  = gameState.getAgentState(agent.index).numCarrying
    self.remaining = len(self.food)
    self.target    = agent.target

    self.lastEaten = agent.lastEaten
    self.invaders  = agent.getInvaders(gameState)
    self.ghosts    = agent.getGhosts(gameState)
    self.agent     = agent

  def getStartState(self):
    return self.startState

  def isGoalState(self, state):
    util.raiseNotDefined()

  def getSuccessors(self, state):
    successors = []

    for action in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
      x,y = state
      dx, dy = Actions.directionToVector(action)
      nextx, nexty = int(x + dx), int(y + dy)
      enemyPos = (nextx, nexty) in [g.getPosition() for g in self.ghosts if g.scaredTimer < 5]

      if not enemyPos and not self.walls[nextx][nexty]:
        nextState = (nextx, nexty)
        successors.append((nextState, action, 1))

    return successors

  def getCostOfActions(self, actions):
    if actions == None: return 999999
    x,y= self.getStartState()
    cost = 0
    for action in actions:
      dx, dy = Actions.directionToVector(action)
      x, y = int(x + dx), int(y + dy)
      if self.walls[x][y]: return 999999
      cost += 1
    return cost

############################
# CONCRETE SEARCH PROBLEMS #
############################

class FindFood(SearchProblem):

  def isGoalState(self, state):
    return (state == self.target) if self.target else state in self.food

class EvasiveManeuver(SearchProblem):
    
  def isGoalState(self, state):
    return state in self.boundaries or state in self.capsules

class EscapeHome(SearchProblem):

  def isGoalState(self, state):
    return state in self.boundaries

class TrackLastEaten(SearchProblem):
  
  def isGoalState(self, state):
    return state == self.lastEaten

class GuardTerritory(SearchProblem):

  def isGoalState(self, state):
    return False if not self.invaders else state in [invader.getPosition() for invader in self.invaders]

class Patrol(SearchProblem):

  def isGoalState(self, state):    
    return state == self.agent.getGuardPosition()

class Seppuku(SearchProblem):

  def isGoalState(self, state):    
    return state in [g.getPosition() for g in self.ghosts]

#################
# TEAM CREATION #
#################

def createTeam(firstIndex, secondIndex, isRed, first = 'OffensiveAgent', second = 'DefensiveAgent', numTraining = 0):
  """
  This function should return a list of two agents that will form the
  team, initialized using firstIndex and secondIndex as their agent
  index numbers.  isRed is True if the red team is being created, and
  will be False if the blue team is being created.

  As a potentially helpful development aid, this function can take
  additional string-valued keyword arguments ("first" and "second" are
  such arguments in the case of this function), which will come from
  the --redOpts and --blueOpts command-line arguments to capture.py.
  For the nightly contest, however, your team will be created without
  any extra arguments, so you should make sure that the default
  behavior is what you want for the nightly contest.
  """
  return [eval(first)(firstIndex), eval(second)(secondIndex)]

##################
# CAPTURE AGENTS #
##################

class BaseAgent(CaptureAgent):
  """
  A base class for reflex agents that chooses score-maximizing actions
  """
 
  def registerInitialState(self, gameState):
    CaptureAgent.registerInitialState(self, gameState)
    
    self.start     = gameState.getAgentPosition(self.index)
    self.halfway   = gameState.data.layout.width / 2
    self.height    = gameState.data.layout.height
    self.lastEaten = None

    self.roamFood  = False
    self.target    = None
    self.roamIndex = 0

    self.topguard = False
    
    self.boundaries = self.getBoundaries(gameState)
    self.boundaries.sort(key=lambda x: x[1])

    half = math.floor(len(self.boundaries) / 2)
    quat = math.floor(len(self.boundaries) / 4)

    self.minguard = self.boundaries[half - quat]
    self.maxguard = self.boundaries[half + quat]

    self.moves     = []
    self.moveCount = 0
    self.kamikaze  = False

    self.simulations = 5
    self.turns = 30

  def chooseAction(self, gameState):
    """
    Picks among the actions with the highest Q(s,a).
    """
    actions = gameState.getLegalActions(self.index)

    values = [self.evaluate(gameState, a) for a in actions]

    maxValue = max(values)
    bestActions = [a for a, v in zip(actions, values) if v == maxValue]

    return random.choice(bestActions)

  def evaluate(self, gameState, action):
    """
    Computes a linear combination of features and feature weights
    """
    features = self.getFeatures(gameState, action)
    weights  = self.getWeights(gameState, action)
    return features * weights

  def getFeatures(self, gameState, action):
    """
    Returns a counter of features for the state
    """
    features  = util.Counter()
    successor = self.getSuccessor(gameState, action)
    features['successorScore'] = self.getScore(successor)
    return features

  def getWeights(self, gameState, action):
    """
    Normally, weights do not depend on the gamestate.  They can be either
    a counter or a dictionary.
    """
    return {'successorScore': 1.0}

  def getSuccessor(self, gameState, action):
    """
    Finds the next successor (Game state object)
    """
    successor = gameState.generateSuccessor(self.index, action)
    pos = successor.getAgentState(self.index).getPosition()
    if pos != nearestPoint(pos):
      return successor.generateSuccessor(self.index, action)
    else:
      return successor

  def getBoundaries(self, gameState):
    """
    Finds valid boundary positions
    """
    i = self.halfway + (-1 if self.red else 1)
    boundaries = [(int(i),int(j)) for j in range(self.height)]
    positions = [i for i in boundaries if gameState.hasWall(i[0], i[1]) is False]

    return positions
  
  def getHome(self, gameState):
    """
    Finds closest distance over boundary line
    """
    agent      = gameState.getAgentState(self.index)
    position   = agent.getPosition()
    boundaries  = self.getBoundaries(gameState)
    distances  = [self.getMazeDistance(pos, position) for pos in boundaries]

    return min(distances)

  def getGuardPosition(self):    
    return self.minguard if self.topguard else self.maxguard

  def getNearestOpponent(self, gameState):
    """
    Finds the distance to the nearest opponent
    """
    position = gameState.getAgentPosition(self.index)
    enemies  = [gameState.getAgentState(i) for i in self.getOpponents(gameState)]
    ghosts   = [g for g in enemies if not g.isPacman and g.scaredTimer < 3 and g.getPosition() is not None]

    if ghosts:
      distances = [[g, self.getMazeDistance(position, g.getPosition())] for g in ghosts]
      return min(distances, key=lambda x : x[1])

  def getInvaders(self, gameState):
    """
    Finds visible invaders
    """
    opponents = self.getOpponents(gameState)
    enemies   = [gameState.getAgentState(agentIndex) for agentIndex in opponents]
    invaders  = [e for e in enemies if e.getPosition() and e.isPacman]

    return invaders

  def getGhosts(self, gameState):
    """
    Finds visible ghosts
    """
    opponents = self.getOpponents(gameState)
    enemies   = [gameState.getAgentState(agentIndex) for agentIndex in opponents]
    ghosts    = [e for e in enemies if e.getPosition() and not e.isPacman]

    return ghosts

  def getNearest(self, position, collection):
    """
    Finds nearest tuple item in a list to a position
    """
    distances = [(c, self.getMazeDistance(position, c)) for c in collection]
    
    if distances:
      return min(distances, key=lambda x: x[1])[1]
    else:
      return 99999999

  def getLastEaten(self,gameState):
    """
    Finds last eaten food by opponent
    """
    if len(self.observationHistory) > 1:
      
      prevState   = self.getPreviousObservation()
      prevFood    = self.getFoodYouAreDefending(prevState).asList()
      currentFood = self.getFoodYouAreDefending(gameState).asList()
      
      if len(currentFood) < len(prevFood):
        for food in prevFood:
          if food not in currentFood:
            self.lastEaten = food

  def contemplateLife(self):
    """
    Find if trapped, then make the ultimate sacrifice
    """
    moves = [i for i in self.moves if i is not Directions.STOP]

    if len(moves) == 0 and self.moveCount > 1:
      self.kamikaze = True

  def roam(self, position, isPacman, opponents):
    """
    Roam border if enemy ghost nearby
    """
    if isPacman is False and opponents and opponents[1] < 5:
      self.roamFood = True

    if position == self.target:
      self.target = None

      if self.roamIndex + 1 < len(self.boundaries):
        self.roamIndex = self.roamIndex + 1
      else:
        self.roamIndex = 0

      if not opponents or opponents[1] >= 5:
        self.roamFood = False

    if self.roamFood:
      self.target = self.boundaries[self.roamIndex]

  def reset(self, position, start):
    """
    Reset fields
    """
    if position == start:
      self.roamIndex = 0
      self.roamFood = False
      self.target = None

  def executeSearch(self, problem, gameState, heuristic):
    """
    Execute a* search with a given heuristic
    """
    result  = aStar(problem, gameState, self, heuristic)
    satisfied = len(result) > 0
    final = result[0] if satisfied else Directions.STOP

    self.moves.append(final)
    self.moveCount += 1

    if len(self.moves) > 5:
      self.moves.pop(0)

    return final

  def runSimulation(self, gameState):
    """
    Execute MCTS algorithm
    """

    result = ucts_search(self.simulations, Node(MctsState(self, gameState, self.turns, [])))
    
    return result.state.parent_action 

###################
# OFFENSIVE AGENT #
###################

class OffensiveAgent(BaseAgent):
      
  def chooseAction(self, gameState):
    
    # # # # # # # # # # # # Variables # # # # # # # # # # # #

    position = gameState.getAgentPosition(self.index)
    isPacman = gameState.getAgentState(self.index).isPacman
    carrying = gameState.getAgentState(self.index).numCarrying
    scared   = gameState.getAgentState(self.index).scaredTimer
    foodList = self.getFood(gameState).asList()
    numFood  = len(foodList)

    timeLeft = gameState.data.timeleft
    distanceHome = self.getHome(gameState)
    distanceCutoff = distanceHome + 30

    opponents = self.getNearestOpponent(gameState)
    invaders  = self.getInvaders(gameState)
    nearestInvader = self.getMazeDistance(position, invaders[0].getPosition()) if invaders else None
    
    self.reset(position, self.start)
    self.roam(position, isPacman, opponents)

    if position == self.getGuardPosition():
      self.topguard = not self.topguard

    # # # # # # # # # # # # Constants # # # # # # # # # # # #

    ghostThreshold  = 5
    scaredThreshold = 30
    
    foodCutoff = 2
    maxCarry   = max(2, numFood * 0.4)

    # # # # # # # # # # # # Attacker Decision Tree # # # # # # # # # # # #

    self.contemplateLife()

    # Seppuku Branch
    if self.kamikaze:
      return self.executeSearch(Seppuku(gameState, self), gameState, martyrHeuristic)

    # Guard Branch
    if invaders and nearestInvader <= 1 and not scared:
      return self.executeSearch(GuardTerritory(gameState, self), gameState, guardHeuristic)

    # Patrol Branch
    if isPacman and opponents and not isPacman and opponents[1] < ghostThreshold:
      return self.executeSearch(Patrol(gameState, self), gameState, patrolHeuristic)

    # Escape Ghost Branch
    if isPacman and opponents and opponents[1] < ghostThreshold and opponents[0].scaredTimer < scaredThreshold:
      return self.executeSearch(EvasiveManeuver(gameState, self), gameState, evasiveHeuristic)
    
    # Run Home Branch
    if isPacman and numFood <= foodCutoff or timeLeft <= distanceCutoff or carrying >= maxCarry:
      return self.executeSearch(EscapeHome(gameState, self), gameState, escapeHeuristic)

    # Find Food Branch
    return self.executeSearch(FindFood(gameState, self), gameState, foodHeuristic)

###################
# DEFENSIVE AGENT #
###################

class DefensiveAgent(BaseAgent):
  
  def chooseAction(self, gameState):

    # # # # # # # # # # # # Variables # # # # # # # # # # # #

    position = gameState.getAgentPosition(self.index)
    scared   = gameState.getAgentState(self.index).scaredTimer
    isPacman = gameState.getAgentState(self.index).isPacman

    foodList = self.getFood(gameState).asList()
    carrying = gameState.getAgentState(self.index).numCarrying
    numFood  = len(foodList)

    if position == self.lastEaten:
      self.lastEaten = None

    self.getLastEaten(gameState)
    
    if position == self.getGuardPosition():
      self.topguard = not self.topguard

    opponents = self.getNearestOpponent(gameState)
    invaders  = self.getInvaders(gameState)

    # # # # # # # # # # # # Constants # # # # # # # # # # # #

    carryLimit = 3
    foodCutoff = 2

    # # # # # # # # # # # # Defender Decision Tree # # # # # # # # # # # #

    # Guard Branch
    if invaders and not scared:
      return self.runSimulation(gameState)

    # Track Eaten Branch
    if self.lastEaten and not scared:
        return self.executeSearch(TrackLastEaten(gameState, self), gameState, trackHeuristic)

    # Find Food Branch
    if carrying < carryLimit and not opponents and not invaders:
      return self.executeSearch(FindFood(gameState, self), gameState, foodHeuristic)  
    
    # Escape Branch
    if (carrying or isPacman) and (opponents or self.lastEaten) or (numFood <= foodCutoff and isPacman):
      return self.executeSearch(EscapeHome(gameState, self), gameState, escapeHeuristic)

    # Patrol Branch
    return self.executeSearch(Patrol(gameState, self), gameState, patrolHeuristic)

  def getFeatures(self, gameState, action):

    features = util.Counter()
    successor = self.getSuccessor(gameState, action)
    
    invaders  = self.getInvaders(successor)

    nearestInvader = self.getNearest(successor.getAgentPosition(self.index), [c.getPosition() for c in invaders])

    features['invaderDistance'] = nearestInvader if invaders else 0

    return features
  
  def getWeights(self, gameState, action):
    return { 'invaderDistance': -10 }


#####################
# MONTE CARLO STATE #
#####################

class MctsState():

  def __init__(self, agent, gameState, value=0, move = None, parent_action = None, turn=5):  
    self.gameState = gameState
    self.value     = value
    self.turn      = turn
    self.move      = move
    self.agent     = agent
    self.parent_action  = parent_action

  def getSuccessor(self, tried = None):
    """
    Get valid successors
    """
    actions    = self.getActions(tried)
    evaluation = [self.agent.evaluate(self.gameState, a) for a in actions]
    highest    = max(evaluation)
    best       = [a for a, v in zip(actions, evaluation) if v == highest]
    self.move  = random.choice([g for g in best])

    successor = self.gameState.generateSuccessor(self.agent.index, self.move)
    
    return MctsState(self.agent, successor, highest, None, self.move, self.turn - 1)
    
  def getActions(self, tried):
    """
    Get valid untried actions
    """
    actions = self.gameState.getLegalActions(self.agent.index)
    actions.remove(Directions.STOP)

    if tried:
      tried   = [t.state.parent_action for t in tried]
      actions = [n for n in actions if n not in tried]

    return actions

  def terminal(self):
    return not self.turn

#########################
# MONTE CARLO TREE NODE #
#########################

class Node():
  def __init__(self, state, parent=None):
    self.visits = 1
    self.reward = 0.0 
    self.state = state
    self.children = []
    self.parent = parent  
  
  def append(self, state):
    """
    Append node to children
    """
    self.children.append(Node(state, self))
  
  def getState(self):
    """
    Deep copy of state
    """
    return MctsState(
      self.state.agent, 
      self.state.gameState, 
      self.state.value, 
      self.state.move, 
      self.state.parent_action, 
      self.state.turn)

  def fully_expanded(self):
    """
    Finds if node is fully expanded
    """
    actions = self.state.gameState.getLegalActions(self.state.agent.index)
    actions.remove(Directions.STOP)
    
    return len(self.children) == len(actions)

#####################################
# MONTE CARLO TREE SEARCH ALGORITHM #
#####################################

def ucts_search(budget, root):
  """
  Finds best child using the MCTS UCT method
  """
  for i in range(int(budget)):
    
    head = tree_policy(root)
    
    rollback_policy(
      head, 
      default_policy(head.state))

  return best_child(root, 0)

def expand(node):
  """
  Expand node with all valid child nodes
  """
  tried=[a for a in node.children]

  node.append(node.state.getSuccessor(tried))
  node.children[-1].parent = node
 
  return node.children[-1]

def tree_policy(node):
  """
  Execute tree policy
  """
  scalar = 1 / math.sqrt(2.0)
  node = node[0] if type(node) is list else node

  while not node.getState().terminal():
    if not node.fully_expanded():  
      return expand(node)
    else:
      node = best_child(node, scalar)
  return node

def default_policy(state):
  """
  Get states value from successors
  """
  while not state.terminal():
    state = state.getSuccessor()
  return state.value

def rollback_policy(node, reward):
  """
  Rollback nodes
  """
  while node:
    node.visits += 1
    node.reward += reward + node.state.value

    node=node.parent

def best_child(node, scalar):
  """
  Find best child from possible successors
  """
  bestscore = -999999999999
  best_children = []

  for child in node.children:
    score = (child.reward / child.visits) + scalar * (equate(node.visits, child.visits))
    
    if score == bestscore:
      best_children.append(child)
    
    if score > bestscore:  
      best_children = [child]
      bestscore = score

  return random.choice(best_children) if best_children else []

def equate(node_visits, child_visits):
  """
  Calculate value for exploration
  """
  child  = float(child_visits)
  node   = math.log(2*node_visits)
  result = math.sqrt(node / child)
  return result