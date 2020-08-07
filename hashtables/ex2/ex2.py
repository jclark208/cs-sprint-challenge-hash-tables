#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = [None] * length
    cache = {}
    for ticket in tickets:
        cache[ticket.source] = ticket.destination
    something = cache["empty"]
    for curr_num in range(0,length):
        route[curr_num] = something
        something = cache[something]

    return route
