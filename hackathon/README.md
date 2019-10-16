# Hackathon

This directory is for placing useful inputs and outputs from our hackathon
projects.

## Starting Point for "Creating an Operator"

The notebook `generic.ipynb` can be used as a stub for creating a new operator.

## Starting Point for "Supporting a New Data Format"

The notebook XXXXXX can be used to start working on reading a new file format.

## Simons Observatory Work

If you have access to S.O. software stack at NERSC, see the wiki page here:

http://simonsobservatory.wikidot.com/nersc-for-so

For how to load pre-installed versions of the tools if you want to work on
something that uses the S.O. focalplane model.

## Workflow

We'll develop the projects using a common fork/pull request workflow.

1. Every project will fork https://github.com/hpc4cmb/toast-workshop-ucsd-2019 to create their own copy of the repository. Use the "Fork" button at the upper right hand corner of the github window.

2. Rename your remote to `upstream`:
```
cd toast-workshop-ucsd-2019
git remote rename origin upstream
```

3. Set up your fork to know about the original repository

```
git remote add origin git checkout https://github.com/<YOUR GITHUB USERNAME>/toast-workshop-ucsd-2019

```

Fetch all the branches of that remote into remote-tracking branches,
such as upstream/master:

```
git fetch upstream
```

Create a new `hackathon` branch:

```
git checkout -b hackathon
```

