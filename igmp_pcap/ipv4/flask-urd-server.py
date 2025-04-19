#!/usr/bin/env python

from flask import Flask, request

app = Flask(__name__)

@app.route("/path")
def path():
    # /path?group=group&source=source1&source=source2
    mc_group = request.args.get("group")
    mc_sources = request.args.getlist("source")

    # G:232.0.0.1 S:10.0.0.3,10.0.0.4
    return f"G:{mc_group}  S:{','.join(mc_sources)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=465, debug=True)