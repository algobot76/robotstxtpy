import setuptools

authors = ['Aaron Ngu', 'Adrian Yeung', 'Kaitian Xie', 'Omar Tsai']
author_emails = ['aaronngu@hotmail.com', 'adrian_yeung_2@sfu.ca',
                 'xkaitian@gmail.com', 'omar2535@gmail.com']

setuptools.setup(
    name='robotstxt',
    version='0.1.0',
    author=', '.join(authors),
    author_email=', '.join(author_emails),
    url='https://github.com/algobot76/robotstxtpy',
    include_package_data=True,
    entry_points='''
        [console_scripts]
        robotstxt=robotstxtpy.cli:add_user_agent
        crawler=robotstxtpy.crawler_cli:add_user_agent
    ''',
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'beautifulsoup4',
        'click',
        'requests',
        'soupsieve',
        'urllib3',
    ],
    python_requires='>=3.6',
)
