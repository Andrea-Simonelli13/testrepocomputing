
import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline


class ProbabilityDensityFunction(InterpolatedUnivariateSpline):
    def __init__(self, x, y, k=1):
        self._x = x
        self._y = y
        #self._spline = InterpolatedUnivariateSpline(x, y)
        super().__init__(x, y, k=k)
        _y = self._y.cumsum()
        _y /= _y[-1]
        self.cdf = InterpolatedUnivariateSpline(x, _y)
        self.ppf = InterpolatedUnivariateSpline(_y, x, k=1)

    def rvs(self, size=1):
        rng = np.random.default_rng()  # crea un generatore
        return self.ppf(rng.uniform(0., 1., size))
        #return self.ppf(np.random.uniform(0., 1., size))    

    # def __call__(self, x):
    #     return self._spline(x)    
    
    # def integral(self, x1, x2):
    #     return self._spline.integral(x1, x2)
    
    def plot(self):
        x=np.linspace(self._x.min(), self._x.max(), 200)
        plt.plot(x, self(x))
        


x = np.linspace(0., 1., 10)
y= 2. *x 
pdf = ProbabilityDensityFunction(x, y, k=1)  

assert np.allclose(pdf(0.5), 1.)
assert np.allclose(pdf.integral(0., 1.), 1)
plt.figure()
pdf.plot()
plt.plot(x, pdf.cdf(x))
plt.grid(True, which="both")
plt.figure()
plt.hist(pdf.rvs(10000), 100)
plt.show()