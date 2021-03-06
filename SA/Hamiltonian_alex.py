'''
Created on Sep 1 , 2016

@author: Alexandre Day
'''
from quspin.operators import hamiltonian
from quspin.basis import spin_basis_1d
import numpy as np

def Hamiltonian(L,J,hz,hx,fct=None):
	
	#basis = spin_basis_1d(L=L,pauli=False)
	fct_arg=[]		
	ones=[[-1,i] for i in range(L)]
	z_field=[[-hz,i] for i in range(L)]

	if L>1:
		basis = spin_basis_1d(L=L,pauli=False,kblock=0,pblock=1)
		zz_int =[[-J,i,(i+1)%L] for i in range(L)] # Has periodic boundary conditions
		static = [["zz",zz_int], ["z",z_field]]
	else:
		basis = spin_basis_1d(L=L,pauli=False)
		static = [["z", z_field]]
		
	dynamic = [["x",ones,fct,fct_arg]]
	
	kwargs = {'dtype':np.float64,'basis':basis,'check_symm':False,'check_herm':False,'check_pcon':False}
	
	return hamiltonian(static,dynamic,**kwargs), basis
