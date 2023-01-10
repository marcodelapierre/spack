# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyProtoPlus(PythonPackage):
    """This is a wrapper around protocol buffers. Protocol buffers is a specification format for APIs,
    such as those inside Google.
    """

    homepage = "https://github.com/googleapis/proto-plus-python"
    pypi = "proto-plus/proto-plus-1.22.2.tar.gz"

    version("1.22.2", sha256="0e8cda3d5a634d9895b75c573c9352c16486cb75deb0e078b5fda34db4243165")

    depends_on("py-setuptools", type="build")

    depends_on("py-protobuf@3.19.0:4", type=("build", "run"))
