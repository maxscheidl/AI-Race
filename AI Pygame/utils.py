import math


# O(1)
def lerp(a, b, t):
    return a + (b - a) * t


# O(1)
def ray_length_scale(rayCount, i):

    if rayCount % 2 == 0:
        return 1 - math.fabs(((rayCount / 2) + 0.5 - (i + 1)) * 1.5 / rayCount)
    else:
        return 1 - math.fabs(((rayCount / 2.0) + 0.5 - (i + 1)) * 1.5 / rayCount)


# O(1)
def get_ray_color(offset):

    if offset > 0.7:
        return "pink"
    elif offset > 0.6:
        return "red"
    else:
        return "darkred"


# O(1)
def get_intersection(a, b, c, d):

    tTop = (d[0] - c[0]) * (a[1] - c[1]) - (d[1] - c[1]) * (a[0] - c[0])
    uTop = (c[1] - a[1]) * (a[0] - b[0]) - (c[0] - a[0]) * (a[1] - b[1])
    bottom = (d[1] - c[1]) * (b[0] - a[0]) - (d[0] - c[0]) * (b[1] - a[1])

    if bottom != 0:
        t = tTop / bottom
        u = uTop / bottom

        if (t >= 0) & (t <= 1) & (u >= 0) & (u <= 1):
            return [
                (lerp(a[0], b[0], t), lerp(a[1], b[1], t)),
                t
            ]

    return []


# O(n)
def find_min_offset(intersections):
    min_offset_intersection = intersections[0]

    for intersection in intersections:
        if min_offset_intersection[1] > intersection[1]:
            min_offset_intersection = intersection

    return min_offset_intersection


# O(n*m)
def polynom_intersection(pol1, pol2):
    for i in range(len(pol1)):
        for j in range(len(pol2)):
            intersection = get_intersection(
                pol1[i],
                pol1[(i + 1) % len(pol1)],
                pol2[j],
                pol2[(j + 1) % len(pol2)]
            )

            if len(intersection) != 0:
                return True

    return False


