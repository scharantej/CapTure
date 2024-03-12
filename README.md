## Flask Application Design

**Problem**: Make a remote procedure call (RPC) to a gRPC server and display the response data in a user-friendly format.

**HTML Files**:

- **index.html**: This file will serve as the main interface for the application. It should contain a form that allows users to enter the necessary parameters for the RPC call, as well as a section to display the response.

```html
<!-- index.html -->
<h1>RPC Client</h1>
<form action="/rpc" method="post">
  <label for="request">Request:</label>
  <input type="text" name="request" id="request" />
  <input type="submit" value="Send" />
</form>
<div id="response"></div>
```

**Routes**:

- **@app.route('/rpc', methods=['POST'])**: This route will handle the RPC call. It should fetch the request data, make the RPC call using the gRPC client, and then render the response in a user-friendly format in the index.html page.

```python
@app.route('/rpc', methods=['POST'])
def rpc():
    request_data = request.form['request']
    response_data = make_rpc_call(request_data)
    return render_template('index.html', response=response_data)
```

- **@app.route('/')**: This route will redirect to the index.html page. It is the default route and ensures that the application always loads the main interface.

```python
@app.route('/')
def index():
    return redirect(url_for('rpc'))
```

**Functionality Overview**:

1. The user enters the request data in the form on the index.html page.
2. Clicking the "Send" button triggers a POST request to the '/rpc' route.
3. The '/rpc' route handles the request, makes the RPC call, and stores the response in the 'response' variable.
4. The index.html page is rendered, displaying the response data in the designated section.