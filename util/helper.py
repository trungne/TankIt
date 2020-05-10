from constants import WIN


def has_reached_vertical_boundary(rect):
    """
    Check if the given rect has reached vertical boundary

    Parameters:
        rect (pygame.Rect): pygame.Rect object to perform checking on

    Returns:
        bool:
    """
    return any([rect.top <= 0, rect.bottom <= 0, rect.top >= WIN[1], rect.bottom >= WIN[1]])


def has_reached_horizontal_boundary(rect):
    """
    Check if the given rect has reached horizontal boundary

    Parameters:
        rect (pygame.Rect): pygame.Rect object to perform checking on

    Returns:
        bool:
    """
    return any([rect.right <= 0, rect.left <= 0, rect.left >= WIN[0], rect.right >= WIN[0]])
