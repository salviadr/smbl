import os
import snakemake
import smbl


ART_454         = os.path.join(smbl.bin_dir,"art_454")
ART_ILLUMINA    = os.path.join(smbl.bin_dir,"art_illumina")
ART_SOLID       = os.path.join(smbl.bin_dir,"art_solid")
BCFTOOLS        = os.path.join(smbl.bin_dir,"bcftools")
BGZIP           = os.path.join(smbl.bin_dir,"bgzip")
BWA             = os.path.join(smbl.bin_dir,"bwa")
DWGSIM          = os.path.join(smbl.bin_dir,"dwgsim")
DWGSIM_EVAL     = os.path.join(smbl.bin_dir,"dwgsim_eval")
SAMTOOLS        = os.path.join(smbl.bin_dir,"samtools")
TABIX           = os.path.join(smbl.bin_dir,"tabix")
TWOBITTOFA      = os.path.join(smbl.bin_dir,"twoBitToFa")
WGSIM           = os.path.join(smbl.bin_dir,"wgsim")
WGSIM_EVAL      = os.path.join(smbl.bin_dir,"wgsim_eval.pl")

ALL = [
		ART_454,
		ART_ILLUMINA,
		ART_SOLID,
		BCFTOOLS,
		BGZIP,
		BWA,
		DWGSIM,
		DWGSIM_EVAL,
		SAMTOOLS,
		TABIX,
		TWOBITTOFA,
		WGSIM,
		WGSIM_EVAL
	]