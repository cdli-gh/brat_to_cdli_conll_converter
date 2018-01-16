#!/usr/bin/env python
import codecs
import click
import os
import re

OUTPUT_FOLDER = 'output'


class BratToCoNLLConverter:

    def __init__(self, bratInputFile, conllInputFile, verbose):
        self.bratInputFileName = bratInputFile
        self.conllInputFileName = conllInputFile
        self.outfolder = os.path.join('', OUTPUT_FOLDER)
        self.verbose = verbose
        self.__reset__()

    def __reset__(self):
        self.outputFilename = ''
        self.tokens = []

    def convert(self):
        if self.verbose:
            click.echo('Info: Reading file {0}.'.format(self.bratInputFileName))
        with codecs.open(self.bratInputFileName, 'r', 'utf-8') as openedBratFile, codecs.open(self.conllInputFileName,
                                                                                              'r',
                                                                                              'utf-8') as openedConllFile:

            conllLines = list()
            for i in openedConllFile:
                l = i.strip()
                l = re.split('[\t  ]', l)
                conllLines.append(l)

            for (i, line) in enumerate(openedBratFile):
                self.__parse(i, line.strip(), conllLines)

    def findID(self, id, conllLines):
        form, lemma, xpostag = '', '', ''
        for i in conllLines:
            if i[0] == id:
                form = i[1]
                lemma = i[2]
                xpostag = i[4]
        return form, lemma, xpostag

    def writeToFile(self):
        outfile_name = os.path.join(self.outfolder, self.outputFilename + ".conll")
        with codecs.open(outfile_name, 'w+', 'utf-8') as outputFile:
            # outputFile.writelines("#new_text=" + self.outputFilename + "\n")
            outputFile.writelines("# ID\tFORM\tSEGM\tXPOSTAG\tHEAD\tDEPREL\tMISC\n")
            # print(self.tokens)
            for tok in self.tokens:
                outputFile.writelines(
                    tok[0] + '\t' + tok[1] + '\t' + tok[2] + '\t' + tok[3] + '\t' + tok[4] + '\t' + tok[5] + '\t' + tok[
                        6] + '\n')

    def __parse(self, linenumber, line, conllLines):
        tokenizedLine = re.split('[\t  ]', line)
        listOfTokens = list()

        filename = re.split('[/ .]', self.bratInputFileName)
        if len(filename) > 1:
            self.outputFilename = filename[1]
        elif len(filename) == 1:
            self.outputFilename = filename[0]

        if len(line) == 0:
            pass
        elif line[0] == 'R':
            tokenizedId = tokenizedLine[0].split('-')
            id = tokenizedId[0][1:]

            form, segm, xpostag = self.findID(id, conllLines)

            tokenizedArg1 = re.split('[: .]', tokenizedLine[2])
            head = tokenizedArg1[2]
            deprel = tokenizedLine[1]
            misc = '_'

            listOfTokens.append(id)
            listOfTokens.append(form)
            listOfTokens.append(segm)
            listOfTokens.append(xpostag)

            listOfTokens.append(head)
            listOfTokens.append(deprel)
            listOfTokens.append(misc)

            self.tokens.append(listOfTokens)

# def main():
#     converter = BratToCoNLLConverter('data/train-sample.ann', 'data/train-sample.conll', verbose=False)
#     converter.convert()
#     converter.writeToFile()
#
# if __name__ == '__main__':
#     main()
