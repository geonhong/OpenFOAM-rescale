#!/usr/bin/env python3

import os, sys
import argparse

from math import pi

parser = argparse.ArgumentParser(description='Average the forces and moments')
parser.add_argument('--nSamples', 
                    metavar='N',
                    type=int, 
                    default=720,
                    help='number of samples to take average')
parser.add_argument('--forcename', 
                    metavar='word',
                    type=str,
                    default='forces',
                    help='the name of force and moment to measure')
parser.add_argument('--timename', 
                    metavar='N',
                    type=str,
                    default='0',
                    help='the initial time of force and moment')

args = parser.parse_args()

forceName = args.forcename
timeName = args.timename

forceFile = open('postProcessing/'+forceName+'/'+timeName+'/force.dat', 'r')
momentFile = open('postProcessing/'+forceName+'/'+timeName+'/moment.dat', 'r')

forceData = forceFile.readlines()
momentData = momentFile.readlines()

fxsum = 0.0
fysum = 0.0
fzsum = 0.0
mxsum = 0.0
mysum = 0.0
mzsum = 0.0
nSamples = args.nSamples

# Print summary
print('''
Average the forces and moments
------------------------------
- force name: ''' + forceName + '''
- time name : ''' + timeName + '''
- Samples   : ''' + str(nSamples) + '''
''')

omg = 0.0

for i in range(1, nSamples+1):
    f = forceData[-i]
    m = momentData[-i]

    if f[0] == '#':
        # skip comment
        pass

    f = f.replace('(','').replace(')','').split()
    fx = float(f[1])
    fy = float(f[2])
    fz = float(f[3])
    fxsum += fx
    fysum += fy
    fzsum += fz

    m = m.replace('(','').replace(')','').split()
    mx = float(m[1])
    my = float(m[2])
    mz = float(m[3])
    mxsum += mx
    mysum += my
    mzsum += mz

fxave = fxsum/nSamples
fyave = fysum/nSamples
fzave = fzsum/nSamples
mxave = mxsum/nSamples
myave = mysum/nSamples
mzave = mzsum/nSamples

print('Averaged Fx : ', fxave, ' N')
print('Averaged Fy : ', fyave, ' N')
print('Averaged Fz : ', fzave, ' N')
print('Averaged Mx : ', mxave, ' N-m')
print('Averaged My : ', myave, ' N-m')
print('Averaged Mz : ', mzave, ' N-m')
