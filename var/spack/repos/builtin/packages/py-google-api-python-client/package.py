# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyGoogleApiPythonClient(PythonPackage):
    """The Google API Client for Python is a client library for accessing the
    Plus, Moderator, and many other Google APIs."""

    homepage = "https://github.com/google/google-api-python-client/"
    pypi = "google-api-python-client/google-api-python-client-1.7.10.tar.gz"

    version("1.8.0", sha256="0f5b42a14e2d2f7dee40f2e4514531dbe95ebde9c2173b1c4040a65c427e7900")
    version("1.7.10", sha256="2e55a5c7b56233c68945b6804c73e253445933f4d485d4e69e321b38772b9dd6")

    depends_on("python@2.7:2.8,3.4:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-httplib2@0.9.2:0", type=("build", "run"))
    depends_on("py-google-auth@1.4.1:", type=("build", "run"))
    depends_on("py-google-auth-httplib2@0.0.3:", type=("build", "run"))
    depends_on("py-google-api-core@1.13.0:1", when="@1.8:", type=("build", "run"))
    depends_on("py-six@1.6.1:1", type=("build", "run"))
    depends_on("py-uritemplate@3.0.0:3", type=("build", "run"))
