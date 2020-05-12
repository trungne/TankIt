from constants import WIN


def out_of_horizontal_axis(rect) -> bool:
    """Check if the given rect has reached horizontal boundary.

    Parameters:
        rect (pygame.Rect): pygame.Rect object to perform checking on
    """
    return any([rect.top <= 0, rect.bottom <= 0, rect.top >= WIN[1], rect.bottom >= WIN[1]])


def out_of_vertical_axis(rect) -> bool:
    """Check if the given rect has reached vertical boundary.

    Parameters:
        rect (pygame.Rect): pygame.Rect object to perform checking on
    """
    return any([rect.right <= 0, rect.left <= 0, rect.left >= WIN[0], rect.right >= WIN[0]])
