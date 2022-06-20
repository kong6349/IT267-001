"""from measure_convert import c_to_n,n_to_c

if __name__=='__main__':
    degree = float(input('กรอกเลข: '))
    print('-----------------')
    print(f'{degree} เซนติเมตร = {c_to_n(degree):.2f} นิ้ว')
    print(f'{degree} นิ้ว = {n_to_c(degree):.2f} เซนติเมตร')"""

import measure_convert as mc
if __name__=='__main__':
    print(mc.n_to_c(5))
    print(mc.c_to_n(6))