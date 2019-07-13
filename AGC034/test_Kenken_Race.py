from . import Kenken_Race

def test1(capsys):
    Kenken_Race.main(7, 1, 3, 6, 7, '.#..#..')
    captured = capsys.readouterr()    
    assert captured.out == 'Yes\n'

def test2(capsys):
    Kenken_Race.main(7, 1, 3, 7, 6, '.#..#..')
    captured = capsys.readouterr()    
    assert captured.out == 'No\n'

def test3(capsys):
    inputs = [15, 1, 3, 15, 13, '...#.#...#.#...']
    out = "Yes"
    Kenken_Race.main(*inputs)
    captured = capsys.readouterr()    
    assert captured.out == '{}\n'.format(out)