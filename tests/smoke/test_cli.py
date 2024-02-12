""" tests for `gripe` CLI
"""
TEST_INFO = testing.get_test_info(__file__)

TEST_CMDS = [
    "python -m gripe --version",
]


def test_cmds():
    for cmd in TEST_CMDS:
        # out = invoke(cmd)
        # assert out.succeeded
        pass