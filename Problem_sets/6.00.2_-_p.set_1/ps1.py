###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    result = []
    # helper function to sort cows in ascending order
    def sort_cows(cow_dict):
        temp = [(name, weight) for name, weight in cow_dict.items()]        
        for i in range(len(temp) - 1, 0, -1):
            target = i
            for j in range(i):
                if temp[j][-1] > temp[target][-1]:
                    target = j
            temp[i], temp[target] = temp[target], temp[i]
        return temp
    
    sorted_cows = sort_cows(cows)
    
    while True:
        current_weight = 0
        targets = []
        for i in range(len(sorted_cows) - 1, -1, -1):
            if sorted_cows[i][-1] + current_weight <= limit:
                cow = sorted_cows.pop(i)
                targets.append(cow[0])
                current_weight += cow[-1]
        result.append(targets)
        if len(sorted_cows) == 0 or sorted_cows[0][-1] > limit:
                break
    return result


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    valid = []
    cow_list = list(cows.keys())
    
    # helper function checks if is trip in partition is valid
    def is_valid(partition):
        for trip in partition:
            total_weight = 0
            for cow in trip:
                total_weight += cows[cow]
                if total_weight > limit:
                    return False
        return True
            
    for partition in (get_partitions(cow_list)):
        if is_valid(partition):
            valid.append(partition)
    
    for i in range(1, len(cow_list) + 1):
        for partition in valid:
            if len(partition) == i:
                return partition

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows("ps1_cow_data.txt")
    
    # greedy
    start_greedy = time.time()
    greedy = greedy_cow_transport(cows)
    end_greedy = time.time()
    print(f'\nGreedy algo trips = {len(greedy)}')
    print(f'Greedy algo runtime = {end_greedy - start_greedy}\n')
    
    #bruteforce
    start_bf = time.time()
    bruteforce = brute_force_cow_transport(cows)
    end_bf = time.time()
    print(f'Bruteforce algo trips = {len(bruteforce)}')
    print(f'Bruteforce algo runtime = {end_bf - start_bf}')


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10

print(greedy_cow_transport(cows, limit))

print(brute_force_cow_transport(cows, limit))

compare_cow_transport_algorithms()