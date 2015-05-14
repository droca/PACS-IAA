# -*- coding: UTF-8 -*-
# Author: daniel roca roca486@gmail.com
# PAC 3 IAA - UOC 2015

from utils import *

from libsvm import svmutil

def vectorMachine(sfile):
	y, x = svm_read_problem(sfile)
	m = svm_train(y, x, '-c 4 -t 1 -d 2')
	yt, xt = svm_read_problem(sfile)
	p_label, p_acc, p_val = svm_predict(yt, xt, m)

