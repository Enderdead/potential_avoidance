from math import atan2


# Faire le convexe
# Faire le clock wise

def is_anti_clock_wise(polygon):
    """Return True if the polygon defined by the sequence of 2D
    points is ordered on anticlockwise.
    """
    center = sum(map(lambda pt : pt[0], polygon), 0)/len(polygon), sum(map(lambda pt : pt[1], polygon), 0)/len(polygon)
    for pt1, pt2 in  zip(polygon, polygon[1:] + [polygon[0],]):
        edge_vec   = (pt2[0]-pt1[0], pt2[1]-pt1[1])
        center_vec = (center[0]-pt1[0], center[1]-pt1[1])
        vector_product = center_vec[0]*edge_vec[1] - edge_vec[0]*center_vec[1]
        if vector_product>0:
            return False
    return True


def is_convex_polygon(polygon):
    """Return True if the polygon defined by the sequence of 2D
    points is 'strictly convex': points are valid, side lengths non-
    zero, interior angles are strictly between zero and a straight
    angle, and the polygon does not intersect itself.

    NOTES:  1.  Algorithm: the signed changes of the direction angles
                from one side to the next side must be all positive or
                all negative, and their sum must equal plus-or-minus
                one full turn (2 pi radians). Also check for too few,
                invalid, or repeated points.
            2.  No check is explicitly done for zero internal angles
                (180 degree direction-change angle) as this is covered
                in other ways, including the `n < 3` check.
    """
    try:  # needed for any bad points or direction changes
        # Check for too few points
        if len(polygon) < 3:
            return False
        # Get starting information
        old_x, old_y = polygon[-2]
        new_x, new_y = polygon[-1]
        new_direction = atan2(new_y - old_y, new_x - old_x)
        angle_sum = 0.0
        # Check each point (the side ending there, its angle) and accum. angles
        for ndx, newpoint in enumerate(polygon):
            # Update point coordinates and side directions, check side length
            old_x, old_y, old_direction = new_x, new_y, new_direction
            new_x, new_y = newpoint
            new_direction = atan2(new_y - old_y, new_x - old_x)
            if old_x == new_x and old_y == new_y:
                return False  # repeated consecutive points
            # Calculate & check the normalized direction-change angle
            angle = new_direction - old_direction
            if angle <= -pi:
                angle += TWO_PI  # make it in half-open interval (-Pi, Pi]
            elif angle > pi:
                angle -= TWO_PI
            if ndx == 0:  # if first time through loop, initialize orientation
                if angle == 0.0:
                    return False
                orientation = 1.0 if angle > 0.0 else -1.0
            else:  # if other time through loop, check orientation is stable
                if orientation * angle <= 0.0:  # not both pos. or both neg.
                    return False
            # Accumulate the direction-change angle
            angle_sum += angle
        # Check that the total number of full turns is plus-or-minus 1
        return abs(round(angle_sum / TWO_PI)) == 1
    except (ArithmeticError, TypeError, ValueError):
        return False  # any exception means not a proper convex polygon



if __name__ == "__main__":
    poly = [(1394.6978243262165, 2030.9257645897196), (1073.2561421503617, 1890.9430965453953), (1010.9620073660711, 1708.8651986190257), (1052.4208758458608, 1523.5196689446702), (1301.3760456300006, 1413.9651165425128), (1500.0, 1500.0), (1736.877679545675, 1636.9004767612514), (1762.8003958501793, 1911.681269588999), (1638.371357588558, 2051.6639376333233)]
    
    print(is_anti_clock_wise(poly))