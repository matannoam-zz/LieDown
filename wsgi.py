from liedown import create_app


_liedown = None


def liedown(*args):
    global _liedown
    if not _liedown:
        _liedown = create_app()
    return _liedown(*args)
