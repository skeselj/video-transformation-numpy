'''"Setup" information for the package.

I used https://python-packaging-tutorial.readthedocs.io/en/latest/setup_py.html
as  a guide.
'''

import setuptools

setuptools.setup(
    name='video_transformation_numpy',
    version='0.0',
    author='Stefan Keselj',
    author_email='keselj.stefan@gmail.com',
    packages=[
        'video_transformation_numpy',
        'video_transformation_numpy.test'],
    url='https://github.com/skeselj/video-transformation-numpy',
    license='LICENSE.md',
    description='''
        Libraries that support transformations on videos and by default
        use numpy representations of objects.''',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
 )