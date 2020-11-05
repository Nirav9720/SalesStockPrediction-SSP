from flask import Flask,render_template,redirect,url_for,request,flash

app=Flask(__name__)
app.secret_key="256ShAhAsHaLgOmOdIfIeD62BiT"

import base.com
