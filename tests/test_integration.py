import pytest
import py

# "gen" is the abbreviated name for "getentityname.py"
import gen

DATADIR=py.path.local(__file__).dirpath().join("data")
XMLFILES=sorted(DATADIR.listdir("*.xml"))
OUTFILES=sorted(DATADIR.listdir("*.out"))


@pytest.mark.parametrize("xmlfile, outfile",
    zip(XMLFILES, OUTFILES),
)
def test_xml_and_output(xmlfile, outfile, capsys):
    # We read our data and convert it into a set.
    # We are only interested in the content, not the order.
    # That way, the order doesn't matter.
    outdata = set(outfile.read().strip().split(" "))
    result = gen.main([xmlfile.strpath])
    assert result == 0
    captured = capsys.readouterr()
    assert set(captured.out.strip().split(" ")) == outdata
