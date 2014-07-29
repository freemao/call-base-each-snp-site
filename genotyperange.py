#!/usr/bin/python
from numpy import *
from optparse import OptionParser

msg_usage = 'usage: %prog [-F] common_fb_file [-G] common_gatk_file [-S] common_sb_file'
descr ='''tackle the three files generated by inter_vcf.py, return R/A, fb_genotype,
gatk_genotype and sb_genotype for next ploting.
'''
optparser = OptionParser(usage = msg_usage, description = descr)
optparser.add_option('-F', '--cfb', dest = 'commonfbfile',
                     help = 'Input the freebayes vcf file with common snp sites.')
optparser.add_option('-G', '--cgatk', dest = 'commongatkfile',
                     help = 'Input the GATK vcf file with common snp sites.')
optparser.add_option('-S', '--csb', dest = 'commonsbfile',
                     help = 'Input the samtools vcf file with common snp sites.')
options, args = optparser.parse_args()


def get_RA_gp(cnfb, cngatk, cnsb):   #gp: genotype
    from VCF_Parser import FbVcf
    from VCF_Parser import GATKVcf
    from VCF_Parser import SBVcf
    countA = []
    countR = []
    fbfile = open(cnfb)
    gatkfile = open(cngatk)
    sbfile = open(cnsb)
    fb_genotype = []
    for i in fbfile:
        ob = FbVcf(i)
        countA.append(ob.Acount)
        countR.append(ob.Rcount)
        fb_genotype.append(ob.genotype)
    arrcountA = array(countA, dtype=float64)
    arrcountR = array(countR, dtype=float64)
    arrRdiviA = arrcountR/arrcountA
    fbfile.close()

    gatk_genotype = []
    for i in gatkfile:
        ob = GATKVcf(i)
        gatk_genotype.append(ob.genotype)
    gatkfile.close()

    sb_genotype = []
    for i in sbfile:
        ob = SBVcf(i)
        sb_genotype.append(ob.genotype)
    sbfile.close()
    print arrRdiviA, arrRdiviA.shape
    print fb_genotype, len(fb_genotype)
    print gatk_genotype, len(gatk_genotype)
    print sb_genotype, len(sb_genotype)

    return arrRdiviA, fb_genotype, gatk_genotype, sb_genotype

if __name__ == '__main__':
    import sys

    f = options.commonfbfile
    g = options.commongatkfile
    s = options.commonsbfile
#    get_RA_gp(sys.argv[1], sys.argv[2], sys.argv[3])
    get_RA_gp(f, g, s)
