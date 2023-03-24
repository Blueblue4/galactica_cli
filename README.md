# CLI interface for GALACTICA
A simple cli for the [GALACTICA](https://github.com/paperswithcode/galai) LLM. 

## Installation 
Recommended installation via [pipx](https://pypa.github.io/pipx/):
```bash
pipx install PATH_TO_CLONED_REPO
```
or
```bash
pipx install git+https://github.com/Blueblue4/galactica-cli.git
```
## Usage
After installing the CLI interface with pipx you can use it from anywhere via your commandline:
```bash
galai_cli "Finish my Paper! Or at least this formula: \\[" 
```

## Features

```
Positional arguments:
  prompt                Prompt for the language model. Special tokens are used to nudge the language model to perform specific tasks, 
                        they include: 
                        [START_REF]      : insert a Reference. 
                        <work>           : reason about a question posed in the prompt. 
                        TLDR:            : produce a TLDR summary of the prompt. 
                        [START_I_SMILES] : generate a molecule/molecules.
                        [START_AMINO]    : generate a protein annotation.

optional arguments:
  -h, --help            show this help message and exit
  --model_size {mini,base,standard,large,huge}
                        Model size of the GALACTICA model, default: base
  --num_gpus NUM_GPUS   Number of GPUs to use
  --parallelize         Parallelize over GPUs, requires more than 1 GPU
  --new_doc             Starts a new document
  --max_length MAX_LENGTH
                        Maximum length in tokens of the generated text including the prompt. If MAX_LENGTH==None, 
                        then 60 is used. Default is None.
  --top_p TOP_P         If specified performs top p sampling, i.e. samples from amongst the top tokens whose 
                        probabilities add up top_p. Gives more variability.
  --num_seq NUM_SEQ     num_return_sequences : int, default 1 Number of generations to return for each prompt. 
                        Only works with TOP_P is set otherwise greedy evalauation would return the same result each time. 
```
See https://github.com/paperswithcode/galai and galactica.org for more information on the GALACTICA model.