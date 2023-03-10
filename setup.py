from setuptools import setup

setup(
    name='xnma',
    version='0.0.0',
    description='Calculate spectra on limited domains without aliasing',
    url='https://github.com/fluidnumerics/xnma',
    author='Dr. Joe Schoonover',
    author_email='joe@fluidnumerics.com',
    license='Researcher Software License',
    packages=['xnma'],
    install_requires=['numba',
                      'scipy',
                      'xmitgcm',
                      'xgcm',
                      'h5py>=3.7.0',
                      'dask'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3'
    ],
)
