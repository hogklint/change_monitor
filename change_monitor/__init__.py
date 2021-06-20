from gevent import monkey

monkey.patch_all()

from .gm import gm_main  # noqa: E402

__version__ = "0.1.0"


def main():
    gm_main()
