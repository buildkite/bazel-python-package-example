# bazel-python-package-example

 An example that shows how to build, test, and package a Python library with Bazel. 

[![Build status](https://badge.buildkite.com/f9b46d96710d254e34229ba68bb8797d0b8f1e64ac5abfecb9.svg)](https://buildkite.com/buildkite/bazel-python-package-example)

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
$ bazel run requirements.update
INFO: Analyzed target //app:requirements.update (15 packages loaded, 988 targets configured).
INFO: Found 1 target...
Target //app:requirements.update up-to-date:
  bazel-bin/app/requirements.update
INFO: Elapsed time: 0.541s, Critical Path: 0.38s
INFO: 5 processes: 5 internal.
INFO: Build completed successfully, 5 total actions
INFO: Running command line: bazel-bin/app/requirements.update '--src=_main/app/requirements.txt' _main/app/requirements_lock.txt //app:requirements.update '--resolver=backtracking' --allow-unsafe --generate-hashes
Updating app/requirements_lock.txt
```

```bash
$ bazel run //app:main --ui_event_filters=-INFO --noshow_progress --show_result=0

The Python package says, 'Hi!'
```
