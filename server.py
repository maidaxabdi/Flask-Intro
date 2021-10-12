"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html>Do you want a <a href='http://localhost:5000/compliment'>compliment</a> or <a href='http://localhost:5000/insult'>insult</a>? </html>"

@app.route('/compliment')
def compliment_level():
  """Have user choose compliment level"""

  return """
    <!doctype html>
    <html>
      <head>
        <title>Compliment Level</title>
      </head>
      <body>
        <h1>Choose Your Compliment Level</h1>
        <form action="/greet-1">
          <input type="radio" name="level 1">
          <label>Level 1</label>
          <input type="submit" value="Submit">
        </form>

        <form action="/greet-2">
          <input type="radio" name="level 2">
          <label>Level 2</label>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """

@app.route('/insult')
def insult_level():
  """Choose insult level"""

  return """
    <!doctype html>
    <html>
      <head>
        <title>Insult Level</title>
      </head>
      <body>
        <h1>Choose Your Insult Level</h1>
        <form action="/diss-1">
          <input type="radio" name="Level 1">
          <label>Level 1</Label>
          <input type="submit" value="Submit">
        </form>
        
        <form action="/diss-2">
          <input type="radio" name="Level 2">
          <label>Level 2</Label>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """
@app.route('/diss-1')
def diss_level_1():
  """Pick Your Insult"""
  return """
    <!doctype html>
    <html>
      <head>
        <title>Choose Your Insult</title>
      </head>
      <body>
        <h1>Choose Your Insult</h1>
        <form action="/greet">
        What's your name? <input type="text" name="person">
        Insult:
          <select name="message">
            <option value="rude">You're rude</option>
            <option value="sad">You're sad</option>
            <option value="mean">You're mean</option>
          </select>
            <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """

@app.route('/diss-2')
def diss_level_2():
  """Pick Your Insult"""
  return """
    <!doctype html>
    <html>
      <head>
        <title>Choose Your Insult</title>
      </head>
      <body>
        <h1>Choose Your Insult</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          Insult:
          <select name="message">
            <option value="ugly">You're ugly</option>
            <option value="angry">You're angry</option>
            <option value="hedious">You're hedious</option>
          </select>
            <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """
@app.route('/greet-1')
def compliments_level_1():
    """User picks compliment at level 1"""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Choose Your Compliment</title>
      </head>
      <body>
        <h1>Choose Your Compliment</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          Compliment:
          <select name="message">
          <option value="beautiful">You are beautiful!</option>
          <option value="smart">You are smart!</option>
          <option value="funny">You are funny!</option>
          </select>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """

@app.route('/greet-2')
def compliments_level_2():
    """User picks compliment at level 2"""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Choose Your Compliment</title>
      </head>
      <body>
        <h1>Choose Your Compliment</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          Compliment:
          <select name="message">
          <option value="incredibly beautiful">You are incredibly beautiful!</option>
          <option value="astronomically smart">You are astronomically smart!</option>
          <option value="outrageously funny">You are outrageously funny!</option>
          </select>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""
  
    player = request.args.get("person")
    message = request.args.get("message")
    
    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {message}!
      </body>
    </html>
    """

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
