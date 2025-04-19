import os
from typing import Dict, Any, Union, Tuple

class LayeredStructure:
    """Manages the creation of a layered Django application structure."""
    
    def __init__(self):
        self.layers = self._define_layers()
        self.env_template = self._define_env_template()
    
    def _define_layers(self) -> Dict[str, Dict[str, Any]]:
        return {
            'presentation': {
                'files': {
                    'views.py': (
                        "# Presentation layer: This module contains the view functions or class-based views.\n"
                    ),
                    'urls.py': (
                        "# Presentation layer: Define URL patterns for the app here.\n"
                        "from django.urls import path\n\n"
                        "urlpatterns = [\n"
                        "    # TODO: add URL patterns here\n"
                        "]\n"
                    ),
                    'serializers.py': (
                        "# Presentation layer: Define serializers for API responses.\n"
                        "# Used for converting model instances to JSON or other content types.\n"
                        "from rest_framework import serializers\n\n"
                        "# TODO: Add your serializers here\n"
                    )
                }
            },
            'application': {
                'files': {
                    'services.py': (
                        "# Application layer: Contains business logic and use cases.\n"
                    )
                }
            },
            'domain': {
                'folders': {
                    'validators': {
                        '__init__.py': (
                            "# Domain layer: Contains validation rules for the domain entities.\n"
                        ),
                        'validators.py': (
                            "# Domain validators\n"
                            "def validate_entity(entity):\n"
                            "    # TODO: implement validation logic\n"
                            "    pass\n"
                        )
                    },
                    'selectors': {
                        '__init__.py': (
                            "# Domain layer: Contains selectors for querying domain-specific data.\n"
                        ),
                        'selectors.py': (
                            "# Domain selectors\n"
                            "def select_active_items(items):\n"
                            "    # TODO: implement selection logic\n"
                            "    return [item for item in items if item.get('active')]\n"
                        )
                    },
                    'utilities': {
                        '__init__.py': (
                            "# Domain layer: Utility functions related to the domain.\n"
                        ),
                        'utilities.py': (
                            "# Domain utilities\n"
                            "def format_entity(entity):\n"
                            "    # TODO: implement a method to format or transform the domain entity\n"
                            "    pass\n"
                        )
                    }
                }
            },
            'infrastructure': {
                'files': {
                    'models.py': (
                        "# Infrastructure layer: Contains Django models.\n"
                        "# IMPORTANT: Move your model definitions here from the default models.py.\n"
                        "from django.db import models\n\n"
                        "class ExampleModel(models.Model):\n"
                        "    # TODO: define your model fields\n"
                        "    name = models.CharField(max_length=255)\n\n"
                        "    def __str__(self):\n"
                        "        return self.name\n"
                    )
                }
            }
        }
    
    def _define_env_template(self) -> str:
        return (
            "# Django environment variables\n"
            "DEBUG=True\n"
            "SECRET_KEY=your-secret-key-here\n"
            "DATABASE_URL=sqlite:///db.sqlite3\n"
            "ALLOWED_HOSTS=localhost,127.0.0.1\n"
            "\n"
            "# Add your environment variables below\n"
        )
    
    def _write_file(self, path: str, content: str) -> None:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)
            
    def _create_init_file(self, directory: str) -> None:
        init_path = os.path.join(directory, '__init__.py')
        with open(init_path, 'w', encoding='utf-8'):
            pass
    
    def _create_layer_files(self, layer_path: str, files_dict: Dict[str, str]) -> None:
        for filename, content in files_dict.items():
            file_path = os.path.join(layer_path, filename)
            self._write_file(file_path, content)
    
    def _create_layer_folders(self, layer_path: str, folders_dict: Dict[str, Dict[str, str]]) -> None:
        for folder_name, folder_files in folders_dict.items():
            folder_path = os.path.join(layer_path, folder_name)
            os.makedirs(folder_path, exist_ok=True)
            self._create_layer_files(folder_path, folder_files)
    
    def setup(self, app_name: str) -> None:
        base_path = os.path.join(app_name)
        
        for layer, config in self.layers.items():
            layer_path = os.path.join(base_path, layer)
            os.makedirs(layer_path, exist_ok=True)
            
            self._create_init_file(layer_path)
            
            if 'files' in config:
                self._create_layer_files(layer_path, config['files'])
            
            if 'folders' in config:
                self._create_layer_folders(layer_path, config['folders'])
        
        env_file_path = os.path.join(base_path, '.env')
        self._write_file(env_file_path, self.env_template)
        
        print(f"📂 The layered structure with sample files was created for the app: {app_name}")
