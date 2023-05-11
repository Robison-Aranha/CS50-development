import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    message = "Some thing goes worng!"
    if request.method == "GET":
        actions = db.execute("SELECT * FROM finances WHERE id = ?", session["user_id"])
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        total = 0
        for c in actions:
            total += c["total"]
        cash = round(cash[0]["cash"], 2)
        total += cash
        total = round(total, 2)
        return render_template("index.html", actions=actions, cash=cash, total=total)

    return apology(message)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    message = ""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        if symbol == "" or "';" in symbol or '"' in symbol:
            message = "Must provide a Symbol!"
        elif shares == "" or "';" in shares or '"' in shares or shares not in "0123456789":
            message = "Must provide the number of shares!"
        else:
            dicionario = lookup(symbol)
            if dicionario != None:
                cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
                cash = float(cash[0]["cash"])
                shares = float(shares)
                if dicionario["price"] * shares < cash:
                    db.execute("UPDATE users SET cash = ? WHERE id = ?", cash - (dicionario["price"] * shares), session["user_id"])
                    if len(db.execute("SELECT * FROM finances WHERE symbol = ? AND id = ?", symbol, session["user_id"])) > 0:
                        ActualShares = db.execute("SELECT shares FROM finances WHERE id = ? AND symbol = ?",
                                                  session["user_id"], symbol)
                        ActualShares = ActualShares[0]["shares"]
                        db.execute("UPDATE finances SET shares = ?, total = ? WHERE id = ? AND symbol = ?", ActualShares + shares, round(dicionario["price"] * (shares + ActualShares), 2),
                                   session["user_id"], symbol)
                    else:
                        db.execute("INSERT INTO finances (id, symbol, name, price, shares, total) VALUES(?, ?, ?, ?, ?, ?)", session["user_id"], symbol, dicionario["name"],
                                   dicionario["price"], shares, dicionario["price"] * shares)
                    db.execute("INSERT OR IGNORE INTO history (id, action, symbol, name, shares, data) VALUES(?, ?, ?, ?, ?, ?)", session["user_id"], "buy", symbol, dicionario["name"],
                               shares, datetime.today().strftime('%Y-%m-%d %H:%M'))
                    return redirect("/")
                else:
                    message = "You don't have enough cash!"
            else:
                message = "The Symbol doesn't exist!"

    elif request.method == "GET":
        return render_template("buy.html")

    return apology(message)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    message = ""
    if request.method == "GET":
        sold = db.execute("SELECT * FROM history WHERE action = 'sell'")
        bought = db.execute("SELECT * FROM history WHERE action = 'buy'")
        return render_template("history.html", bought=bought, sold=sold)
    return apology(message)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    message = ""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if symbol == "" or "';" in symbol or '"' in symbol:
            message = "Must provide a Symbol!"
        else:
            dicionario = lookup(symbol)
            if dicionario != None:
                return render_template("quote.html", dicionario=dicionario, request=request.method)
            message = "The Symbol doesn't exist!"

    elif request.method == "GET":
        return render_template("quote.html", request=request.method)
    return apology(message)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    message = ""
    if request.method == "POST":
        name = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if name == "" or password == "" or "';" in name or '"' in name or "';" in password or '"' in password:
            message = "invalid username and/or password!"
        elif password != confirmation:
            message = "Password and Confirmation don't match!"
        elif len(db.execute("SELECT * FROM users WHERE username = ?", name)) != 0:
            message = "The username is already taken!"
        else:
            password = generate_password_hash(password)
            db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", name, password)
            id = db.execute("SELECT id FROM users WHERE username = ?", name)
            print(id[0])
            session["user_id"] = id[0]["id"]
            return redirect("/")
    elif request.method == "GET":
        return render_template("register.html")

    return apology(message)


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    message = ""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        share = request.form.get("shares")
        max = db.execute("SELECT shares FROM finances WHERE id = ?", session["user_id"])
        if symbol == "Symbols":
            message = "You didn't select any Symbol!"
        elif share == "" or share == "0":
            message = "You didn't select any Share!"
        elif int(share) > max[0]["shares"]:
            message = "Invalid number of shares!"
        else:
            finance = db.execute("SELECT * FROM finances WHERE id = ? AND symbol = ?", session["user_id"], symbol)
            dicionario = lookup(symbol)
            share = float(share)
            cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
            if share == finance[0]["shares"]:
                db.execute("UPDATE users SET cash = ? WHERE id = ?",
                           (finance[0]["price"] * share) + cash[0]["cash"], session["user_id"])
                db.execute("DELETE FROM finances WHERE id = ? AND symbol = ?", session["user_id"], symbol)
            else:
                db.execute("UPDATE users SET cash = ? WHERE id = ?",
                           (finance[0]["price"] * share) + cash[0]["cash"], session["user_id"])
                db.execute("UPDATE finances SET shares = ?, total = ? WHERE id = ?", finance[0]["shares"] - share,
                           finance[0]["price"] * share, session["user_id"])
            db.execute("INSERT INTO history (id, action, symbol, name, shares, data) VALUES(?, ?, ?, ?, ?, ?)", session["user_id"], "sell", symbol, dicionario["name"],
                       share, datetime.today().strftime('%Y-%m-%d %H:%M'))
            return redirect("/")

    elif request.method == "GET":
        symbols = db.execute("SELECT symbol FROM finances WHERE id = ?", session["user_id"])
        shares = db.execute("SELECT shares FROM finances WHERE id = ?", session["user_id"])
        return render_template("sell.html", shares=shares, symbols=symbols)
    return apology(message)


@app.route("/cash", methods=["GET", "POST"])
@login_required
def cash():
    message = ""
    if request.method == "POST":
        cash = request.form.get("cash")
        if cash == "" or "';" in cash or '"' in cash:
            message = "Invalid Input!"
        else:
            cash = float(cash)
            ActualCash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash + ActualCash[0]["cash"], session["user_id"])
            return redirect("/")

    elif request.method == "GET":
        return render_template("cash.html")

    return apology(message)
