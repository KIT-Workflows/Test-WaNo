# Test-WaNo

The Test-WaNo WaNo implements the most used functionalities available within the SimStack workflow framework to define the inputs fields of the Graphical User Interface(GUI). Here we are covering the following set of Simstack features: `WaNoFloat`, `WaNoInt`, `WaNoString`, `WaNoDropDown`,`WaNoDictBox`, `WaNoFile`, `WaNoMultipleOf`, and conditional options using the `WaNoBool`tag. All the remaining input files are loaded from an external source.

<img src="Test-WaNo-GUI.png" alt="drawing" width="700"/>

Figure 1 displays the most used functionalities available within the SimStack workflow framework. The arrows associate the tags used to generate the field and variable types. The **DictBox-name** only popup when the bool variable `Conditional-DictBox` is `True`. 

## 1. Python Setup
To get this WaNo up running on your available computational resources, make sure to have the below libraries installed on Python 3.6 or newer.

```
1. matplotlib.
2. numpy.
3. yaml, sys. 
```

## 2. Test-WaNo Inputs files 
- **file-1**:  is the mandatory file required by this WaNo, as a test case you can use the *dummy_file* of this repo.
- **Load the file**: is only mandatory if the bool variable `Conditional-DictBox` is set to be `True`.

## 3. Test-WaNo Inputs files 
   - results.tar.xz (contains all the following files: `alpha`,`auxbasis`, `basis`,`beta`,`control`,`coord`,`energy`,`forceapprox`,`gradient`,`hessapprox`,`mos`,`optinfo`,`rendered_wano.yml`,`sing_a`,`trip_a`,`unrs_a`)
   - turbomole_results.yml (contains some info like energy value, energy unit, the title of the structure, and the Homo-Lumo gap of the system).
   - final_structure.xyz (final structure after the calculation)


