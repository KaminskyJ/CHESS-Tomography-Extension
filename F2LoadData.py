#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 09:08:56 2018

@author: jk989
"""
#==============================================================================
# %% INPUT
#==============================================================================
"""Input the names of the tdf, tbf, and tomo data folders, and the directory 
of the tomoFunctions module.

Then chose the directory and name of the output data.

ie:
tdfDataFolder='/nfs/chess/raw/2018-1/f2/hurley-698-3/conccube3/6/nf/'
tbfDataFolder='/nfs/chess/raw/2018-1/f2/hurley-698-3/conccube3/7/nf/'
tomoDataFolder='/nfs/chess/raw/2018-1/f2/hurley-698-3/conccube3/8/nf/'
moduleFolder = '/nfs/chess/aux/user/jk989/ver\ 1.0.1/'
saveOutputName = '/nfs/chess/aux/user/jk989/mydata'
"""
tdfDataFolder='' #TODO
tbfDataFolder='' #TODO
tomoDataFolder='' #TODO
moduleFolder = '' #TODO
saveOutputName = '' #TODO

#==============================================================================
# %% IMPORT
#==============================================================================
"""Import tomoFunctions"""
import sys
sys.path.append(moduleFolder)
import numpy as np
import tomoFunctions as tf

#==============================================================================
# %% LOAD DATA
#==============================================================================
"""Process tomoImgs and theta."""
tdf = tf.genDark(tdfDataFolder)
tbf = tf.genBright(tbfDataFolder, tdf)
intCorr = tf.getIntCorr(tomoDataFolder)
tomoImgs = tf.genTomo(tomoDataFolder, tdf, tbf, intCorr)
theta = tf.getTheta(tomoDataFolder)

#==============================================================================
# %% SAVE DATA
#==============================================================================
"""Save the data into an hdf5."""
tf.save(saveOutputName + '.hdf5',['sinograms','theta'],[tomoImgs, theta])