def search(a,b,t):
    lower = 0
    upper = b
    h = (a ** 2 - (b / 2) ** 2) ** 0.5
    while True:
        l = (lower + upper) / 2
        if abs(l**2 - square(l,a,h,b)) < t:
            return l
        elif (l**2 - square(l,a,h,b)) < 0:
            lower = l 
        elif (l**2 - square(l,a,h,b)) > 0:
            upper = l
def square(l,a,h,b):
    return ((1/2*b*h) - ((h - l) * l / 2 + (b - l) * l / 2))
a, b, t = map(float,input().strip().split())
print(search(a, b, t))
