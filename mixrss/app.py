import dataclasses
import json
import logging
import os
import sys
import time
import uuid

from flask import Flask, flash, redirect, render_template, url_for
from flask_bootstrap import Bootstrap

sys.path.insert(0, r"D:\Jupyter\rumpy")
from rumpy import FullNode

from mixrss.forms import *

logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config["SECRET_KEY"] = uuid.uuid4().hex
Bootstrap(app)

RUM_APPKEY = "group_timeline"
app = FullNode().init_app(app)


def check_rum_connect(port=None):
    global app
    if port: #
        _app = FullNode(port=port).init_app(app)
    else:
        _app = app

    if _app.rum.api.node_status.lower() == "node_online":
        app = _app
        return True
    else:
        return False


@app.route("/")
def home():
    if not check_rum_connect():
        return redirect(url_for("add_quorum_port"))
    return render_template("home.html")


@app.route("/port/", methods=["GET", "POST"])
def add_quorum_port():
    """添加 quorum 的端口号，如果可连接，将被记录下来；以后无需重复输入。"""
    form = PortForm()
    if form.validate_on_submit():
        port = form.port.data
        if check_rum_connect(port):
            return redirect(url_for("home"))
        else:
            flash(f"Opps. port is: {port}, quorum cannot be connected. Start your quorum or check the port.")
            return redirect(url_for("add_quorum_port"))
    return render_template("port.html", form=form)

