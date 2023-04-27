# README
# DIRECTIONS FOR LAB 24
On the HPC, create a conda environment using the cloned "requirements.txt" file from this git repo:
conda create --name <env_name> --file requirements.txt

List your conda environments:
conda list env

Near the bottom of the list you should see the path to your new conda env.
Activate that env: conda activate /home/<username>/.conda/envs/<env_name>

Then execute the scatter.py code in that directory.
As long as x-forwarding is enabled, it should show a plot!
