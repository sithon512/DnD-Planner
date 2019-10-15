"""
Contains helper classes and methods for use in views.
"""

import json

class Creature:
	"""
	Defines attributes of a creature. Acts as a superclass for any PC classes
	and NPC classes.
	"""

	class CreatureSerializer(json.JSONEncoder):
		"""
		Inner class to serialize Creature.
		"""
		def default(self, object):
			"""
			Return serialized Creature
			"""
			if isinstance(object, Creature):
				return object.__dict__
			else:
				return json.JSONEncoder.default(self, object)
	
	def __init__(self, name, hp, ac, initiative_roll, num_hit_die=None,
	creature_type=None, resistances=[], is_PC=False, unique_id=0):
		"""
		Standard initialization method.

		:type name: string
		:type param: the name of the creature

		:type hp: integer
		:param hp: the maximum health of the creature

		:type ac: integer
		:param ac: the armor class of the creature

		:type num_hit_die: integer
		:param num_hit_die: the number of hit die the creature has

		:type creature_type: string
		:param creature_type: the type of the creature

		:type resistances: list of strings
		:param resistances: a list of all the resistances the creature has

		:type is_PC: boolean
		:param is_PC: whether or not this creature is a Player Character, used
		for determining whether or not it gets to attempt death saving throws
		"""

		self.name = name.capitalize()
		self.hp = hp
		self.ac = ac
		self.initiative_roll = initiative_roll
		self.unique_id = unique_id
		self.num_hit_die = num_hit_die
		self.creature_type = creature_type
		self.death_save_success = 0
		self.death_save_failure = 0
		self.resistances = resistances
		self.is_PC = is_PC
		self.status = ''

	def __eq__(self, other):
		"""
		Standard equivalancy comparison.
		"""
		if not isinstance(other, Creature):
			# if other isn't an instance of creature, obviously
			# these aren't equal
			return False;

		if self.name == other.name and\
		self.unique_id == other.unique_id:
			return True
		else:
			return False

	def __str__(self):
		ret_str = self.name
		if self.unique_id != 0:
			ret_str += f' ({self.unique_id})'
		return ret_str

	def addStatus(self, msg):
		if self.status == '':
			self.status = f'{self.name} {msg}.'
		else:
			self.status = self.status + ' ' + self.name + ' ' + msg + '.'
			self.status = f'{self.status} {self.name} {msg}.'

	def is_conscious(self):
		"""
		Returns whether the creature is still conscious.
		"""

		return self.hp > 0

	def is_dead(self):
		"""
		Returns whether the creature is still alive. If the creature isn't
		designated as a player character, this simply evaluates the
		is_conscious function.
		"""

		if self.is_PC == True:
			return self.death_save_failure >= 3
		else:
			return self.is_conscious()

	def is_resistant(self, dmg_type):
		"""
		Returns whether the creature is resistant to the damage type or not.
		"""

		return dmg_type in self.resistances

	def damage(self, dmg, dmg_range, dmg_type):
		"""
		Handles creature taking damage and updates the status string so that a
		textual report of what occurred can be retrieved.
		"""

		if self.is_dead():
			return # creature is already dead, damage is pointless

		if self.hp <= 0:
			if dmg_range == 'ranged':
				self.death_save_failure += 1
				self.addStatus('failed a death saving throw from a ' +\
					'ranged attack')
			else: # dmg_range == 'melee'
				self.death_save_failure += 2
				self.addStatus('failed 2 death saving throws from a ' +\
					'melee attack')
		elif self.is_resistant(dmg_type):
			net_dmg = floor(dmg/2)
			self.hp -= net_dmg
			self.addStatus(f'took {net_dmg} {dmg_type} damage' +\
				f' from a {dmg_range} attack')
		else:
			self.hp -= dmg
			self.addStatus(f'took {dmg} {dmg_type} damage' +\
				f' from a {dmg_range} attack')

		# if they fell dead or unconscious, add that to the status text.
		if self.is_dead():
			self.addStatus('has died from its injuries')
		elif not self.is_conscious():
			self.addStatus('has fallen unconscious')

	def serialize(self):
		return self.CreatureSerializer().default(self)

	def from_dict(in_dict):
		new_crt = Creature(
			in_dict['name'],
			in_dict['hp'],
			in_dict['ac'],
			in_dict['initiative_roll'],
			num_hit_die=in_dict['num_hit_die'],
			creature_type=in_dict['creature_type'],
			resistances=in_dict['resistances'],
			is_PC=in_dict['is_PC'],
			unique_id=in_dict['unique_id'],
		)
		return new_crt

def sort_init_order(char_list):
	"""
	Sorts the list of characters that makes up the initiative order and
	returns the new, sorted list.

	:type char_list: list of dictionaries (json serialized Creature)
	:param char_list: the unsorted initiative order
	"""

	# lambda function designates sort by 'initiative_roll' key in dict
	ret_list = sorted(char_list, key=lambda k: k['initiative_roll'],
		reverse=True)

	# remains for future debugging efforts if needed:
	# 
	# print('sorted list:')
	# for val in ret_list:
	# 	print(val)

	return ret_list
