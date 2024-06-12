from odoo import models, fields, api
import requests

class ImportCollectionsWizard(models.TransientModel):
    _name = 'collections_import.import_wizard'
    _description = 'Import Collections'

    api_token = fields.Char(string='API Token', required=True)

    def import_collections(self):
        url = 'https://collectionmanagementapp.onrender.com/api/v1/collections'
        headers = {
            'Authorization': self.api_token
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            collections_data = response.json()
            for collection_data in collections_data:
                self.env['collections_import.collection'].create({
                    'owner': self.env.user.id,
                    'name': collection_data['name'],
                    'description': collection_data['description'],
                    'number_of_items': len(collection_data['items']),
                    'category': collection_data['category']
                })
        else:
            raise Exception('Failed to fetch collections. Please check the API token.')
