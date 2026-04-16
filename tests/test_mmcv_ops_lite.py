# Copyright (c) VBTI. All rights reserved.
"""Tests whether mmrotate works when onedl-mmcv without ops is installed.

The simulation runs in a subprocess so that the monkeypatched sys.modules does
not persist into the rest of the pytest session.
"""

import pytest
import subprocess
import sys
import textwrap
from packaging.version import Version

try:
    import mmdet
except ImportError:
    mmdet = None


@pytest.mark.xfail(
    mmdet is None or Version(mmdet.__version__) <= Version('3.4.6'),
    reason='mmdet <= 3.4.6 has unguarded mmcv.ops imports',
    strict=True,
)
def test_mmrotate_import_without_mmcv_ops():
    """Run the mmcv.ops-absent simulation in a fresh interpreter subprocess.

    This avoids polluting sys.modules for later tests and removes the need for
    pytest-order to control test sequencing.
    """
    script = textwrap.dedent("""\
        import sys
        import traceback
        import types

        class OpsMock(types.ModuleType):
            def __getattr__(self, name):
                if name in {
                        '__file__', '__name__', '__package__',
                        '__loader__', '__spec__'}:
                    return super().__getattribute__(name)
                raise ModuleNotFoundError('No module named "mmcv._ext"')

        ops_mock = OpsMock('mmcv.ops')
        sys.modules['mmcv.ops'] = ops_mock
        sys.modules.pop('mmcv._ext', None)

        import mmrotate  # noqa: F401
        mmrotate.__version__

        from mmrotate.utils import register_all_modules

        try:
            register_all_modules()
        except ModuleNotFoundError as e:
            tb = traceback.format_tb(e.__traceback__)
            last_entry = tb[-2] if tb else 'No traceback available'
            print(
                'Import failed, onedl-mmcv.ops is not properly guarded in\\n'
                + last_entry,
                file=sys.stderr,
            )
            sys.exit(1)
    """)

    result = subprocess.run(
        [sys.executable, '-c', script],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        'mmrotate import without mmcv.ops failed in subprocess:\n' +
        result.stderr)
