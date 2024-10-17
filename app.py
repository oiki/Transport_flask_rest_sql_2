from flask import Flask, request, jsonify
from models import db, Transport
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/transports', methods=['GET'])
def get_transports():
    transports = Transport.query.all()
    return jsonify([transport.to_dict() for transport in transports])

@app.route('/transports', methods=['POST'])
def add_transport():
    data = request.get_json()
    new_transport = Transport(
        patient_name=data['patient_name'],
        transport_type=data['transport_type'],
        destination=data['destination'],
        status=data['status']
    )
    db.session.add(new_transport)
    db.session.commit()
    return jsonify(new_transport.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)
