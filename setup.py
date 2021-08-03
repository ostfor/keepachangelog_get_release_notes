from setuptools import setup, find_packages

setup(name='keepachangelog_get_release_notes',
      use_scm_version=True,
      setup_requires=['setuptools_scm'],
      description='Gitlab release',
      url='http://github.com/ostfor/keepachangelog_get_release_notes',
      author='Denis Brailovsky',
      author_email='denis.brailovsky@gmail.com',
      license='MIT',
      scripts = ["scripts/keepachangelog_get_release_notes"],
      zip_safe=False)
