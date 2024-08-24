from setuptools import setup, find_packages

  setup(
      name='dsa_princeton_algorithms',
      version='0.1.0',
      description='Implementation of Princeton Algorithms',
      author='Your Name',
      author_email='your.email@example.com',
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
