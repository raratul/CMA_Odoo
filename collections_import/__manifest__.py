{
    'name': 'Collections Import',
    'version': '1.0',
    'summary': 'Module to import collections from external API',
    'description': 'This module allows users to import their collections from an external API using an API token.',
    'author': 'Md Khairul Islam Ratul',
    'depends': ['base'],
    'data': [
        'views/collection_views.xml',
        'views/import_collections_wizard.xml',
    ],
    'installable': True,
    'application': True,
}
