from flask import Blueprint, request, session, redirect, url_for, flash, g, jsonify
from flask_security import login_required, logout_user, login_user, current_user
from flask_security.utils import hash_password, verify_password
from flask.templating import render_template
from skyway_connect.client.models import Client

bp_client = Blueprint('clients',__name__,static_folder='../static')


@bp_client.before_request
def before_request():
    g.user = current_user

@bp_client.route('/', methods=['GET'])
@login_required
def get_clients():
    clients = Client.query.filter_by(organization_id = g.user.organization_id).get()
    return jsonify(clients)

@bp_client.route('/', methods=['POST'])
@login_required
def create_client():
    data = request.get_json()
    client = Client(data)
    client.organization_id = g.user.organization_id
    client.save()
    return jsonify(client)