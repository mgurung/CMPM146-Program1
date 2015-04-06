from p1_support import load_level, show_level
from math import sqrt
from heapq import heappush, heappop

def dijkstras_shortest_path(src, dst, graph, adj): 

	curr_dist = {} #initialize dic for current distance
	prev_dist = {} #initialize dic for prev distance

	curr_dist[src] = 0
	prev_dist[src] = None

	pq = [] #initialize queue

	heappush(pq, (src, 0)) #push source cell to queue with distance of 0

	while not len(pq) == 0:

		curr_cell, distance = heappop(pq) #pop lowest out of queue

		if curr_cell == dst: #check if the current cell is our destination and if it is, break
			break

		neighbors = adj(graph, curr_cell) #get neighboring cells

		for neighbor_cell, neighbor_distance in neighbors: #iterate through neighbors 

			path_len = distance + neighbor_distance #calculate current path distance 
			
			if neighbor_cell not in curr_dist or path_len < curr_dist[neighbor_cell]:
				curr_dist[neighbor_cell] = path_len
				prev_dist[neighbor_cell] = curr_cell
				heappush(pq, (neighbor_cell, path_len))
		
	if curr_cell == dst:
		path = []
		while curr_cell:
			path.append(curr_cell)
			curr_cell = prev_dist[curr_cell]
		path.reverse()
		return path
	else:
		return []


def navigation_edges(level, cell):

  	edges = []
	x, y = cell

	for dx in [-1,0,1]:
		for dy in [-1,0,1]:
			next_cell = (x + dx, y + dy)
			dist = sqrt(dx*dx+dy*dy)

			if dist > 0 and next_cell in level['spaces']:
				#print dist
				edges.append((next_cell, dist))

	return edges

def test_route(filename, src_waypoint, dst_waypoint):

	level = load_level(filename)

	show_level(level)

	src = level['waypoints'][src_waypoint]
	dst = level['waypoints'][dst_waypoint]

	path = dijkstras_shortest_path(src, dst, level, navigation_edges)

	if path:
		show_level(level, path)
	else:
		print "No path possible!"

if __name__ ==  '__main__':
	import sys
	_, filename, src_waypoint, dst_waypoint = sys.argv
	test_route(filename, src_waypoint, dst_waypoint)