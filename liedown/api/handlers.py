from flask import jsonify, current_app

def setup_handlers(app):

    @app.errorhandler(Exception)
    def internal_server_error(e):
        current_app.logger.exception(e)
        return jsonify({
            'message': "Apologies, there's been an unexpected error."}), 500
