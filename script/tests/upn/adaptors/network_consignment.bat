cls
@echo off
bazel test --test_output=all --test_summary=detailed --test_verbose_timeout_warnings ^
    //src/test/upn/api/network_consignment/...
@echo on