import argparse


class MessengerRnsHandler:
    def __init__(self, dna):
        self.dna = dna

    def run(self):
        self.transcription(self.dna)

    def transcription(self, dna):
        '''Create a messenger RNS from a branch of the DNA according to these rules:
            - T --> A
            - A --> U
            - G --> C
            - C --> G'''
        rns = ''
        for base in dna:
            if base == 'T':
                rns = rns + 'A'
            elif base == 'A':
                rns = rns + 'U'
            elif base == 'G':
                rns = rns + 'C'
            elif base == 'C':
                rns = rns + 'G'

        return rns


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument('-dna', '--deoxy_ribonucleic_acid',
                            default="",
                            help='This is a string which defines the DNA chain. It consists of base elements(A, T, C, G)')

    args = arg_parser.parse_args()

    handler = MessengerRnsHandler(args.deoxy_ribonucleic_acid)

    handler.run()
