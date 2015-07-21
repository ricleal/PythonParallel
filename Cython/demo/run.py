"""
First run:

python setup.py build_ext --inplace

Then:

python run.py

"""

import my_package

print "Fib result:", my_package.fib(20)

print "Integration result of f:", my_package.integrate_f(10,50,100)
