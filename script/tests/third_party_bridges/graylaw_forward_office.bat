cls
@echo off
bazel test --test_output=all --test_summary=detailed --test_verbose_timeout_warnings ^
    //src/test/third_party_bridges/graylaw_forward_office/...
@echo on