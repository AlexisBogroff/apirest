from flask import Flask, stream_with_context, Response

app = Flask(__name__)

@app.route('/stream')
def stream_example():
    def generate():
        yield 'Hello '
        yield 'World!'
        yield 'This'
        yield 'is'
        yield 'a'
        yield 'stream'
        yield 'example.'
    return Response(stream_with_context(generate()))

app.run()