{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "initial_id",
   "metadata": {
    "ExecuteTime": {
     "start_time": "2023-11-20T12:40:54.015484700Z"
    },
    "is_executing": true
   },
   "outputs": [],
   "source": [
    "from flask import Flask,request,render_template\n",
    "app = Flask(__name__)\n",
    "@app.route(\"/\",methods=[\"GET\",\"POST\"])\n",
    "def index():\n",
    "    if request.method == \"POST\":\n",
    "        rate=float(request.form.get(\"rate\"))\n",
    "        print(rate)\n",
    "        return(render_template(\"index.html\",result=-50.6*rate+90.2))\n",
    "    else:\n",
    "        return(render_template(\"index.html\",result=\"waiting for exchange rate.....\"))\n",
    "if __name__ == \"__main__\":\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e3b9b5346d114d82",
   "metadata": {
    "collapsed": false,
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "outputs": [],
   "source": [
    "print(\"c\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ead76a4e7efb60dd",
   "metadata": {
    "collapsed": false,
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
