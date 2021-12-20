# Test-WaNo

The Test-WaNo WaNo implements the most used functionalities available within the SimStack workflow framework to define the inputs fields of the Graphical User Interface(GUI). Here we are covering the following set of Simstack features: `WaNoFloat`, `WaNoInt`, `WaNoString`, `WaNoDropDown`,`WaNoDictBox`, `WaNoFile`, `WaNoMultipleOf`, and conditional options using the `WaNoBool`tag. All the remaining input files are loaded from an external source.

<img src="Test-WaNo-GUI.png" alt="drawing" width="700"/>
Figure 1 displays the most used functionalities available within the SimStack workflow framework. The arrows associate the tags used to generate the field and variable types. The `DictBox-name` only popup when the bool variable `Conditional-DictBox` is `True` `WaNoInt`. 

## 1. Python Setup
To get this WaNo up running on your available computational resources, make sure to have the below libraries installed on Python 3.6 or newer.

```
1. Atomic Simulation Environment (ASE).
2. Python Materials Genomics (Pymatgen).
3. subprocess, glob, os, sys, yaml. 
```

## 2. DFT-Turbomole Inputs files 
- **Follow-up calculation**: This option performs calculations from previous simulations.
- **Title**: Name the structure in the `control` file.
- **Molecule structure**: Here the user can define the input geometry format and load the structure input file.
- **Basis set**: Here the user can choose the basis set type.
- **Initial guess**: In this box, we set up the initial charge and multiplicities of the system.
- **DFT options**: This box sets up the basic DFT parameters, such as the maximum number of self-consistent steps, exchange-correlation functional, integration grid, van-der-Waals corrections, and solvation effects(treated by the COSMO). 
- **Type of calculation**: Here the user can perform Structure optimization, Excited states (TDDFT), and frequency (vibrational states) calculations. 
- 
## 3. DFT-Turbomole Output files 
   - results.tar.xz (contains all the following files: `alpha`,`auxbasis`, `basis`,`beta`,`control`,`coord`,`energy`,`forceapprox`,`gradient`,`hessapprox`,`mos`,`optinfo`,`rendered_wano.yml`,`sing_a`,`trip_a`,`unrs_a`)
   - turbomole_results.yml (contains some info like energy value, energy unit, the title of the structure, and the Homo-Lumo gap of the system).
   - final_structure.xyz (final structure after the calculation)


