# brat_to_cdli_conll_converter
Brat standoff to CDLI-CoNLL Converter

## Installation

If you don't have pip installed on your system, please find the instructions [here](https://pip.pypa.io/en/stable/installing/).

To install this converter, you can run the following commands:

```
pip install git+git://github.com/cdli-gh/brat_to_cdli_conll_converter.git
```

OR

```
pip install git+https://github.com/cdli-gh/brat_to_cdli_conll_converter.git
```

OR

```
git clone https://github.com/cdli-gh/brat_to_cdli_conll_converter.git
cd brat_to_cdli_conll_converter
pip install .
```

## Upgrading

To upgrade this tool, you can run the following commands:

```
pip install git+git://github.com/cdli-gh/brat_to_cdli_conll_converter.git --upgrade
```

OR

```
pip install git+https://github.com/cdli-gh/brat_to_cdli_conll_converter.git --upgrade
```

OR

```
cd brat_to_cdli_conll_converter
git pull origin master
pip install . --upgrade
```

## Execution

To use/execute this tool, run one of the following commands:

If the input is a folder, you can use:

```
brat2conll -i data
```

If the input is a file, you can use:

```
brat2conll -i data/input_file_name.ann
```

To see the processing message on console, use the verbose option (-v):
```
brat2conll -i data -v
```

To view all the possible options, use the --help option like this:
```
brat2conll --help
```

If you don't use any arguments, it will prompt for the input file path as follows:
> $ brat2conll

> Input path: data

> Info: Converting the files  [####################################]  100%




