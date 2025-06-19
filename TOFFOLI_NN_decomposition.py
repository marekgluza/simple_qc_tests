import scipy
import numpy as np
from qibo.symbols import *
def TOFFOLI_circuit_NN(c = None, q0 = 0,q1 = 1,q2 = 2):

    if c is None:
        c = Circuit(3)

    pi = np.pi

    c.add(gates.RX(q0,theta = -pi ))
    c.add(gates.RX(q1,theta = pi/2 ))
    c.add(gates.RZ(q2,theta = pi/2 ))
    c.add(gates.RX(q2,theta = pi/2 ))

    c.add(gates.CZ(q1,q2))

    c.add(gates.RX(q1,theta = -pi ))
    c.add(gates.RX(q2,theta = -pi ))

    c.add(gates.CZ(q0,q1))

    c.add(gates.RX(q0,theta = pi/2 ))
    c.add(gates.RX(q1,theta = pi/2 ))

    c.add(gates.CZ(q0,q1))

    c.add(gates.RZ(q0,theta = -pi/2 ))
    c.add(gates.RX(q0,theta = pi/4 ))
    c.add(gates.RZ(q1,theta = pi/4 ))
    c.add(gates.RX(q1,theta = pi/2 ))

    c.add(gates.CZ(q1,q2))

    c.add(gates.RX(q1,theta = pi/2 ))
    c.add(gates.RX(q2,theta = -pi ))

    c.add(gates.CZ(q0,q1))

    c.add(gates.RZ(q0,theta = -pi ))
    c.add(gates.RX(q0,theta = pi/4 ))
    c.add(gates.RZ(q1,theta = -pi/4 ))
    c.add(gates.RX(q1,theta = pi/2 ))

    c.add(gates.CZ(q0,q1))

    c.add(gates.RZ(q0,theta = -pi ))
    c.add(gates.RX(q0,theta = pi/2 ))
    c.add(gates.RX(q1,theta = pi/2 ))

    c.add(gates.CZ(q1,q2))

    c.add(gates.RX(q1,theta = pi/2 ))
    c.add(gates.RZ(q2,theta = -pi/4 ))
    c.add(gates.RX(q2,theta = pi/2 ))
    c.add(gates.RZ(q2,theta = pi/2 ))

    c.add(gates.CZ(q0,q1))

    c.add(gates.RZ(q0,theta = -pi/2 ))
    c.add(gates.RX(q0,theta = pi/2 ))
    c.add(gates.RZ(q0,theta = -pi/4 ))
    c.add(gates.RZ(q1,theta = -pi/2 ))
    c.add(gates.RX(q1,theta = pi/2 ))
    c.add(gates.RZ(q1,theta = -3*pi/4 ))
    return c

def test_TOFFOLI():
    c =TOFFOLI_circuit_NN()
    -(c.unitary()*np.exp(1j*5.10645)).real