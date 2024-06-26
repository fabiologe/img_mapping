from blueprints.upload import upload_jpgs_blueprint
from blueprints.upload import upload_tiffs_blueprint
from blueprints.upload import FILENAMES
from blueprints.status import check_jpgs_blueprint
from blueprints.status import check_tiffs_blueprint
from blueprints.download import serve_jpgs_blueprint, serve_tiffUTM_blueprint
from blueprints.delete import delete_jpgs_blueprint
__all__ = [
    'upload_tiffs_blueprint',
    'upload_jpgs_blueprint',
    'check_tiffs_blueprint',
    'check_jpgs_blueprint',
    'serve_jpgs_blueprint',
    'serve_tiffUTM_blueprint',
    'delete_jpgs_blueprint',
    'FILENAMES'
]