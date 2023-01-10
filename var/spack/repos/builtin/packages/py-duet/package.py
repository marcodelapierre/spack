# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyDuet(PythonPackage):
    """A simple future-based async library for python."""

    homepage = "http://github.com/google/duet"
    pypi = "duet/duet-0.2.7.tar.gz"

    version("0.2.7", sha256="152d9b34db363b6b2322e48c756a8bb1832f0a704319941ff974d9ffee63c053")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-typing-extensions@3.10.0", when="^python@3.7", type=("build", "run"))
