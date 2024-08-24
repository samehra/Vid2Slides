from setuptools import setup, find_packages

  setup(
      name='video slides capture',
      version='0.1.0',
      description='automatically capture screenshots from a youtube video capturing important highlights',
      author='samehra',
      packages=find_packages(),
      install_requires=[
          # List any dependencies your project needs 
          'numpy',
          'pytubefix',
          'opencv-python',
          'scikit-image',
          'pillow',
          'shutil'
      ],
  )
