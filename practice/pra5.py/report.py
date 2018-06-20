def get_description():
    """this function returns a weather randomly
    like a professional weather forecaster."""
    from random import choice
    possibilities=['rain','snow','sleet','fog','sun','who knows']
    return choice(possibilities)
