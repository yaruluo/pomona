import babies as b 
import sys


def test_parse_names(fname):
    d = b.parse_names(fname)
    assert(d[1960]['Karen'] == 3168 + 5)
    assert(d[1960]['Diane'] == 1430)
    assert(d[1960]['William'] == 3257+8)

def test_extract_data(fname):
    d = b.parse_names(fname)
    ed = b.extract_data(d,"Geoffrey")
    assert(ed[1960] == 87)
    assert(ed[1910] == 0)
    assert(ed[1940] == 7)

    ed = b.extract_data(d,"Geo*")
    assert(ed[1960] == 1345)
    assert(ed[1910] == 154)
    assert(ed[1940] == 946)

    ed = b.extract_data(d,"*")
    assert(ed[1960] == 358554)
    assert(ed[1910] == 9163)
    assert(ed[1940] == 102613)

def test_normalize_data(fname):
    d = b.parse_names(fname)
    ed = b.extract_data(d,"Geoffrey")
    b.normalize_data(ed)
    assert(int(100*ed[1960]) == 143)
    assert(int(100*ed[1910]) == 0)
    assert(int(100*ed[1940]) == 11)

    ed = b.extract_data(d,"Geo*")
    b.normalize_data(ed)
    assert(int(100*ed[1960]) == 141)
    assert(int(100*ed[1910]) == 16)
    assert(int(100*ed[1940]) == 99)

    ed = b.extract_data(d,"*")
    b.normalize_data(ed)
    assert(int(100*ed[1960]) == 125)
    assert(int(100*ed[1910]) == 3)
    assert(int(100*ed[1940]) == 36)

def main(fname):
    test_parse_names(fname)
    print("parse_names() passed")
    test_extract_data(fname)
    print("extract_data passed")
    test_normalize_data(fname)
    print("normalize_data passed")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1] + '/CA.TXT')
    else:
        main('namesbystate/CA.TXT')
