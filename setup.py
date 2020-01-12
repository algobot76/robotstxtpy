import setuptools

setuptools.setup(
    name='robotstxt',
    version='0.0.2',
    author="Example Author",
    url="https://github.com/algobot76/robotstxtpy",
    include_package_data=True,
    entry_points='''
        [console_scripts]
        robotstxt=robotstxtpy.cli:add_user_agent
        crawler=robotstxtpy.crawler_cli:add_user_agent
    ''',
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],  
    install_requires=[
        'beautifulsoup4',
        'certifi',
        'chardet',
        'click',
        'Flask',
        'idna',
        'itsdangerous',
        'Jinja2',
        'MarkupSafe',
        'requests',
        'soupsieve',
        'urllib3',
        'Werkzeug',
    ],
    python_requires='>=3.6',
)
