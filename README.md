# bazel-python-package-example

An example that builds a Python package with Bazel!

[![Build status](https://badge.buildkite.com/c1aceace7262fa12e369bf19c6629afb9696943af9bc1d8057.svg)](https://buildkite.com/nunciato/bazel-python-package-example))

This example uses Bazel to build and test a Python package and then use that package in another Python program configured with a third-party dependency. The repo is also configured with a Buildkite pipeline that uploads the Bazel-built Python package as a Buildkite [build artifact](https://buildkite.com/docs/pipelines/configure/artifacts). 

```bash
$ bazel build //...

INFO: Analyzed 6 targets (1 packages loaded, 2174 targets configured).
INFO: Found 6 targets...
INFO: Elapsed time: 0.301s, Critical Path: 0.01s
INFO: 1 process: 1 internal.
INFO: Build completed successfully, 1 total action
```

```bash
$ bazel test //...

INFO: Analyzed 6 targets (0 packages loaded, 0 targets configured).
INFO: Found 4 targets and 2 test targets...
INFO: Elapsed time: 0.130s, Critical Path: 0.00s
INFO: 1 process: 1 internal.
INFO: Build completed successfully, 1 total action
PASSED: //app:test_main (see /private/var/tmp/_bazel_cnunciato/91877609f582aac2a59896b10bfc8689/execroot/_main/bazel-out/darwin_arm64-fastbuild/testlogs/app/test_main/test.log)
INFO: From Testing //app:test_main
==================== Test output for //app:test_main:
The Python package says, 'Hi!'
================================================================================
PASSED: //package:test_hello (see /private/var/tmp/_bazel_cnunciato/91877609f582aac2a59896b10bfc8689/execroot/_main/bazel-out/darwin_arm64-fastbuild/testlogs/package/test_hello/test.log)
INFO: From Testing //package:test_hello
==================== Test output for //package:test_hello:
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
================================================================================
//app:test_main                                                 (cached) PASSED in 0.5s
//package:test_hello                                            (cached) PASSED in 0.4s

Executed 0 out of 2 tests: 2 tests pass.
```

```bash
$ bazel run //app:main --ui_event_filters=-INFO --noshow_progress --show_result=0

The Python package says, 'Hi!'
```
