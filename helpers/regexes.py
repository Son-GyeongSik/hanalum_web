""" 주로 사용되는 regex 들을 모아두는 모듈입니다. """
import re

email_regex = re.compile(
    r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
)

nickname_regex = re.compile(
    r"^[a-zA-Z0-9가-힣]{1,10}$"
)  # 영문 & 숫자로 이루어진 길이 1~10인 닉네임만 허용

realname_regex = re.compile(
    r"^[가-힣]+$"
)

password_regex = re.compile(
    r"^\s*(?:\S\s*){8,16}$"
)
