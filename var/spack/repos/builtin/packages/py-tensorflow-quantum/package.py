# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyTensorflowQuantum(PythonPackage):
    """TensorFlow Quantum is an open source library for high performance batch
    quantum computation on quantum simulators and quantum computers.
    """

    homepage = "https://github.com/tensorflow/quantum"
    pypi = ""

    version("", sha256="")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-tensorflow@2.7.0", type=("build", "run"))

    # depends_on("py-cirq-core@0.13.1", type=("build", "run"))
    # depends_on("py-cirq-google@0.13.1", type=("build", "run"))
    depends_on("py-sympy@1.8", type=("build", "run"))
    depends_on("py-numpy@1.19.5", type=("build", "run"))
    depends_on("py-nbformat@4.4.0", type=("build", "run"))
    depends_on("py-pylint@2.4.4", type=("build", "run"))
    depends_on("py-yapf@0.28.0", type=("build", "run"))

    depends_on("py-googleapis-common-protos@1.52.0", type=("build", "run"))
    depends_on("py-google-api-core@1.21.0", type=("build", "run"))
    depends_on("py-google-auth@1.18.0", type=("build", "run"))
    depends_on("py-google-api-python-client@1.8.0", type=("build", "run"))
    depends_on("py-grpcio@1.34.1", type=("build", "run"))
    depends_on("py-protobuf@3.17.3", type=("build", "run"))
