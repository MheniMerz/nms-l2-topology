import flask
import main 

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "<h1>HOME PAGE</h1><p>This site is a prototype API for physical topology discovery</p>"

@app.route('/nms/nodes', methods=['GET'])
def graph():
    return main.get_nodes()

@app.route('/nms/links', methods=['GET'])
def graph():
    return main.get_links()

@app.route('/nms/graph', methods=['GET'])
def graph():
    return main.get_graph()

app.run(host="0.0.0.0", port=6556)
