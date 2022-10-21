from flask import Flask, jsonify
import datetime, requests
app = Flask(__name__)

orderData = [
    {
    'Order Data' : [
        {
        'order_number' : '12345678',
        'door_number' : 'A1',
        'vendor' : [{
            'vendor_type': 'Jollibee',
            'vendor_method' : 'Self-pickup'
        }],
        'timestamp_in' : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'timestamp_out' : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        {
            'order_number' : '87654321',
            'door_number' : 'A2',
            'vendor' : [{
                'vendor_type': 'Jollibee',
                'vendor_method' : 'Rider pickup'
            }],
            'timestamp_in' : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'timestamp_out' : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        {
            'order_number' : 'GF-454T',
            'door_number' : 'A3',
            'vendor' : [{
                'vendor_type': 'Grab Food',
                'vendor_method' : 'Rider pickup'
            }],
            'timestamp_in' : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'timestamp_out' : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        {
            'order_number' : 'GF-455T',
            'door_number' : 'A4',
            'vendor' : [{
                'vendor_type': 'Grab Food',
                'vendor_method' : 'Store Pickup'
            }],
            'timestamp_in' : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'timestamp_out' : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        {
            'order_number' : 'abc-acb1',
            'door_number' : 'A5',
            'vendor' : [{
                'vendor_type': 'Grab Food',
                'vendor_method' : 'Rider pickup'
            }],
            'timestamp_in' : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'timestamp_out' : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    ]
}]

@app.route('/')
def index():
    return True

@app.route('/orders', methods=['GET'])
def get():
    return jsonify({'Orders' : orderData})


if __name__ == "__main__":
    app.run(debug = True)



    