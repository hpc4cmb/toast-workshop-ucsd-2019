# Lesson Setup

These notebooks are designed to run on the https://jupyter.nersc.gov but the serial portion of the notebooks should run anywhere that TOAST is installed.  You can set up these notebooks completely within the jupyter session.

## Connect to Jupyterhub

Make sure you have activated your NERSC account and [have set up MFA](https://www.nersc.gov/users/connecting-to-nersc/mfa/).  Then go to https://jupyter.nersc.gov and log in.  Select a "shared cori node" to run your session.  You should now be at a file system browser.  

## Clone this Repo

Go to the Jupyter menu File-->New-->Terminal.  This will launch a terminal window.  Decide where you want to put it and then clone this repo:

    $>  git clone https://github.com/hpc4cmb/toast-workshop-ucsd-2019.git
    
## Set Up Your Software Stack

Before running these notebooks, we need to install a custom ipython kernel.  This only needs to be done when the software stack is updated.  From the terminal, load the latest "cmbenv" software stack:

    $>  module use /global/common/software/cmb/cori/default/modulefiles
    
    $>  module load cmbenv
    
    $>  source cmbenv

Now there will be a command available which installs the kernel for this stack:

    $>  cmbenv-jupyter

## Open the Lesson

In the jupyter file browser, navigate to the workshop git checkout and go into lessons/01_Introduction.  Double click on the `intro.ipynb` file to open it.  At the top of the notebook, you can optionally set the nersc_reservation variable to the reservation in use during the workshop.  If you leave it as "None", the notebook will still submit the job at the end, but there may be a short wait while the job queues.

Under the Run menu, select "Run all".

# Developer Notes

This git repository has a hook which runs the "nbstripout" tool on notebooks when committing.  You will need to have that tool installed (via pip or conda) to commit changes to the notebooks.