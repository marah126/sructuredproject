from flask import jsonify

def not_found_error(error):
    return jsonify({'error': 'Not found'}), 404

def internal_server_error(error):
    return jsonify({'error': f'Internal server error: {error}'}), 500

class UsernameAlreadyExistsError(Exception):
    def __init__(self, message="Username already exists. Choose another one"):
        self.message = message
        super().__init__(self.message)

class ResourceNotFoundError(Exception):
    def __init__(self, message="This Resource is not found"):
        self.message = message
        super().__init__(self.message)
