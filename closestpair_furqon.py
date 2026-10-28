from math import dist

def sort(points):
    pts = sorted(points)
    return solve(pts, 0, len(pts) - 1)

def solve(pts, low, high):
    if high - low <= 3:
        best = (float('inf'), None, None)
        for i in range(low, high +1):
            for j in range(i + 1, high + 1):
                d = dist(pts[i], pts[j])
                if d < best[0]:
                    best = (d, pts[i], pts[j])
        return best

    mid = (low + high) // 2
    mid_x = pts[mid][0]