# MedianFilter

Example Implementation of a median filter to an image

## Usage

Depends on OpenCV and MatPlotlib libraries for reading, writing, or displaying images and plots

```bash
pip install opencv-python matplotlib
```

Run main.py from the project root directory.

```bash
python main.py
```

Please rollback numpy to 1.19.3 if you you get the error: 
RuntimeError: The current Numpy installation fails to pass a sanity check due to a bug in the windows runtime.

```bash
pip install numpy==1.19.3
```

It's a bug of numpy 1.19.4 that fails with all python versions. 

After successfully running the program, the results of filtering can be found in the results folder in the project root directory.

## Contributing
Pull requests are welcome.

## License
Distributed under the MIT license. See LICENSE for more information.