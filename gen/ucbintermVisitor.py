# Generated from /home/chrispy/PycharmProjects/GPS_stimulus_gen/ucbinterm.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ucbintermParser import ucbintermParser
else:
    from ucbintermParser import ucbintermParser

# This class defines a complete generic visitor for a parse tree produced by ucbintermParser.

class ucbintermVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ucbintermParser#data_stream.
    def visitData_stream(self, ctx:ucbintermParser.Data_streamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ucbintermParser#epoch.
    def visitEpoch(self, ctx:ucbintermParser.EpochContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ucbintermParser#msg.
    def visitMsg(self, ctx:ucbintermParser.MsgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ucbintermParser#msg_hdr.
    def visitMsg_hdr(self, ctx:ucbintermParser.Msg_hdrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ucbintermParser#msg_row.
    def visitMsg_row(self, ctx:ucbintermParser.Msg_rowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ucbintermParser#msg_end.
    def visitMsg_end(self, ctx:ucbintermParser.Msg_endContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ucbintermParser#msg_contents.
    def visitMsg_contents(self, ctx:ucbintermParser.Msg_contentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ucbintermParser#timestamp.
    def visitTimestamp(self, ctx:ucbintermParser.TimestampContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ucbintermParser#ep_stamp.
    def visitEp_stamp(self, ctx:ucbintermParser.Ep_stampContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ucbintermParser#line_no.
    def visitLine_no(self, ctx:ucbintermParser.Line_noContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ucbintermParser#msg_payload.
    def visitMsg_payload(self, ctx:ucbintermParser.Msg_payloadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ucbintermParser#msg_text.
    def visitMsg_text(self, ctx:ucbintermParser.Msg_textContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ucbintermParser#hex_byte.
    def visitHex_byte(self, ctx:ucbintermParser.Hex_byteContext):
        return self.visitChildren(ctx)



del ucbintermParser