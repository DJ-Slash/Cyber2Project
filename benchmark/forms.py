from django.contrib.staticfiles.storage import staticfiles_storage
from django.forms import ChoiceField, Form, Select, RadioSelect
from django.urls import reverse
from crispy_forms.bootstrap import FormActions, InlineField, InlineRadios
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, ButtonHolder, Div, Fieldset, HTML, Layout, Submit

import os.path
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

blue = os.path.join(BASE_DIR, 'castle/static/blue.json')
red = os.path.join(BASE_DIR, 'castle/static/red.json')

CRITERIA_BLUE = json.load(open(blue))
CRITERIA_RED = json.load(open(red))

CHOICES = [
    (5, "Niveau 5 : Critère de poids majeur"),
    (4, "Niveau 4 : Critère de poids considérable"),
    (3, "Niveau 3 : Critère de poids important"),
    (2, "Niveau 2 : Critère de poids moyen"),
    (1, "Niveau 1 : Critère de poids faible")
]

class CustomerBlueForm(Form):
	# Ajouter ici un champ pour chaque entrée de "static/blue.json" personnalisable par le client
	detection = ChoiceField(
		widget=Select,
		choices=CHOICES,
		initial=CRITERIA_BLUE['detection']["weight"],
		label=CRITERIA_BLUE['detection']["label"],
		help_text=CRITERIA_BLUE['detection']["help_text"])
	capacite_d_analyse = ChoiceField(
		widget=Select,
		choices=CHOICES,
		initial=CRITERIA_BLUE['capacite_d_analyse']["weight"],
		label=CRITERIA_BLUE['capacite_d_analyse']["label"],
		help_text=CRITERIA_BLUE['capacite_d_analyse']["help_text"])
	complexite_d_analyse = ChoiceField(widget=Select,
		choices=CHOICES,
		initial=CRITERIA_BLUE['complexite_d_analyse']["weight"],
		label=CRITERIA_BLUE['complexite_d_analyse']["label"],
		help_text=CRITERIA_BLUE['complexite_d_analyse']["help_text"])
	export_des_resultats = ChoiceField(widget=Select,
		choices=CHOICES,
		initial=CRITERIA_BLUE['export_des_resultats']["weight"],
		label=CRITERIA_BLUE['export_des_resultats']["label"],
		help_text=CRITERIA_BLUE['export_des_resultats']["help_text"])
	creation_de_regles = ChoiceField(widget=Select,
		choices=CHOICES,
		initial=CRITERIA_BLUE['creation_de_regles']["weight"],
		label=CRITERIA_BLUE['creation_de_regles']["label"],
		help_text=CRITERIA_BLUE['creation_de_regles']["help_text"])
	export_de_fichier_suspect = ChoiceField(widget=Select,
		choices=CHOICES,
		initial=CRITERIA_BLUE['export_de_fichier_suspect']["weight"],
		label=CRITERIA_BLUE['export_de_fichier_suspect']["label"],
		help_text=CRITERIA_BLUE['export_de_fichier_suspect']["help_text"])
	prevention = ChoiceField(widget=Select,
		choices=CHOICES,
		initial=CRITERIA_BLUE['prevention']["weight"],
		label=CRITERIA_BLUE['prevention']["label"],
		help_text=CRITERIA_BLUE['prevention']["help_text"])

class CustomerRedForm(Form):
	# Ajouter ici un champ pour chaque entrée de "static/red.json" personnalisable par le client
	mise_a_jour = ChoiceField(
		widget=Select,
		choices=CHOICES,
		initial=CRITERIA_RED['mise_a_jour']["weight"],
		label=CRITERIA_RED['mise_a_jour']["label"],
		help_text=CRITERIA_RED['mise_a_jour']["help_text"])
	capacite_de_detection = ChoiceField(
		widget=Select,
		choices=CHOICES,
		initial=CRITERIA_RED['capacite_de_detection']["weight"],
		label=CRITERIA_RED['capacite_de_detection']["label"],
		help_text=CRITERIA_RED['capacite_de_detection']["help_text"])
	configuration = ChoiceField(
		widget=Select,
		choices=CHOICES,
		initial=CRITERIA_RED['configuration']["weight"],
		label=CRITERIA_RED['configuration']["label"],
		help_text=CRITERIA_RED['configuration']["help_text"])
	rapidite_d_execution = ChoiceField(
		widget=Select,
		choices=CHOICES,
		initial=CRITERIA_RED['rapidite_d_execution']["weight"],
		label=CRITERIA_RED['rapidite_d_execution']["label"],
		help_text=CRITERIA_RED['rapidite_d_execution']["help_text"])
	comsommation_de_ressources = ChoiceField(
		widget=Select,
		choices=CHOICES,
		initial=CRITERIA_RED['comsommation_de_ressources']["weight"],
		label=CRITERIA_RED['comsommation_de_ressources']["label"],
		help_text=CRITERIA_RED['comsommation_de_ressources']["help_text"])
	explication_de_vulnerabilite = ChoiceField(
		widget=Select,
		choices=CHOICES,
		initial=CRITERIA_RED['explication_de_vulnerabilite']["weight"],
		label=CRITERIA_RED['explication_de_vulnerabilite']["label"],
		help_text=CRITERIA_RED['explication_de_vulnerabilite']["help_text"])
	scope_de_scan = ChoiceField(
		widget=Select,
		choices=CHOICES,
		initial=CRITERIA_RED['scope_de_scan']["weight"],
		label=CRITERIA_RED['scope_de_scan']["label"],
		help_text=CRITERIA_RED['scope_de_scan']["help_text"])
	flexibilite = ChoiceField(
		widget=Select,
		choices=CHOICES,
		initial=CRITERIA_RED['flexibilite']["weight"],
		label=CRITERIA_RED['flexibilite']["label"],
		help_text=CRITERIA_RED['flexibilite']["help_text"])
	communaute = ChoiceField(
		widget=Select,
		choices=CHOICES,
		initial=CRITERIA_RED['communaute']["weight"],
		label=CRITERIA_RED['communaute']["label"],
		help_text=CRITERIA_RED['communaute']["help_text"])
	compatibilite_avec_outis_externes = ChoiceField(
		widget=Select,
		choices=CHOICES,
		initial=CRITERIA_RED['compatibilite_avec_outis_externes']["weight"],
		label=CRITERIA_RED['compatibilite_avec_outis_externes']["label"],
		help_text=CRITERIA_RED['compatibilite_avec_outis_externes']["help_text"])
	

class StaffBlueForm(Form):
	customer_id = ChoiceField(
		widget=Select,
		choices=(), # liste des ID clients
		label='ID client',
		help_text="Identifiant du client pour lequel les outils sont benchmarkés.")
	tool = ChoiceField(
		widget=Select,
		choices=(), # liste des tools blue non notés
		label='Outil',
		help_text="Outil pour lequel les notes des critères ci-dessous vont s'appliquer.")

	# Ajouter ici un champ pour chaque entrée de "static/blue.json"
	contexte = ChoiceField(
		widget=Select,
		choices=[(x,CRITERIA_BLUE["contexte"]["notes"][x]) for x in CRITERIA_BLUE["contexte"]["notes"]],
		label=CRITERIA_BLUE['contexte']['label'],
		help_text=CRITERIA_BLUE['contexte']['help_text'])
	detection = ChoiceField(
		widget=Select,
		choices=[(x,CRITERIA_BLUE["detection"]["notes"][x]) for x in CRITERIA_BLUE["detection"]["notes"]],
		label=CRITERIA_BLUE['detection']['label'],
		help_text=CRITERIA_BLUE['detection']['help_text'])
	capacite_d_analyse = ChoiceField(
		widget=Select,
		choices=[(x,CRITERIA_BLUE["capacite_d_analyse"]["notes"][x]) for x in CRITERIA_BLUE["capacite_d_analyse"]["notes"]],
		label=CRITERIA_BLUE['capacite_d_analyse']['label'],
		help_text=CRITERIA_BLUE['capacite_d_analyse']['help_text'])
	complexite_d_analyse = ChoiceField(
		widget=Select,
		choices=[(x,CRITERIA_BLUE["complexite_d_analyse"]["notes"][x]) for x in CRITERIA_BLUE["complexite_d_analyse"]["notes"]],
		label=CRITERIA_BLUE['complexite_d_analyse']['label'],
		help_text=CRITERIA_BLUE['complexite_d_analyse']['help_text'])
	export_des_resultats = ChoiceField(
		widget=Select,
		choices=[(x,CRITERIA_BLUE["export_des_resultats"]["notes"][x]) for x in CRITERIA_BLUE["export_des_resultats"]["notes"]],
		label=CRITERIA_BLUE['export_des_resultats']['label'],
		help_text=CRITERIA_BLUE['export_des_resultats']['help_text'])
	creation_de_regles = ChoiceField(
		widget=Select,
		choices=[(x,CRITERIA_BLUE["creation_de_regles"]["notes"][x]) for x in CRITERIA_BLUE["creation_de_regles"]["notes"]],
		label=CRITERIA_BLUE['creation_de_regles']['label'],
		help_text=CRITERIA_BLUE['creation_de_regles']['help_text'])
	export_de_fichier_suspect = ChoiceField(
		widget=Select,
		choices=[(x,CRITERIA_BLUE["export_de_fichier_suspect"]["notes"][x]) for x in CRITERIA_BLUE["export_de_fichier_suspect"]["notes"]],
		label=CRITERIA_BLUE['export_de_fichier_suspect']['label'],
		help_text=CRITERIA_BLUE['export_de_fichier_suspect']['help_text'])
	prevention = ChoiceField(
		widget=Select,
		choices=[(x,CRITERIA_BLUE["prevention"]["notes"][x]) for x in CRITERIA_BLUE["prevention"]["notes"]],
		label=CRITERIA_BLUE['prevention']['label'],
		help_text=CRITERIA_BLUE['prevention']['help_text'])
	


class StaffRedForm(Form):
	customer_id = ChoiceField(
		widget=Select,
		choices=(), # liste des ID clients
		label='ID client',
		help_text="Identifiant du client pour lequel les outils sont benchmarkés.")
	tool = ChoiceField(
		widget=Select,
		choices=(), # liste des tools red non notés
		label='Outil',
		help_text="Outil pour lequel les notes des critères ci-dessous vont s'appliquer.")

	# Ajouter ici un champ pour chaque entrée de "static/red.json"
	contexte = ChoiceField(
		widget=Select,
		choices=[(x,CRITERIA_RED["contexte"]["notes"][x]) for x in CRITERIA_RED["contexte"]["notes"]],
		label=CRITERIA_RED['contexte']['label'],
		help_text=CRITERIA_RED['contexte']['help_text'])
	mise_a_jour = ChoiceField(
		widget=Select,
		choices=[(x,CRITERIA_RED["mise_a_jour"]["notes"][x]) for x in CRITERIA_RED["mise_a_jour"]["notes"]],
		label=CRITERIA_RED['mise_a_jour']['label'],
		help_text=CRITERIA_RED['mise_a_jour']['help_text'])
	capacite_de_detection = ChoiceField(
		widget=Select,
		choices=[(x,CRITERIA_RED["capacite_de_detection"]["notes"][x]) for x in CRITERIA_RED["capacite_de_detection"]["notes"]],
		label=CRITERIA_RED['capacite_de_detection']['label'],
		help_text=CRITERIA_RED['capacite_de_detection']['help_text'])
	configuration = ChoiceField(
		widget=Select,
		choices=[(x,CRITERIA_RED["configuration"]["notes"][x]) for x in CRITERIA_RED["configuration"]["notes"]],
		label=CRITERIA_RED['configuration']['label'],
		help_text=CRITERIA_RED['configuration']['help_text'])
	rapidite_d_execution = ChoiceField(
		widget=Select,
		choices=[(x,CRITERIA_RED["rapidite_d_execution"]["notes"][x]) for x in CRITERIA_RED["rapidite_d_execution"]["notes"]],
		label=CRITERIA_RED['rapidite_d_execution']['label'],
		help_text=CRITERIA_RED['rapidite_d_execution']['help_text'])
	comsommation_de_ressources = ChoiceField(
		widget=Select,
		choices=[(x,CRITERIA_RED["comsommation_de_ressources"]["notes"][x]) for x in CRITERIA_RED["comsommation_de_ressources"]["notes"]],
		label=CRITERIA_RED['comsommation_de_ressources']['label'],
		help_text=CRITERIA_RED['comsommation_de_ressources']['help_text'])
	explication_de_vulnerabilite = ChoiceField(
		widget=Select,
		choices=[(x,CRITERIA_RED["explication_de_vulnerabilite"]["notes"][x]) for x in CRITERIA_RED["explication_de_vulnerabilite"]["notes"]],
		label=CRITERIA_RED['explication_de_vulnerabilite']['label'],
		help_text=CRITERIA_RED['explication_de_vulnerabilite']['help_text'])
	documentation = ChoiceField(
		widget=Select,
		choices=[(x,CRITERIA_RED["documentation"]["notes"][x]) for x in CRITERIA_RED["documentation"]["notes"]],
		label=CRITERIA_RED['documentation']['label'],
		help_text=CRITERIA_RED['documentation']['help_text'])
	scope_de_scan = ChoiceField(
		widget=Select,
		choices=[(x,CRITERIA_RED["scope_de_scan"]["notes"][x]) for x in CRITERIA_RED["scope_de_scan"]["notes"]],
		label=CRITERIA_RED['scope_de_scan']['label'],
		help_text=CRITERIA_RED['scope_de_scan']['help_text'])
	flexibilite = ChoiceField(
		widget=Select,
		choices=[(x,CRITERIA_RED["flexibilite"]["notes"][x]) for x in CRITERIA_RED["flexibilite"]["notes"]],
		label=CRITERIA_RED['flexibilite']['label'],
		help_text=CRITERIA_RED['flexibilite']['help_text'])
	communaute = ChoiceField(
		widget=Select,
		choices=[(x,CRITERIA_RED["communaute"]["notes"][x]) for x in CRITERIA_RED["communaute"]["notes"]],
		label=CRITERIA_RED['communaute']['label'],
		help_text=CRITERIA_RED['communaute']['help_text'])
	compatibilite_avec_outis_externes = ChoiceField(
		widget=Select,
		choices=[(x,CRITERIA_RED["compatibilite_avec_outis_externes"]["notes"][x]) for x in CRITERIA_RED["compatibilite_avec_outis_externes"]["notes"]],
		label=CRITERIA_RED['compatibilite_avec_outis_externes']['label'],
		help_text=CRITERIA_RED['compatibilite_avec_outis_externes']['help_text'])
	
