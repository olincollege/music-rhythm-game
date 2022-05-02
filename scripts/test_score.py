from score import score_calc
CASES_RIGHT = [
    (10, 1),
    (20, .9),
    (30, .8),
    (40, .7),
    (50, .6),
    (60, .5),
    (70, .4),
    (80, .3),
    (90, .2),
    (100, .1),
    (110, 0)
]

CASES_REST = [
    (20, 1),
    (30, .9),
    (40, .8),
    (50, .7),
    (60, .6),
    (70, .5),
    (80, .4),
    (90, .3),
    (100, .2),
    (110, .1),
    (120, 0)
]

def test_right_arrow():
    """
    Test to ensure that the right arrow cases return the correct value
    """

    for item in CASES_RIGHT:
        assert(score_calc((item[0]), "right") == item[1])

def test_rest_arrows():
    """
    Test to ensure that the rest of the arrow cases return the correct value
    """
    for item in CASES_REST:
        assert(score_calc((item[0]), "left") == item[1])