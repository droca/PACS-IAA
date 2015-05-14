# -*- coding: UTF-8 -*-
# Author: daniel roca roca486@gmail.com
# PAC 3 IAA - UOC 2015

from utils import *

def deuclidea(x, y):
   return sum(map(lambda a, b: (float(a) - float(b)) ** 2, x, y)) ** (1 / 2)

def comptar(l):
   p = {}
   for x in l:
      p.setdefault(x, 0)
      p[x] += 1
   return p

def classifyknn(t,train, classTrain):
  k=3
  ds = list(map(deuclidea, train, [t for x in range(len(train))]))
  kcl = comptar([sorted([(ds[i], classTrain[i]) for i in range(len(train))],
    key=lambda x: x[0])
  [i][1] for i in range(k)])
  return max([(x , kcl[x]) for x in kcl.keys()],key=lambda x: x[1])[0]

def knn(dades):

  # Build the training, 2 out of 3
  train = training(dades)
  

  # construccio del test: 1 de cada 3
  test = list(map(lambda x: x[1],
                  filter(lambda v: v[0] % 3 == 0, enumerate(dades))))
  classesTest = list(map(lambda x: x.pop(), test))

  # Classificacio
  prediccions = list(map(classifyknn, test,[train], [classesTrain(train)]))   

  #prediction = [classifyknn(train) for x in test]

  # Nombre de correctes
  print('kNN Prec.:', len(list(filter(lambda x: x[0] == x[1],
                                  zip(*[prediccions, classesTest]))))
                  / len(test) * 100, '%')
