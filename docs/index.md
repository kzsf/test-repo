# EPVS

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## How to use:

* Clone the repository and cd into it.
* Install poetry using `pip install poetry`
* Install dependencies with `poetry install`, then use `poetry shell` to activate the virtual environment.
* Navigate to epvs directory cd epvs where you will see the run.py file.
* First run the workflow dry-run with python `./run.py <path to bids data> <path to output> participant -np`.
* If the dry run is successful, we can run the workflow with `python ./run.py <path to bids data> <path to output> participant -c all --use-singularity`. Where `-c` is for number of cores you want to use. all will use everything available. (If matlab is not available, we will need to add matlab to the path with `module load matlab`.)
* When running for the first time, it will install all the singularity containers.




## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
