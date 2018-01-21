# Image size (pixels)
WIDTH = 1920
HEIGHT = 1080
# Plot window
RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1
MAX_ITER = 4000
noLoop()
def setup():
    background(0,0,0)
    size(WIDTH,HEIGHT)
    colorMode(HSB,100)

def draw():
    print("drawn")
    for x in range(0,WIDTH):
        for y in range(0,HEIGHT):
            drawmandel(x,y)

def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    return n

def drawmandel(x,y):
    # Convert pixel coordinate to complex number
    c = complex(RE_START + (float(x) / WIDTH) * (RE_END - RE_START),
                IM_START + (float(y) / HEIGHT) * (IM_END - IM_START))
    # Compute the number of iterations
    m = mandelbrot(c)
    # The color depends on the number of iterations
    color = 255 - int(m * 255 / MAX_ITER)
    H = int(m * 255 / MAX_ITER)
    S = 255
    V = 0 
    if (m < MAX_ITER):
        V = 255 
    # Plot the point
    stroke(H,S,V)
    point(x,y)