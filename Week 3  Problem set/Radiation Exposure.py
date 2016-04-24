def radiationExposure(start, stop, step):
        add=0.0
        dup =int((stop-start)/step)
        for i in range(dup):
                add = add+step*f(start)
                start += step
        return add

