# CHESS Tomography Extension Procedure 1.0.

## Overview

This module is an extension for tomopy 1.0.1. It allows users to process raw tomographic data
through automation and GUIs.

It is designed to decrease the amount of variables necessary to complete reconstructions and increase
ease of use, while still maintaining the flexability of tomopy.

By reading this manual and using the template, a new user should be able to complete a full
reconstruction with no edits to any code besides the initial inputs.

## Dependencies

```
Software Version
python 2.7.
tomopy 1.0.
matplotlib 2.1.
ipython 5.4.
h5py 2.7.
```
## Initial Data Format

There are two pieces of data that must be loaded in order for proper reconstruction: the tomographic
image stack, and theta values for the stack. These should be in the format [elements, rows, angles,
columns] and [radians] respectively.

This data should be packaged into an hdf5 file as seperate data sets. This can be done using
the save() method included in this module.


## Contact

Any questions or suggestions can be sent to jk989@cornell.edu.


