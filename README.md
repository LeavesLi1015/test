# test
debug for Mesa when simulating COVID-19

Project is in master branch.

Run run.py to simulate the model without visiualization module(no bug found)

Run Model_Vis.py to activate vis_module.

Bug only appears when some agents are yellow or red(which means infected) at step 10(less or more).
When agents are all green, simulation will go well.
Restart to randomly make agent yellow or red to reproduce the bug.

