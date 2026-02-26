from setuptools import setup
config = {
    'description': 'My project',
    'author': 'My name',
    'url': 'Project\'s url',
    'download_url': 'Link for downloading',
    'author_email': 'My e-mail',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['Name'],
    'scripts': [],
    'name': 'projectname'
}
setup(**config)