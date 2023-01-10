# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyCirqCore(PythonPackage):
    """A framework for creating, editing, and invoking
    Noisy Intermediate Scale Quantum (NISQ) circuits.
    """

    homepage = "http://github.com/quantumlib/cirq"

    # pip build from wheel recommended on github repo
    version(
        "0.13.1",
        sha256="31f88210f00b43c6d10c83c0e2e5291c6e4a1750f436dcb8044b3343c6bd73b9",
        expand=False,
        url = "https://files.pythonhosted.org/packages/2d/29/d4e36ad6e9e38e5e03d7e5a23402598b95fb97262d1993b8e56fc8c5455a/cirq_core-0.13.1-py3-none-any.whl",
    )

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-duet@0.2.0:0.2", type="run")
    depends_on("py-matplotlib@3.0:3", type="run")
    depends_on("py-networkx@2.4:2", type="run")
    depends_on("py-numpy@1.16:1", type="run")
    depends_on("py-pandas", type="run")
    depends_on("py-sortedcontainers@2.0:2", "run")
    depends_on("py-scipy", type="run")
    depends_on("py-sympy", type="run")
    depends_on("py-typing_extensions", type="run")
    depends_on("py-tqdm", type="run")
