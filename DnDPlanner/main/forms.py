"""
Defines forms for use in html templates.
"""

from django import forms

# custom forms
class QuickTrkrForm(forms.Form):
	"""
	Captures information for adding to the quick initiative tracker.
	"""

	initiative_roll = forms.IntegerField(min_value=0, max_value=50,
		required=True, label='Initiative Roll')
	character_name = forms.CharField(strip=True, max_length=30, required=True,
		label='Character Name')

	# below fields will be added to the full version of the tracker, but won't
	# be available to the simple version.
	# 
	# character_ac = forms.IntegerField(min_value=0, required=True,
	# 	label='Armor Class')
	# character_hp = forms.IntegerField(min_value=1, required=True,
	# 	label='Hit Points')


# model forms
