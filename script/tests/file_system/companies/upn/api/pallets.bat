cls
@echo off
bazel test --test_output=all --test_summary=detailed --test_verbose_timeout_warnings ^
    //src/test/file_system/companies/upn/api/pallets/...
@echo on