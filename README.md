# Painter

#### Introduction
This repo is used for plot some common figures in machine learning papers, and it will be updated if pther types of
figures are required.

#### Dependence
- Python 3
- matplotlib, seaborn
- numpy, pandas, argparse

#### Documentation
* Line Chart (error area)

  :heart:A example for random data:

  ```
  python Painter.py -k='line'
  ```

  <img src="https://github.com/Linging/Painter/blob/master/images/example.jpg" width="500">

  :heart:And you can plot your figure:

  ```
  python Painter.py -k='line' -d='./data/' -sh=True
  ```
  Your data path should be like { method-1.csv, method-2.csv, ... }, and each csv file may have mutiple experimental results(in a range of columns). 

* 3D Chart ()

    :heart:A example for random data:

      ```
      python Painter.py -k='36d'
      ```
    <img src="https://github.com/Linging/Painter/blob/master/images/example-36d.jpg" width="500">

    :heart:And you can plot your figure:

    ```
    python Painter.py -k='line' -d='./data/' -sh=True
    ```
    Each csv file should be organized like this: { columns: x_axis, index: y_axis, values: z_axis}
