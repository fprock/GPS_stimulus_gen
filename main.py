# ******************************************************************
#   GPS DATA PARSER
#   Engineer: Christopher Jones
#   Description:
#       Takes a text file of GPS log data from the Binary
#       Terminal of the UBlox U-Center software and prepares it for
#       use as stimulus for the GPS simulator.
#
# ******************************************************************

import sys
from antlr4 import *
from ucbintermLexer import ucbintermLexer
from ucbintermParser import ucbintermParser
from test_listener import gpsListener


def main(argv):
    input_file = FileStream(argv[1], 'utf8')
    # input_file = open("uc_bin_term_msg.txt", "r")
    lexer = ucbintermLexer(input_file)
    stream = CommonTokenStream(lexer)
    parser = ucbintermParser(stream)
    tree = parser.data_stream()

    output_file = open("output.txt", "w")
    listening = gpsListener(output_file)
    walker = ParseTreeWalker()
    walker.walk(listening, tree)

    output_file.close()


if __name__ == '__main__':
    main(sys.argv)
