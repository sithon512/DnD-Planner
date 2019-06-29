from django import forms

# custom forms
class AddToInitTrkrForm(forms.Form):
	initiative_roll = forms.IntegerField(min_value=0, max_value=50,
		required=True, label='Initiative Roll')
	character_name = forms.CharField(strip=True, max_length=30, required=True,
		label='Character Name')

	# below fields will be added in a later iteration of the tracker
	# character_ac = forms.IntegerField(min_value=0, required=True,
	# 	label='Armor Class')
	# character_hp = forms.IntegerField(min_value=1, required=True,
	# 	label='Hit Points')

	def get_fields(self):
		return [
			'Initiative Roll',
			'Character Name',
			'Armor Class',
			'Hit Points',
		]


# model forms