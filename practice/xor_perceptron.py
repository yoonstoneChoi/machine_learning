import numpy as np

def XOR_gate_layer(x1, x2):
    w1_or=0.6
    w2_or=0.6
    w1_nand = -0.5
    w2_nand = -0.5
    b_or = -0.5
    b_nand = 0.7
    print(x1, x2)
    result_or = x1*w1_or + x2*w2_or + b_or
    print('result_or :',result_or)
    result_nand = x1*w1_nand + x2 * w2_nand + b_nand
    print('result_nand :',result_nand)

    if result_or <= 0 or result_nand <=0:
        return 0
    else:
        return 1


print(XOR_gate_layer(0,1))
print(XOR_gate_layer(1,0))
print(XOR_gate_layer(1,1))
print(XOR_gate_layer(0,0))

