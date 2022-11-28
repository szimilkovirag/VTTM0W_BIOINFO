import argparse
import json


class MessengerRnaHandler:
    def __init__(self, dna):
        self.dna = dna

    def run(self):
        rna = self.transcription(self.dna)
        amino_acids = self.convert_json_to_dict('C:/Users/SZV7BP/Desktop/suli/bio_info/VTTM0W_BIOINFO/amino_acids.json')
        protein = self.translation(rna, amino_acids)
        print(protein)

    def transcription(self, dna):
        '''Create a messenger RNA from a branch of the DNA according to these rules:
            - T --> A
            - A --> U
            - G --> C
            - C --> G'''
        rna = ''
        for base in dna:
            if base == 'T':
                rna = rna + 'A'
            elif base == 'A':
                rna = rna + 'U'
            elif base == 'G':
                rna = rna + 'C'
            elif base == 'C':
                rna = rna + 'G'

        return rna

    def translation(self, rna, amino_acids):
        '''Create amino acids from RNA'''
        rna = rna + ' '
        protein = []
        codon = ''
        codons = []
        for base in rna:
            if len(codon) < 3:
                codon = codon + base
            else:
                codons.append(codon)
                codon = ''
                codon = codon + base

        for codon in codons:
            for acid in amino_acids:
                if codon in amino_acids[acid]:
                    protein.append(acid)

        self.check_start_and_end(protein)
        self.separate_start_and_metionin(protein)

        return protein

    def check_start_and_end(self, protein):
        if not 'START' in protein[0] or not 'STOP' in protein[len(protein)-1]:
            raise Exception('The protein has to begin with START codon and has to end with STOP codon.')

    def separate_start_and_metionin(self, protein):
        protein[0] = 'START'
        for idx, acid in enumerate(protein):
            if '/' in acid:
                protein[idx] = 'metionin'

    def convert_json_to_dict(self, file_path):
        with open(file_path) as f:
            return json.load(f)


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument('-dna', '--deoxy_ribonucleic_acid',
                            default="",
                            help='This is a string which defines the DNA chain. It consists of base elements(A, T, C, G)')

    args = arg_parser.parse_args()

    handler = MessengerRnaHandler(args.deoxy_ribonucleic_acid)

    handler.run()
