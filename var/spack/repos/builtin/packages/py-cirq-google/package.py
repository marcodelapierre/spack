# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyCirqGoogle(PythonPackage):
    """The Cirq module that provides tools and access
    to the Google Quantum Computing Service.
    """

    homepage = "http://github.com/quantumlib/cirq"

    # pip build from wheel recommended on github repo
    version(
        "1.1.0",
        sha256="4ddab3e274df78a5c816d1aebbd96248c187ef04a44d3499799d51fb3a85981f",
        expand=False,
        url = "https://files.pythonhosted.org/packages/30/d2/4355681fd75b5df9c9ab492beb44c624c897232da0a1cb0c7c1b6e0d85c3/cirq_google-1.1.0-py3-none-any.whl",
    )
    version(
        "0.13.1",
        sha256="4319fade78e7ecb3fc846a82d426d14426079df3b219d82325e70e34b564af98",
        expand=False,
        url = "https://files.pythonhosted.org/packages/b8/0b/cdffde4457fc5abb3aa1c65b1b7a53d8ed3b3c0c05370040833d3ff7bedb/cirq_google-0.13.1-py3-none-any.whl",
    )

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-google-api-core@1.14.0:1+grpc", type="run")
    depends_on("py-protobuf@3.13.0:3", type="run")
    depends_on("py-proto-plus@1.20.0:", when="@0.15.0:", type="run")
