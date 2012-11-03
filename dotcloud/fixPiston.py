#Create an "__init__.py" file in the piston installation directory for correct django importing
from setuptools.command.easy_install import easy_install
import os

class easy_install_default(easy_install):
  """ class easy_install had problems with the fist parameter not being
      an instance of Distribution, even though it was. This is due to
      some import-related mess.
      """

  def __init__(self):
    from distutils.dist import Distribution
    dist = Distribution()
    self.distribution = dist
    self.initialize_options()
    self._dry_run = None
    self.verbose = dist.verbose
    self.force = None
    self.help = 0
    self.finalized = 0

e = easy_install_default()
import distutils.errors
try:
  e.finalize_options()
except distutils.errors.DistutilsError:
  pass


def fix_piston():
    path = os.path.join(e.install_dir, "piston", "__init__.py")
    print path
    file = open(path, 'w')
    file.write("")
    file.close()