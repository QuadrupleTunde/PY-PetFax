from flask import (Blueprint, render_template) 


bp = Blueprint('fact', __name__, url_prefix="/fact")

@bp.route('/new')
def new(): 
    return render_template('fact/new.html')



# @bp.route('/fact', method=['POST'])
# def index3(): 
#     return render_template()