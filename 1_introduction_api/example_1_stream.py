from flask import Flask, stream_with_context, Response
import time

app = Flask(__name__)

@app.route('/stream')
def stream_example():
    def generate():
        yield 'Hello '
        time.sleep(1)
        yield 'World!'
        time.sleep(1)
        yield 'This'
        time.sleep(1)
        yield 'is'
        time.sleep(1)
        yield 'a'
        time.sleep(1)
        yield 'stream'
        time.sleep(1)
        yield 'example.'
    return Response(stream_with_context(generate()))


@app.route('/stream2')
def stream_example2():
    gen = (i for i in ['Hello ', 'World!', 'This', 'is', 'a', 'stream', 'example.'])
    return Response(stream_with_context(gen))


app.run()