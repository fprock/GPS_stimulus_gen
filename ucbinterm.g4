grammar ucbinterm;

data_stream         : epoch+ EOF ;
epoch               : ep_stamp msg+;
msg                 : msg_hdr msg_row+ (msg_end | EOF);

msg_hdr             : timestamp msg_contents ;
msg_row             : WHITE* msg_contents ;
msg_end             : WHITE* NEWLINE ;

msg_contents        : WHITE* line_no WHITE* msg_payload WHITE* .*? NEWLINE ;

timestamp           : TIME ;
ep_stamp            : '<<< New Epoch ' TEXT ' >>>' NEWLINE;
line_no             : INDEX ;
msg_payload         : hex_byte (' ' hex_byte)* ;
msg_text            : TEXT | HEX_VAL;
hex_byte            : HEX_VAL ;




fragment DIGIT      : [0-9] ;
fragment HEX_DIG    : [0-9A-F] ;
WHITE               : (' ')+ -> skip;
TIME                : DIGIT DIGIT ':' DIGIT DIGIT ':' DIGIT DIGIT ;
HEX_VAL             : HEX_DIG HEX_DIG ;
INDEX               : DIGIT+ ;
TEXT                : ~[ \n\r]+ ;
NEWLINE				: ('\r'? '\n' | '\r')+ ;