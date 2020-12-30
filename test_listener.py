import sys
from antlr4 import *
from ucbintermParser import ucbintermParser
from ucbintermListener import ucbintermListener

class gpsListener(ucbintermListener):
    def __init__(self, output):
        self.output = output

    # # Enter a parse tree produced by ucbintermParser#data_stream.
    # def enterData_stream(self, ctx:ucbintermParser.Data_streamContext):
    #     self.output.write("<<< Enter Data Stream >>>\n")

    # # Exit a parse tree produced by ucbintermParser#data_stream.
    # def exitData_stream(self, ctx:ucbintermParser.Data_streamContext):
    #     self.output.write("<<< Exit Data Stream >>>\n")

    # # Enter a parse tree produced by ucbintermParser#epoch.
    # def enterEpoch(self, ctx:ucbintermParser.EpochContext):
    #     self.output.write("<<< New Epoch " + ctx.TEXT().getText() + " >>>\n")

    # Exit a parse tree produced by ucbintermParser#epoch.
    def exitEpoch(self, ctx:ucbintermParser.EpochContext):
        self.output.write("#\n")

  # # Enter a parse tree produced by ucbintermParser#msg.
  #   def enterMsg(self, ctx:ucbintermParser.MsgContext):
  #       self.output.write("\n")

    # Exit a parse tree produced by ucbintermParser#msg.
    def exitMsg(self, ctx:ucbintermParser.MsgContext):
        self.output.write("\n")

    #
    # # Enter a parse tree produced by ucbintermParser#msg_hdr.
    # def enterMsg_hdr(self, ctx:ucbintermParser.Msg_hdrContext):
    #     pass
    #
    # # Exit a parse tree produced by ucbintermParser#msg_hdr.
    # def exitMsg_hdr(self, ctx:ucbintermParser.Msg_hdrContext):
    #     pass
    #
    #
    # # Enter a parse tree produced by ucbintermParser#msg_row.
    # def enterMsg_row(self, ctx:ucbintermParser.Msg_rowContext):
    #     pass
    #
    # # Exit a parse tree produced by ucbintermParser#msg_row.
    # def exitMsg_row(self, ctx:ucbintermParser.Msg_rowContext):
    #     pass
    #
    #
    # # Enter a parse tree produced by ucbintermParser#msg_end.
    # def enterMsg_end(self, ctx:ucbintermParser.Msg_endContext):
    #     pass
    #
    # # Exit a parse tree produced by ucbintermParser#msg_end.
    # def exitMsg_end(self, ctx:ucbintermParser.Msg_endContext):
    #     pass
    #
    #
    # # Enter a parse tree produced by ucbintermParser#msg_contents.
    # def enterMsg_contents(self, ctx:ucbintermParser.Msg_contentsContext):
    #     pass
    #
    # # Exit a parse tree produced by ucbintermParser#msg_contents.
    # def exitMsg_contents(self, ctx:ucbintermParser.Msg_contentsContext):
    #     pass
    #

    # # Enter a parse tree produced by ucbintermParser#timestamp.
    # def enterTimestamp(self, ctx:ucbintermParser.TimestampContext):
    #     self.output.write(ctx.TIME().getText() + ' ')

    # # Exit a parse tree produced by ucbintermParser#timestamp.
    # def exitTimestamp(self, ctx:ucbintermParser.TimestampContext):
    #     pass


    # # Enter a parse tree produced by ucbintermParser#ep_stamp.
    # def enterEp_stamp(self, ctx:ucbintermParser.Ep_stampContext):
    #         self.output.write("<<< New Epoch " + ctx.TEXT().getText() + " >>>\n")

    # # Exit a parse tree produced by ucbintermParser#ep_stamp.
    # def exitEp_stamp(self, ctx:ucbintermParser.Ep_stampContext):
    #     pass
    #
    #
    # # Enter a parse tree produced by ucbintermParser#line_no.
    # def enterLine_no(self, ctx:ucbintermParser.Line_noContext):
    #     pass
    #
    # # Exit a parse tree produced by ucbintermParser#line_no.
    # def exitLine_no(self, ctx:ucbintermParser.Line_noContext):
    #     pass
    #
    #
    # # Enter a parse tree produced by ucbintermParser#msg_payload.
    # def enterMsg_payload(self, ctx:ucbintermParser.Msg_payloadContext):
    #     pass
    #
    # # Exit a parse tree produced by ucbintermParser#msg_payload.
    # def exitMsg_payload(self, ctx:ucbintermParser.Msg_payloadContext):
    #     pass
    #
    #
    # # Enter a parse tree produced by ucbintermParser#msg_text.
    # def enterMsg_text(self, ctx:ucbintermParser.Msg_textContext):
    #     pass
    #
    # # Exit a parse tree produced by ucbintermParser#msg_text.
    # def exitMsg_text(self, ctx:ucbintermParser.Msg_textContext):
    #     pass


    # Enter a parse tree produced by ucbintermParser#hex_byte.
    def enterHex_byte(self, ctx:ucbintermParser.Hex_byteContext):
        the_value = ctx.HEX_VAL().getText()
        binary = lambda x: " ".join(reversed([i + j for i, j in zip(*[["{0:04b}".format(int(c, 16)) for c in reversed("0" + x)][n::2] for n in [1, 0]])]))
        bin_value = binary(the_value)
        self.output.write(bin_value + ' ')

    # # Exit a parse tree produced by ucbintermParser#hex_byte.
    # def exitHex_byte(self, ctx:ucbintermParser.Hex_byteContext):
    #     self.output.write(' ')