from setuptools import setup

setup(
    name='robotstxt',
    version='0.1',
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        robotstxt=robotstxtpy.cli:add_user_agent
        crawler=robotstxtpy.crawler_cli:add_user_agent
    ''',
)
