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

2. The clone your fork of the repository to NERSC with
```
mkdir my_forks
cd my_forks
git checkout https://github.com/<YOUR GITHUB USERNAME>/toast-workshop-ucsd-2019
```

3. Set up your fork to know about the original repository

```
git remote add upstream https://github.com/hpc4cmb/toast-workshop-ucsd-2019
```

Fetch all the branches of that remote into remote-tracking branches,
such as upstream/master:

```
git fetch upstream
```

Checkout the `ucsd` branch we used in the workshop

```
git checkout ucsd
```

Rewrite your master branch so that any commits of yours that
aren't already in upstream/master are replayed on top of that
other branch

```
git rebase upstream/master
```

If you don't want to rewrite the history of your master branch, (for example because other people may have cloned it) then you should replace the last command with git merge upstream/master. However, for making further pull requests that are as clean as possible, it's probably better to rebase.

If you've rebased your branch onto upstream/master you may need to force the push in order to push it to your own forked repository on GitHub. You'd do that with:

```
git push -f origin master
You only need to use the -f the first time after you've rebased.
```

4. Create a branch in your fork
```
cd toast-workshop-ucsd-2019
git checkout -b my_branch
```

