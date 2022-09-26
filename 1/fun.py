from scipy.optimize import linprog
import numpy as np

def Nash_Equilibrium(a):
    obj = [-1 for i in range(len(a[0]))] #уравнение для целевой функции
    rhs_ineq = [1 for i in range(len(a))]
    opt1 = linprog(c = obj, A_ub = a, b_ub=rhs_ineq, method = "simplex")
    f = 1 / sum(opt1.x)
    q = opt1.x * f
    at = np.array(a)
    at = at.transpose() * (-1)
    obj = [1 for i in range(len(at[0]))]
    rhs_ineq = [-1 for i in range(len(at))]
    opt2 = linprog(c = obj, A_ub = at, b_ub = rhs_ineq, method = "simplex")
    g = 1 / sum(opt2.x)
    p = opt2.x * g
    return f, p, q



