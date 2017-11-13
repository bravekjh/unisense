from setuptools import setup

REQUIREMENTS = ['scikit-learn>=0.19.1',
                'pip>=9.0.0, <10.0.0',
                'spacy>=2.0.0, <3.0.0', 
                'six>=1.11.0, <2.0.0']

setup(
    name='unisense',
    version='0.0.2',
    description='Sentiment analysis',
    url='https://github.com/silverguo/unisense',
    author='Yuhan',
    author_email='guoyuhan819@gmail.com',
    license='MIT',
    install_requires=REQUIREMENTS,
    packages=['unisense', 'unisense.en', 'unisense.fr'],
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    zip_safe=False
)

