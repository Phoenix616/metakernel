from ._metakernel import (
    ExceptionWrapper, MetaKernel, IPythonKernel, register_ipython_magics, get_metakernel,
    MetaKernelApp)
from . import pexpect
from .replwrap import REPLWrapper, u
from .process_metakernel import ProcessMetaKernel
from .magic import Magic, option
from .parser import Parser

__all__ = ['Magic', 'MetaKernel', 'option']

__version__ = '0.28.1'
