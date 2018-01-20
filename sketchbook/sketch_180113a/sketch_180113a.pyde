def setup():
    noSmooth()
    x = 200
    y = 200
    size(x,y)
    
def draw():
    MAX_ITER = 100
    def mandelbrot(c):
         z = 0
         n = 0
         while abs(z) <= 2 and n < MAX_ITER:
             z = z*z + c
             n = n + 1
        return n