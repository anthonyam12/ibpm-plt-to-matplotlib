# ibpm-plt-to-matplotlib
Converts .plt files generated by this implementation of the [Immersed Boundary Projection Method](https://github.com/cwrowley/ibpm) into Matplotlib heatmaps. This conversion is done by parsing the .plt file as per Tecplot's [data format guide](
http://home.ustc.edu.cn/~cbq/360_data_format_guide.pdf).

These scripts will, in particular, output a plot of the vorticity. Great to use to avoid the high cost of the Tecplot plotting software and the headache of trying to make other software read the plt files.
