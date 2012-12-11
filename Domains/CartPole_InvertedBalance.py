import sys, os
#Add all paths
sys.path.insert(0, os.path.abspath('..'))
from Tools import *
from Domain import *
from CartPole import *

#####################################################################
# Robert H. Klein, Alborz Geramifard at MIT, Nov. 30 2012
#####################################################################
# (See CartPole implementation in the RL Community,
# http://library.rl-community.org/wiki/CartPole)
#
# ---OBJECTIVE---
# Reward is 0 everywhere, -1 if x or theta exceeds bounds.
# This is also the terminal condition.
#
# RL Community has the following bounds for failure:
# theta: [-12, 12] degrees  -->  [-pi/15, pi/15]
# x: [-2.4, 2.4] meters
#
# Pendulum starts straight up, theta = 0, with the
# cart at x = 0.
# (see CartPole parent class for coordinate definitions).
#
# Note that the reduction in angle limits affects the resolution
# of the discretization of the continuous space.
#
# Note that if unbounded x is desired, set x (and/or xdot) limits to
# be [float("-inf"), float("inf")]
#
#####################################################################

class CartPole_InvertedBalance(CartPole):
    
    GOAL_EXIT_REWARD    = -1 		 	# Reward for exiting the goal region
    ANGLE_LIMITS        = [-pi/15, pi/15] # rad - Limits on pendulum angle per RL Community CartPole (NOTE we wrap the angle at 2*pi)
    ANGULAR_RATE_LIMITS = [-6*pi, 6*pi] # Limits on pendulum rate [per RL Community CartPole]
    POSITON_LIMITS 		= [-2.4, 2.4] 	# m - Limits on cart position [Per RL Community CartPole]
    VELOCITY_LIMITS 	= [-6.0, 6.0] 	# m/s - Limits on cart velocity [per RL Community CartPole]   

    episodeCap          = 3000      # Max number of steps per trajectory
    
    def __init__(self, logger = None):
        self.statespace_limits  = array([self.ANGLE_LIMITS, self.ANGULAR_RATE_LIMITS, self.POSITON_LIMITS, self.VELOCITY_LIMITS])
        super(CartPole_InvertedBalance,self).__init__(logger)
    
    def s0(self):    
        # Returns the initial state, pendulum vertical
        return array([0,0,0,0])
    
    def _getReward(self, s, a):
        # Return the reward earned for this state-action pair
        return self.GOAL_EXIT_REWARD if self.isTerminal(s) else 0
    
    def isTerminal(self,s):
        return (not (-pi/15 < s[StateIndex.THETA] < pi/15) or \
                not (-2.4    < s[StateIndex.X]     < 2.4))


if __name__ == '__main__':
    random.seed(0)
    p = CartPole_InvertedBalance();
    p.test(1000)
    