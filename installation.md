# Recommended
Instructions for installing the [Anaconda Python](https://www.anaconda.com/distribution/) distribution can be found here: 
* https://github.com/story645/install/blob/master/sections/python.md

Any __3.X__ version of Python is acceptable. Once you have a working Anaconda install, please open the conda terminal and type:

```bash
conda install -c conda-forge matplotlib jupyter pandas -y
```

More detailed instructions for using conda to install libraries can be found at
* https://github.com/story645/install/blob/master/sections/conda.md 

# Alternative
If for whatever reason Anaconda does not work, you can install Matplotlib using the pip package installer. First open a command line or terminal prompt and then type:
```bash
python -m pip install -U pip
python -m pip install -U matplotlib
python -m pip install -U pandas
```

# Test Install
To test the install, please open a Jupyter notebook and type the following in a cell:

```python
%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("http://bit.ly/tscv17")
fig, ax = plt.subplots()
_ = ax.plot(np.sort(df['Age']), 'o')
```

Then execute the cell and this figure should appear:

![scatter plot, image should look like dots curving upward](images/install.png?)



# Resources
If you are unfamiliar with command or terminal prompts, more information can be found at:

* __Windows:__ https://github.com/story645/install/blob/master/sections/windows_terminal.md
* __OS/X:__ https://github.com/story645/install/blob/master/sections/osx_terminal.md

This tutorial uses Jupyter notebook as the programming environment. More information about opening and working with a Jupyter notebook can be found at https://github.com/story645/install/blob/master/sections/jupyter.md 
