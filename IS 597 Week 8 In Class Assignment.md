# IS 597 Week 8 In Class Assignment

Members: Vel (Tien-Yun) Wu (tienyun2), Sam Walkow (swalkow2)

Notes about game play:
- at least two loops where needed to win the game
- could not back up (had to be in forward gear), could not turn around, could not go the wrong way down a one way street (it would cause a traffic violation)
- One possible solution
    - had to reach the southern block of nodes and had to follow one path to reach the end.

1. "How many total combinations are there for an intersection in the middle of town?"

- For each intersection with x directions, look at the adjacent nodes and their possible directions which could be 2~4

- Given the requirement to always move forward, when taking any single intersection, driving in from 1 direction, we have 2 to the 3rd = 8 possibilities from the intersection. This could then be multiplied by the 4 directions which nets a total of 32 combinations. 

2. NetworkX library's DiGraph approach
- Each intersection is a node
- Each edge denotes legal routes to the adjacent nodes
- Illegal routes are ignored and never recorded in the graph
- No weights are required as legal routes would be represented by edges
- add node attributes so we know which direction we're coming from, to help determine which legal directions we have at available

![](https://i.imgur.com/EgM3AcU.png)


![](https://i.imgur.com/RzyY4Qz.png)

![](https://i.imgur.com/vYb1hA3.png)

- This may not prevent U-turns, so locations between crossings will also be added as pairs of nodes
- Then add edges as can be attached to a node going in one direction on one side of the 'street'. A second set of edges can be attached to nodes going the other direction. This way, we can stop going in an illegal when we need to, because that node will not have an edge to go in an illegal direction or make a u-turn.
- this keeps you on one side of the road, going in forward motion, so the loop never includes a u-turn.

![](https://i.imgur.com/7Zj0lTv.png)


3. A data structure to achieve the same purpose. Also encoded for a couple of intersections.

![](https://i.imgur.com/ZkegzoD.png)

- (1) Create each intersection as a Intersection() class instance:
    - Attributes can be assigned as next_intersection
    - additional attributes for intersection coordinates and to connect nodes (in a list)
- (2) Have methods to append traveled nodes to a list in the global space
- (3) Call indices [-1] and [-2] on the list when moving, check whether they are identical to the current node being traveled. This should prevent U-turns in an algorithmic sense. 
