import os.path

from lsst.utils import getPackageDir

config.load(os.path.join(getPackageDir("obs_pfs"), "config", "pfs", "isr.py"))

config.darkTime = None

config.isr.doBias = True
config.isr.doDark=False
config.isr.doFlat=False
config.repair.cosmicray.nCrPixelMax = 1000000
config.repair.cosmicray.minSigma = 5.0
config.repair.cosmicray.min_DN = 50.0
config.isr.doLinearize=False
#config.combination.combine = lsst.afw.math.MEDIAN
