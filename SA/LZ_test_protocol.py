'''
Created on Jan 2 , 2017

@author: Alexandre Day

Purpose:
    This module is just for testing protocols

'''

import LZ_sim_anneal as LZ
import time

hx_tmp=[-4.,4.,4.,-4.,4.,-4.]
action_set=[-8.,0.,8.]

standard_eval=LZ.custom_protocol(delta_t=0.05,option='standard')
LZ.custom_protocol(J=-1.0,L=4,hz=1.0,hx_init_state=-2.0,hx_target_state=2.0,
                    delta_t=0.05,hx_i=-4.,hx_max=4.,action_set_=[-8.,0.,8.],
                    option='standard')
exit()                    
fast_eval=LZ.custom_protocol(delta_t=0.05,option='fast')

start=time.time()
print(standard_eval.evaluate_protocol_fidelity(hx_tmp))
print("Standard run in %.6f"%(time.time()-start))

start=time.time()
print(fast_eval.evaluate_protocol_fidelity(hx_tmp))
print("Fast ran in %.6f"%(time.time()-start))
