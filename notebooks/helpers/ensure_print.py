'''
make sure prints in callbacks make it to the notebook

See https://ipywidgets.readthedocs.io/en/stable/examples/Output%20Widget.html

    By default, calling `print` in a ipywidgets callback results in the output
    being lost (because it is not clear _where_ it should go).  You can explictily
    capture that the text to a given output area using at Output widget.

This is a wrapper for `plt.subplots` that makes sure
  a) an ipywidgets.widgets.Output is created with each Figure
  b) the `mpl_connect` on the canvas is monkey-patched such that all
     user callbacks run in a context where the stdout is captured and sent

to that output area.
'''

import matplotlib.pyplot as plt


def _monkey_patch_pyplot():
    import matplotlib.pyplot as plt
    import functools
    from IPython.display import display
    import ipywidgets as widgets
    import weakref

    @functools.wraps(plt.figure)
    def figure(*args, **kwargs):
        fig = figure._figure(*args, **kwargs)
        fig._output = output = widgets.Output()
        display(output)

        orig_mpl_connect = fig.canvas.mpl_connect

        @functools.wraps(orig_mpl_connect)
        def mpl_connect(key, cb, **kwargs):
            # try to use a WeakMethod to make sure we don't keep objects alive
            # to match the behavior of the base mpl_connect
            try:
                r = weakref.WeakMethod(cb)
            except TypeError:
                def r():
                    return cb

            def wrapper(*args, **kw):
                cb = r()

                with output:
                    if cb is not None:
                        cb(*args, **kw)

            orig_mpl_connect(key, wrapper, **kwargs)

        # mokeny patch the canvas
        fig.canvas.mpl_connect = mpl_connect
        return fig

    # stash the orginal
    figure._figure = plt.figure
    # monkey patch pyplot (!?)
    plt.figure = figure
    plt._print_hacked = True


# make sure we only do this once!
if getattr(plt, '_print_hacked', False):
    ...
else:
    _monkey_patch_pyplot()

# clean up after our selves and do not polute the user's namespace
del _monkey_patch_pyplot
del plt
