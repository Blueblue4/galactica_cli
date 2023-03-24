import galai as gal
import argparse
import json
import sys
import os



def process_args():
    parser = argparse.ArgumentParser(prog='GALACTICA cli',
                                     description='CLI interface for GALACTICA',
                                     epilog='See https://github.com/paperswithcode/galai and galactica.org '
                                            'for more information on the GALACTICA model.')
    parser.add_argument(
        'prompt', type=str,
        help='Prompt for the language model. \n'
             'Special tokens are used to nudge the language model to perform specific tasks, they include: \n'
             '[START_REF] : insert a Reference. \n'
             '<work> : reason about a question posed in the prompt. \n' 
             'TLDR: : produce a TLDR summary of the prompt. \n'
             '[START_I_SMILES] : generate a molecule/molecules. \n'
             '[START_AMINO] : generate a protein annotation. \n'
    )
    parser.add_argument(
        '--model_size', type=str, default='base',
        choices=['mini', 'base', 'standard', 'large', 'huge'],
        help='Model size of the GALACTICA model',
    )
    parser.add_argument(
        '--num_gpus', type=int, default=None,
        help="Number of GPUs to use"
    )
    parser.add_argument(
        '--parallelize', action='store_true',
        help="Parallelize over GPUs, requires more than 1 GPU"
    )
    parser.add_argument(
        '--new_doc', action='store_true',
        help="Weather to start a new document"
    )
    parser.add_argument(
        '--max_length', type=int, default=None,
        help="Maximum length in tokens of the generated text including the prompt. "
             "If None, then 60 is used."
    )
    parser.add_argument(
        '--top_p', type=float, default=None,
        help="If specified performs top p sampling, i.e. samples from amongst the "
             "top tokens whose probabilities add up top_p. Gives more variability."
    )
    parser.add_argument(
        '--num_seq', type=int, default=1,
        help="num_return_sequences : int, default 1 Number of generations to return for each prompt."
    )

    return parser.parse_args()


def galai_func(args):
    model = gal.load_model(args.model_size, num_gpus=args.num_gpus, parallelize=False if args.num_gpus is None else args.num_gpus > 0 and args.parallelize)
    out = model.generate(args.prompt, max_length=args.max_length, top_p=args.top_p, num_return_sequences=args.num_seq)
    if isinstance(out, list):
        for o in out:
            print(o)
    else:
        print(out)


def main():
    galai_func(process_args())


if __name__ == '__main__':
    main()


