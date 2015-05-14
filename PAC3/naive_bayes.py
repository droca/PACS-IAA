# -*- coding: UTF-8 -*-
# Author: daniel roca roca486@gmail.com
# PAC 3 IAA - UOC 2015

# Naïve Bayes

from functools import reduce
from utils import *

FILE = 'Wholesale_customers.txt'
# declaracio de funcions
def comptar(l):
   p = {}
   for x in l:
      p.setdefault(x, 0)
      p[x] += 1
   return p
   
def comptar2(l, k):
   p = {}
   for i in range(len(l)):
      p.setdefault(k[i], {})
      p[k[i]].setdefault(l[i], 0)
      p[k[i]][l[i]] += 1
   return p

def Pxik(atr, N, k, Nk,n):
   if atr in N[k]:
      return N[k][atr] / Nk[k]
   else:
      return Nk[k] / n ** 2

def classify(t, Nk,n,Nxik):
   l = [(k , Nk[k] / n *
        reduce(lambda x, y: x * y,
               map(Pxik, t, Nxik,
                   [k for a in range(len(t))],[Nk],[n])))
        for k in Nk.keys()]
   return max(l, key=lambda x: x[1])[0]

def naiveBayes(dades):

  train = training(dades)
  n = len(train)

  # construccio del test: 1 de cada 3
  test = list(map(lambda x: x[1],
                  filter(lambda v: v[0] % 3 == 0, enumerate(dades))))

  # transposta del training
  m = list(zip(*train))

  # Numerador de P(k)
  Nk = comptar(m[0])

  # Numerador de P(xi|k)
  Nxik = [comptar2(m[i], m[0]) for i in range(1, len(m))]

  # Classificacio
  classes = list(map(lambda x: x.pop(), test))
  prediccions = list(map(classify, test,[Nk],[n],[Nxik]))   

  # Nombre de correctes
  print('Prec.:', len(list(filter(lambda x: x[0] == x[1],
                                  zip(*[prediccions, classes]))))
                  / len(test) * 100, '%')

