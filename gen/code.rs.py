import parser

def gen_header():
    print "// This file was generated automatically."
    print "// See the gen/ folder at the project root."
    print
    print "use std::fmt;"
    print "use std::str;"

def gen_enum(codes):
    print "#[derive(Clone, Copy, Debug, Eq, PartialEq)]"
    print "pub enum Code {"
    for code in codes:
        print "    " + code.format_code + ","
    print "}"

def gen_methods(codes):
    print "impl Code {"
    print
    print "    pub fn is_reply(&self) -> bool {"
    print "        match *self {"
    for code in codes:
        if not code.reply: continue
        print "            Code::" + code.format_code + " => true,"
    print "            _  => false,"
    print "        }"
    print "    }"
    print
    print "    pub fn is_error(&self) -> bool {"
    print "        match *self {"
    for code in codes:
        if not code.error: continue
        print "            Code::" + code.format_code + " => true,"
    print "            _  => false,"
    print "        }"
    print "    }"
    print
    print "}"

def gen_display(codes):
    print "impl fmt::Display for Code {"
    print
    print "    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {"
    print "        let text = match *self {"
    for code in codes:
        print "            Code::" + code.format_code + " => " + code.format_value + ","
    print "        };"
    print "        f.write_str(text)"
    print "    }"
    print
    print "}"

def gen_fromstr(codes):
    print "impl str::FromStr for Code {"
    print "    type Err = ();"
    print
    print "    fn from_str(s: &str) -> Result<Code, ()> {"
    print "        let code = match s {"
    for code in codes:
        print "            " + code.format_value + " => Code::" + code.format_code + ","
    print "            _ => return Err(()),"
    print "        };"
    print "        Ok(code)"
    print "    }"
    print "}"

if __name__ == '__main__':
    codes = parser.parse("codes.txt")
    gen_header()
    print
    gen_enum(codes)
    print
    gen_methods(codes)
    print
    gen_display(codes)
    print
    gen_fromstr(codes)
    print
