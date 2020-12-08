[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.108-blue.svg)](https://doi.org/10.25663/bl.app.108)

# app-generatetractsurfaces

This service converts binary voxel images (.nii.gz format) into 3D surface meshes. The output files can be in either .stl, .ply., or .vtk file format. Choose .vtk if you plan to use the output with other brainlife.io apps.  

### Author
- Lindsey Kitchell (kitchell@indiana.edu)

### Funding Acknowledgement
brainlife.io is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your publications and code reusing this code.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)

### Citations
We kindly ask that you cite the following articles when publishing papers and code using this code. 

1. Avesani, P., McPherson, B., Hayashi, S. et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). [https://doi.org/10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

2. Kitchell L., Bullock D., Hayashi S., Pestilli F. (2018) Shape Analysis of White Matter Tracts via the Laplace-Beltrami Spectrum. In: Reuter M., Wachinger C., Lombaert H., Paniagua B., Lüthi M., Egger B. (eds) Shape in Medical Imaging. ShapeMI 2018. Lecture Notes in Computer Science, vol 11167. Springer, Cham. [https://doi.org/10.1007/978-3-030-04747-4_19](https://doi.org/10.1007/978-3-030-04747-4_19)

## Running the App 

### On Brainlife.io

You can submit this App online at [https://brainlife.io/app/593049d7ff090a00210eff05](https://brainlife.io/app/593049d7ff090a00210eff05) via the "Execute" tab.

### Running Locally (on your machine)

1. git clone this repo.
2. Inside the cloned directory, create `config.json` with something like the following content with paths to a folder (e.g. 'masks') containing your input files.

```json
{
    "maskdir": "../input/masks",
    "filetype": "vtk"
}
```
If you have singularity installed on your local machine:

3. Launch the App by executing `main`

```bash
./main
```

Otherwise:

3. Ensure you have the proper dependencies installed for python and execute main.py directly. 

### Sample Datasets

If you don't have your own input file, you can download sample datasets from Brainlife.io, or you can use [Brainlife CLI](https://github.com/brain-life/cli).

## Output

The main output of this App is a folder called 'surfaces'. This folder contains one surface mesh file for each input binary voxel file. 


### Dependencies

This App only requires [singularity](https://www.sylabs.io/singularity/) to run. If you don't have singularity, you will need to install following dependencies.  

  - VTK: https://www.vtk.org/download/
  (easiest to just use Anaconda (https://www.anaconda.com/) which comes with vtk)
