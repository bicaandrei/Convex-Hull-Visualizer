def Left_index(points):

    minn = 0
    for i in range(1, len(points)):
        if points[i].x < points[minn].x:
            minn = i
        elif points[i].x == points[minn].x:
            if points[i].y > points[minn].y:
                minn = i
    return minn


def orientation(p, q, r):

    val = (q.y - p.y) * (r.x - q.x) - \
          (q.x - p.x) * (r.y - q.y)

    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2


def convexHull(points, n):
    # There must be at least 3 points
    if n < 3:
        return

    # Find the leftmost point
    l = Left_index(points)

    hull = []

    p = l
    q = 0
    while (True):

        hull.append(points[p])

        q = (p + 1) % n

        for i in range(n):
             if (orientation(points[p],points[i], points[q]) == 2):
                q = i
        p = q

        if (p == l):
            break

    return hull