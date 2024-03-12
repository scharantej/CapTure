
# main.py
from flask import Flask, request, render_template
import grpc
import example_pb2
import example_pb2_grpc

app = Flask(__name__)

@app.route('/rpc', methods=['POST'])
def rpc():
    request_data = request.form['request']
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = example_pb2_grpc.ExampleServiceStub(channel)
        response = stub.get_example(example_pb2.ExampleRequest(data=request_data))
    return render_template('index.html', response=response.data)

@app.route('/')
def index():
    return redirect(url_for('rpc'))

if __name__ == '__main__':
    app.run()
