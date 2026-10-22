from setuptools import setup

# Package metadata lives in pyproject.toml. The cffi extension can't be
# declared there, so it stays here.
setup(
    cffi_modules=[
        "matcher/solvers/bvn_extension/bvn_extension_build.py:ffibuilder"
    ],
)
