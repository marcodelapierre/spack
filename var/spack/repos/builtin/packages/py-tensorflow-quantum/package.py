# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import sys

from spack.package import *


class PyTensorflowQuantum(PythonPackage):
    """TensorFlow Quantum is an open source library for high performance batch
    quantum computation on quantum simulators and quantum computers.
    """

    homepage = "https://github.com/tensorflow/quantum"

    # pip build from wheel is the recommended way on the github repo
    # also note that the repo does not tag releases any more
    # TODO:
    # 1. attempt to match version and commit
    # 2. then attempt to build from source, with custom build,install functions;
    #    a starting point might be the recipe for py-tensorflow
    # END TODO
    if sys.platform == "darwin":
        version(
            "0.7.2-py3.9",
            sha256="adea72bcde99373851e46f2d047a37a86617cc779757f289e005a7ea0332a9c0",
            expand=False,
            url = "https://files.pythonhosted.org/packages/83/ab/256e5c340e5fe044129de1592d93ea8fd8940535755d139b0523a2ce9fc1/tensorflow_quantum-0.7.2-cp39-cp39-macosx_12_1_x86_64.whl",
        )
        version(
            "0.7.2-py3.8",
            sha256="b7b4569825398778e5079a5e0335390983f90644a2dd594cbab5627f6381e522",
            expand=False,
            url = "https://files.pythonhosted.org/packages/2a/71/32df2daad7d85d3318ab0294656bfcb99bee10c559e752310ab26cde718c/tensorflow_quantum-0.7.2-cp38-cp38-macosx_10_11_x86_64.whl",
        )
        version(
            "0.7.2-py3.7",
            sha256="934f98d93e835751f5a39542d9c7b9f3191bc630d8866001c90056d7ecd649cc",
            expand=False,
            url = "https://files.pythonhosted.org/packages/27/11/6a75f88cc892f2a3a070ca05ffd4a88f65de88585c8df018a3e2f1c000ac/tensorflow_quantum-0.7.2-cp37-cp37m-macosx_10_11_x86_64.whl",
        )
    elif sys.platform.startswith("linux") or sys.platform == "cray":
        version(
            "0.7.2-py3.9",
            sha256="1e44348011f8d2ad5f114805825d5a6568c80ec95ae391d63f4e319ffa55412b",
            expand=False,
            url = "https://files.pythonhosted.org/packages/d7/2c/820affe24172e4ffdcb326dedc4546199dae556abb5a84ef824354f5634a/tensorflow_quantum-0.7.2-cp39-cp39-manylinux_2_12_x86_64.manylinux2010_x86_64.whl",
        )
        version(
            "0.7.2-py3.8",
            sha256="fa1662ab47034ce692af9fc0e5956c2aaa3e14d6d1908d5d8b404aab7bbfad4c",
            expand=False,
            url = "https://files.pythonhosted.org/packages/39/f0/3682fd6f562dd288c9560f7a58df7ce65de257cd9f777971c9d564cd82ff/tensorflow_quantum-0.7.2-cp38-cp38-manylinux_2_12_x86_64.manylinux2010_x86_64.whl",
        )
        version(
            "0.7.2-py3.7",
            sha256="c8fa7d37b80d3058fbd281910533f452301fd5edd30579756e9ded0f0ca52693",
            expand=False,
            url = "https://files.pythonhosted.org/packages/dc/a5/eedc08009ec8c91d213abaa1899ca302e1453c9e62e966ded31433dde3c7/tensorflow_quantum-0.7.2-cp37-cp37m-manylinux_2_12_x86_64.manylinux2010_x86_64.whl",
        )

    depends_on("python@3.9", when="@0.7.2-py3.9", type=("build", "run"))
    depends_on("python@3.8", when="@0.7.2-py3.8", type=("build", "run"))
    depends_on("python@3.7", when="@0.7.2-py3.7", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    # this one builds, but then py-tensorflow-quantum examples fail at runtime,
    # due to symbols not found (possibly an ABI issue)
    # depends_on("py-tensorflow@2.7.0", type=("build", "run"))
    # this one is from the tensorflow docs, however build currently fails
    depends_on("py-tensorflow@2.7.0+gxx_old_abi", type=("build", "run"))

    depends_on("py-cirq-core@0.13.1", type=("build", "run"))
    depends_on("py-cirq-google@0.13.1", type=("build", "run"))
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
