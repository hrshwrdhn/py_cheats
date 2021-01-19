# Anaconda or Miniconda?


#### Choose Anaconda if you:
* Are new to conda or Python.
* Like the convenience of having Python and over 1,500 scientific packages automatically installed at once.
* Have the time and disk space---a few minutes and 3 GB.
* Do not want to individually install each of the packages you want to use.

#### Choose Miniconda if you:
* Do not mind installing each of the packages you want to use individually.
* Do not have time or disk space to install over 1,500 packages at once.
* Want fast access to Python and the conda commands and you wish to sort out the other programs later.



# MINICONDA 

Install Miniconda3
```
$ cd ~/Downloads
$ wget https://repo.anaconda.com/miniconda/...
```
for  example install miniconda3 for windows,linux
``` 
https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe
https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
```
#  create new environment
```
$ conda create -n environment_name python = 3.7.6
$ conda create --name python3-env python pip
$ conda create --name python36-env python=3.6 pip=20.0
```

# Activating an existing environment
```
$ conda activate basic-scipy-env
```
**code** 
```
(basic-scipy-env) $
```

# Deactivate the current environment
```
$ (basic-scipy-env) $ conda deactivate
```
**code** 
``` 
$
```

# Installing a package into an existing environment
```
$ conda activate basic-scipy-env
$ conda install numba

```
