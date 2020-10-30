
# def test_pass_fail(testdir):
#     testdir.makepyfile("""
#
#         def test_pass():
#             assert 1 == 1
#
#         def test_fail():
#             assert 1 == 2
#
#     """)
#
#     result = testdir.runpytest()
#
#     print(" The result is ", result)
#
#     result.stdout.fnmatch_lines(['*.F*',])
#
#     assert result.ret == 1

def test_nice_option(test_sample):
    result = test_sample.runpytest("--nice")
    print(" The result is ", result.stdout)
    result.stdout.fnmatch_lines(['*.D*',])
    assert result.ret == 1


def test_nice_option_with_verbose(test_sample):
    result = test_sample.runpytest("-v","--nice")
    print(" The result is ", result.stdout)
    result.stdout.fnmatch_lines(['*::test2 Dinesh to change these*',])
    assert result.ret == 1