# python3
import sys


def compute_min_refills(distance, tank, stops):
    startPoint = 0
    noOfRefill = 0
    travelDistance = 0
    stops.append(distance)


    n = len(stops)
    # if distance <= tank: return -1
  
    for  i in range(n):
        # print("I: ",i)
        if stops[i] - startPoint <=tank:
            travelDistance = stops[i]
            # print("TRAVEL : ",travelDistance)
        elif stops[i] - startPoint > tank:
            noOfRefill += 1
            startPoint = stops[i-1]
            # print("LAST REFILL POINT: ",startPoint)

            travelDistance  = stops[i]
            # print("TRAVEL : ",travelDistance)

        if travelDistance - startPoint <= tank:
            pass
        else:
            return -1

    return noOfRefill

if __name__ == '__main__':
    # d, m, _, *stops = map(int, input().split())
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
