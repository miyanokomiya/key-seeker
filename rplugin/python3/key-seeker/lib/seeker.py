from typing import List


def valid_line(line: str) -> bool:
    """
    行バリデーション

    Parameters
    ----------
    line: str
        行テキスト

    Returns
    -------
    valid: bool
        validであるフラグ
    """

    lstriped = line.lstrip()
    if len(lstriped) == 0:
        return False

    if lstriped[0] == '#':
        return False

    if lstriped[0] == '/':
        return False

    return True


def seek_key(lines: List[str], index: int) -> str:
    """
    キー階層シーク

    Parameters
    ----------
    lines: List[str]
        テキスト
    index: int
        探索行インデックス

    Returns
    -------
    key: str
        該当キー
    """

    ret: str = '.'
    current_indent: int = 10000  # 十分に大きなインデントを初期値としておく

    for line in lines[:index + 1][::-1]:
        if not valid_line(line):
            continue

        indent = len(line) - len(line.lstrip())
        if indent >= current_indent:
            continue

        splited = line.split(':')
        if len(splited) <= 1:
            continue

        ret = '.' + splited[0].strip().replace("'", '').replace('"', '') + ret
        current_indent = indent
        if current_indent == 0:
            break

    # . が余分に付くので削除
    return ret[1:-1]


def dig_key(lines: List[str], key: str) -> [int, int, str]:
    """
    キー掘り下げ

    Parameters
    ----------
    lines: List[str]
        テキスト
    key: str
        探索キー

    Returns
    -------
    row_index: int
        該当キーの行、ヒットしなければ最も近い階層の行
    column_index: int
        テキスト開始列
    hit_key: str
        ヒットしたキー
    """

    splited_key: List[str] = key.split('.')
    current_key_index: int = 0
    row_index: int = -1
    current_indent: int = 0
    last_hit_row_index: int = -1

    for line in lines:
        row_index += 1
        if not valid_line(line):
            continue

        indent = len(line) - len(line.lstrip())
        if indent <= current_indent:
            continue

        splited = line.split(':')
        if len(splited) <= 1:
            continue

        current_key = splited[0].strip().replace("'", '').replace('"', '')
        if current_key == splited_key[current_key_index]:
            current_key_index += 1
            current_indent = indent
            last_hit_row_index = row_index

        if current_key_index == len(splited_key):
            break

    return [last_hit_row_index,
            current_indent,
            '.'.join(splited_key[:current_key_index])]
