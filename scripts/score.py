def score(y_position, arrow_type):
    """
    Function to determine the score a player recieves after they stop the arrow
    from moving

    Arguments:
        -y_position: an integer value representing the y-position of the arrow
                     when the player stopped it.
        -arrow_type: a string representing the type of arrow (left, right, down,
                     up)
    
    Returns:
        -score: the score gained (will need to be added on total score in main 
                function)
    """

    
    if arrow_type == "right":
        ARROW_POSITION = 10
    else:
        ARROW_POSITION = 20

    diff = abs(ARROW_POSITION - y_position)

    score = 0

    if diff == 0:
        score += 1
    elif diff > 0 and diff <= 10:
        score += .9
    elif diff > 10 and diff <= 20:
        score += .8
    elif diff > 20 and diff <= 30:
        score += .7
    elif diff > 30 and diff <= 40:
        score += .6
    elif diff > 40 and diff <= 50:
        score += .5
    elif diff > 50 and diff <= 60:
        score += .4
    elif diff > 60 and diff <= 70:
        score += .3
    elif diff < 70 and diff <= 80:
        score += .2
    elif diff < 80 and diff <= 90:
        score += .1

    return score