#-------------------------------------------#
#               Modules
#-------------------------------------------#

import random

print(random)
print(f"random = {random.random()}")#lock likerandom = 0.6839147145619241
print(dir(random))#['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_ONE', '_Sequence', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_fabs', '_floor', '_index', '_inst', '_isfinite', '_lgamma', '_log', '_log2', '_os', '_parse_args', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', 'betavariate', 'binomialvariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'main', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']

from random import randint,randrange,random

print(randint(100,900))
print(randrange(100,900))
print(random())


import mod
print(dir(mod))
mod.setname("abd")
mod.sayHello()


from mod import setage
setage(21)


mod.details()






#----------------------------------------------#
#             Install External Packages        #
#----------------------------------------------#

#----------------------------------------------------------------------------
#[1] Modules Vs packages
#[2] External package Downloaded From Internet
#[3] You can install package with python package manager PIP
#[4] PIP install the package and its dependencies
#[5] Modules List "https://docs.python.org/3/py-modindex.html"
#[6] packages and Modules Directory "https://pypi.org/"
#[7] PIP Manual "https://pip.pypa.io/en/stable/reference/pip_install/"
#----------------------------------------------------------------------------

import termcolor
import pyfiglet

print(dir(pyfiglet))
print(pyfiglet.figlet_format("a b d "))
print(termcolor.colored("a b d",color="yellow"))

print(termcolor.colored(pyfiglet.figlet_format("a b d"),color="yellow"))





