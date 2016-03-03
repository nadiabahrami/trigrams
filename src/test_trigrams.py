# -*- coding: utf-8 -*-

import pytest

TEXT_TABLE = [
    ('dummy_text.txt', 'My favorite color is red. His favorite color is blue.  The baloons color is green.')
]

CLEAN_TABLE = [
	('\r\nwhat up?  Double it.', ' what up? Double it.')
]

DIC_TABLE = [
    ('what up? Double it.', {'what up?': ['Double'], 'up? Double': ['it.']})
]

MAKE_TABLE = [
	(8,{'what up?': ['Double'], 'up? Double': ['it.']}, 8)
]



@pytest.mark.parametrize('path, result', TEXT_TABLE)
def test_text_import(path, result):
    from trigrams import text_import
    assert text_import(path) == result


@pytest.mark.parametrize('full_text, result', CLEAN_TABLE)
def test_clean_read(full_text, result):
    from trigrams import clean_read
    assert clean_read(full_text) == result
    


@pytest.mark.parametrize('clean_text, result', DIC_TABLE)
def test_create_dic(clean_text, result):
    from trigrams import create_dic
    assert create_dic(clean_text) == result

@pytest.mark.parametrize('num, dic, result', MAKE_TABLE)
def test_make_story(num, dic, result):
    from trigrams import make_story
    assert len(make_story(num, dic)) == result
    