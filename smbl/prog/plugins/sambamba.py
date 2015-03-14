import smbl
import snakemake
import os

import __program

SAMBAMBA = __program.get_bin_file_path("sambamba")


##########################################
##########################################


class SamBamBa(__program.Program):
	@classmethod
	def get_installation_files(cls):
		return [
				SAMBAMBA,
			]

	@classmethod
	def install(cls):
		version="v0.5.1"

		if (smbl.is_linux()):
			fn=cls.download_file("http://github.com/lomereiter/sambamba/releases/download/{ver}/sambamba_{ver}_linux.tar.bz2".format(ver=version),"sambamba.tar.bz2")
		elif smbl.is_mac():
			fn=cls.download_file("http://github.com/lomereiter/sambamba/releases/download/{ver}/sambamba_{ver}_osx.tar.bz2".format(ver=version),"sambamba.tar.bz2")
		else:
			raise NotImplementedError("Unsupported OS")
		dir=cls.extract_tar(fn)

		cls.install_file("sambamba_{ver}".format(ver=version),SAMBAMBA)

	@classmethod
	def supported_platforms(cls):
		return ["macos","linux"]