from . import admin
from flask import jsonify
from firebase_admin import auth, _auth_utils

# Admin commands testing
@admin.route('/add_admin/<uid>', methods=['POST'])
def add_admin(uid):
    try:
        auth.set_custom_user_claims(uid, { 'admin': True })
        return jsonify({"message": f"User with UID {uid} promoted to admin"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@admin.route('/is_admin/<uid>', methods=['GET'])
def is_admin(uid):
    try:
        user = auth.get_user(uid)
        custom_claims = user.custom_claims or {}
        result = custom_claims.get('admin', False)
        return jsonify(result), 200
    except _auth_utils.UserNotFoundError:
        return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500