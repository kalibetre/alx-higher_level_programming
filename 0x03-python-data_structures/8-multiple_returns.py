#!/usr/bin/python3
def multiple_returns(sentence):
    str_len = len(sentence) if sentence else 0
    return (str_len, None if str_len == 0 else sentence[0])
