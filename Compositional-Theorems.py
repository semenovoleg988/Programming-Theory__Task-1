"""
1. Prove the superposition function theorem by writing a python code that accepts programs
for functions F, G1, .., Gm and returns a program for its superposition.
2. Prove the primitive recurssion theorem by writing a python code that accepts programs
for functions F, G and returns a program for its primitive recursion.
3. Prove the minimization theorem by writing a python code that accepts program
for a function F and returns a program for its minimization.
"""



def superposition(f, gs, args):
    """Approving of the superposition function theorem

    Args:
        f: function
        gs: list of functions g1, ... , gm 
    Returns:
        function for their superposition
    """
    def __superposition():
        return f(*[g(*args) for g in gs])
    return __superposition


def recursion(f, g, args, steps):
    """Approving of the primitive recurssion theorem

    Args:
        f, g: functions
    Returns:
        function for their primitive recursion
    """
    res = f(*args)

    def __recursion():
        nonlocal res, steps
        if steps > 0:
            steps -= 1
            res = g(*args, steps, __recursion())
        return res
    return __recursion


def minimization(f, args):
    """Approving of the the minimization theorem

    Args:
        f: function
        args: arguments
    Returns:
        function for its minimization
    """
    def __minimization():
        s, res = 0, 1
        while res != 0:
            res = f(*args, s)
            if res > 0:
                s += 1
        return s
    return __minimization