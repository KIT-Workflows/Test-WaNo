When publishing results obtained with Test-WaNo, please consider citing it. [![DOI](https://zenodo.org/badge/440164995.svg)](https://zenodo.org/badge/latestdoi/440164995)

# Test-WaNo
The Test-WaNo WaNo implements the most used functionalities available within the SimStack workflow framework to define the inputs fields of the Graphical User Interface(GUI). Here we are covering the following set of Simstack features: `WaNoFloat`, `WaNoInt`, `WaNoString`, `WaNoDropDown`,`WaNoDictBox`, `WaNoFile`, `WaNoMultipleOf`, and conditional options using the `WaNoBool`tag. All the remaining input files are loaded from an external source.

<img src="Test-WaNo-GUI.png" alt="drawing" width="700"/>

Figure 1 displays the most used functionalities available within the SimStack workflow framework. The arrows associate the tags used to generate the field and variable types. The **DictBox-name** only popup when the bool variable `Conditional-DictBox` is `True`. In this example we use the variables `start`,  `stop`, and `step` as input to the python script file `test-script.py` to generate an array with the `numpy.arange(start, stop, step)` function.    

## 1. Python Setup
To get this WaNo up running on your available computational resources, make sure to have the below libraries installed on Python 3.6 or newer.

```
1. matplotlib.
2. numpy.
3. yaml, sys. 
```

The python scripts run with the `simstack_kit` conda environment defined in the `WaNoExecCommand` tag as shown below. 
```
<WaNoExecCommand>
   bash config.sh
</WaNoExecCommand>
```
Other local environments are allowed but have to be changed accordingly in the respective tag of the `Test-WaNo.xml` file.


## 2. Test-WaNo Inputs files 
- **file-1**:  is the mandatory file required by this WaNo, as a test case you can use the *dummy_file* of this repo.
- **Load the file**: is only mandatory if the bool variable `Conditional-DictBox` is set to be `True`.

## 3. Test-WaNo Inputs files 
   - The `figure.png` image is the mandatory output of this WaNo
## 4. Report
   - By clicking the right mouse button on the executed workflow folder, we can choose the report option to display the pre-defined `.html` file. Below we show the outcome of this file, which exhibits the title **Test-Report**, some information about the output of the WaNo (blue). It prints out all the inputs of the WaNo, and plot a figure by using the python script `test-script.py`.     
   <img src="Report.png" alt="drawing" width="700"/>

## License & copyright
© Celso R. C. Rêgo

Licensed under the [MIT License](LICENSE).

