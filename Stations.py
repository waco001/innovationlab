from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

stations_bp = Blueprint('stations', __name__)

@stations_bp.route('/stations')
def stations_index():
	return render_template('stations/index.html')

@stations_bp.route('/stations/printing')
def printing():
	context = {'title':'3D Printing Technologies',
			'sub_title':'The innovation lab employs 3D printing technologies to infuse 3D modeling with product testing.'}
	return render_template('stations/printing/index.html', data=context)

@stations_bp.route('/stations/printing/resources')
def printing_resources():
	return render_template('stations/printing/resources.html')

@stations_bp.route('/stations/printing/instructions')
def printing_instruction():
	return render_template('stations/printing/instructions.html')


@stations_bp.route('/stations/makerspace')
def makerspace():
	context = {'title':'Maker Spaces',
			'sub_title':'Maker Spaces provide a way of replicating published stations and projects of the STEAM Innovation Lab'}
	return render_template('stations/makerspace/index.html', data=context)