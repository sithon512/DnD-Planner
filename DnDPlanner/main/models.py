"""
Defines all of the database models.
"""

from django.conf import settings
from django.db import models

# model choices

# creature type choices (<=4 char)
PC = 'pc'
ABERRATION = 'abrr'
BEAST = 'bst'
CELESTIAL = 'clst'
CONSTRUCT = 'const'
DRAGON = 'drgn'
ELEMENTAL = 'elmnt'
FEY = 'fey'
FIEND = 'fiend'
GIANT = 'giant'
HUMANOID = 'hmnd'
MONSTROSITY = 'mnstr'
OOZE = 'ooze'
PLANT = 'plant'
UNDEAD = 'unded'
CTYPE_CHOICES = [
	(PC, 'Player Character'),
	(ABERRATION, 'Aberration'),
	(BEAST, 'Beast'),
	(CELESTIAL, 'Celestial'),
	(CONSTRUCT, 'Construct'),
	(DRAGON, 'Dragon'),
	(ELEMENTAL, 'Elemental'),
	(FEY, 'Fey'),
	(FIEND, 'Fiend'),
	(GIANT, 'Giant'),
	(HUMANOID, 'Humanoid'),
	(MONSTROSITY, 'Monstrosity'),
	(OOZE, 'Ooze'),
	(PLANT, 'Plant'),
	(UNDEAD, 'Undead'),
]

# item type choices (3 char)
ARMOR = 'arm'
POTION = 'ptn'
RING = 'rng'
ROD = 'rod'
SCROLL = 'scr'
STAFF = 'stf'
WAND = 'wnd'
WEAPON = 'wpn'
WONDEROUS = 'wdr'
ITYPE_CHOICES = [
	(ARMOR, 'Armor'),
	(POTION, 'Potion'),
	(RING, 'Ring'),
	(ROD, 'Rod'),
	(SCROLL, 'Scroll'),
	(STAFF, 'Staff'),
	(WAND, 'Wand'),
	(WEAPON, 'Weapon'),
	(WONDEROUS, 'Wonderous'),
]

# encounter type choices (<=6 char)
COMBAT = 'combat'
PUZZLE = 'puzzle'
SKILL = 'skill'
SOCIAL = 'social'
TRAVEL = 'travel'
ETYPE_CHOICES = [
	(COMBAT, 'Combat'),
	(PUZZLE, 'Puzzle'),
	(SKILL, 'Skill Challenge'),
	(SOCIAL, 'Social'),
	(TRAVEL, 'Travel'),
]

# terrain type choices (for location) (<=6 char)
ARCTIC = 'arctic'
COAST = 'coast'
DESERT = 'desert'
FOREST = 'forest'
GRASSLAND = 'grslnd'
MOUNTAIN = 'mntain'
SWAMP = 'swamp'
UNDERDARK = 'unddrk'
TTYPE_CHOICES = [
	(ARCTIC, 'Arctic'),
	(COAST, 'Coast'),
	(DESERT, 'Desert'),
	(FOREST, 'Forest'),
	(GRASSLAND, 'Grassland'),
	(MOUNTAIN, 'Mountain'),
	(SWAMP, 'Swamp'),
	(UNDERDARK, 'Underdark'),
]

# proficiency type choices (4 char)
EXPERTISE = 'expt'
PROFICIENCY = 'prof'
PTYPE_CHOICES = [
	(EXPERTISE, 'Expertise'),
	(PROFICIENCY, 'Proficiency'),
]

# ability choices (3 char)
STRENGTH = 'str'
DEXTERITY = 'dex'
CONSTITUTION = 'con'
INTELLIGENCE = 'int'
WISDOM = 'wis'
CHARISMA = 'cha'
ABILITY_CHOICES = [
	(STRENGTH, 'Strength'),
	(DEXTERITY, 'Dexterity'),
	(CONSTITUTION, 'Constitution'),
	(INTELLIGENCE, 'Intelligence'),
	(WISDOM, 'Wisdom'),
	(CHARISMA, 'Charisma'),
]

# tool category (3 char)
ARTISANS = 'art'
GAMING = 'gam'
MUSICAL = 'mus'
SUBTERFUGE = 'sub'
TOOLCAT_CHOICES = [
	(ARTISANS, "Artisan's Tools"),
	(SUBTERFUGE, 'Subterfuge Tools'),
	(GAMING, 'Gaming Sets'),
	(MUSICAL, 'Musical Instruments'),
]


# weapon property choices (4 char)
AMMUNITION = 'ammo'
FINESSE = 'fnse'
HEAVY = 'hevy'
LIGHT = 'lite'
LOADING = 'load'
RANGE = 'rnge'
REACH = 'rech'
SPECIAL = 'spec'
THROWN = 'thrw'
TWOHANDED = 'thnd'
VERSATILE = 'vers'
SILVERED = 'slvr'
WEAPONPROPERTY_CHOICES = [
	(AMMUNITION, 'Ammunition'),
	(FINESSE, 'Finesse'),
	(HEAVY, 'Heavy'),
	(LIGHT, 'Light'),
	(LOADING, 'Loading'),
	(RANGE, 'Range'),
	(REACH, 'Reach'),
	(SPECIAL, 'Special'),
	(THROWN, 'Thrown'),
	(TWOHANDED, 'Two-Handed'),
	(VERSATILE, 'Versatile'),
	(SILVERED, 'Silvered'),
]


# creature size options (3 char)
TINY = 'tny'
SMALL = 'sml'
MEDIUM = 'med'
LARGE = 'lar'
HUGE = 'hug'
GARGANTUAN = 'grg'
CREATURESIZE_CHOICES = [
	(TINY, 'Tiny'),
	(SMALL, 'Small'),
	(MEDIUM, 'Medium'),
	(LARGE, 'Large'),
	(HUGE, 'Huge'),
	(GARGANTUAN, 'Gargantuan'),
]

# resistances options (longest: 25 char)
	# not used directly in a model, imported to other modules to be
	# prompted as choices
	# 
	# these aren't abbreviated because it will be easier to have them
	# unabbreviated for populating menus
SLASHING = 'Slashing'
BLUDGEONING = 'Bludgeoning'
PIERCING = 'Piercing'
NONMAG_PHYSICAL = 'Nonmagical Physical'
NONMAG_SLASHING = 'Nonmagical Slashing'
NONMAG_BLUDGEONING = 'Nonmagical Bludgeoning'
NONMAG_PIERCING = 'Nonmagical Piercing'
NONSLV_PHYSICAL = 'Nonsilvered Physical'
NONSLV_SLASHING = 'Nonsilvered Slashing'
NONSLV_BLUDGEONING = 'Nonsilvered Bludgeoning'
NONSLV_PIERCING = 'Nonsilvered Piercing'
NONADM_PHYSICAL = 'Nonadamantium Physical'
NONADM_SLASHING = 'Nonadamantium Slashing'
NONADM_BLUDGEONING = 'Nonadamantium Bludgeoning'
NONADM_PIERCING = 'Nonadamantium Piercing'
ACID = 'Acid'
COLD = 'Cold'
FIRE = 'Fire'
FORCE = 'Force'
LIGHTNING = 'Lightning'
NECROTIC = 'Necrotic'
POISON = 'Poison'
PSYCHIC = 'Psychic'
RADIANT = 'Radiant'
THUNDER = 'Thunder'
RESISTANCE_CHOICES = [
	(SLASHING, SLASHING),
	(BLUDGEONING, BLUDGEONING),
	(PIERCING, PIERCING),
	(NONMAG_PHYSICAL, NONMAG_PHYSICAL),
	(NONMAG_SLASHING, NONMAG_SLASHING),
	(NONMAG_BLUDGEONING, NONMAG_BLUDGEONING),
	(NONMAG_PIERCING, NONMAG_PIERCING),
	(NONSLV_PHYSICAL, NONSLV_PHYSICAL),
	(NONSLV_SLASHING, NONSLV_SLASHING),
	(NONSLV_BLUDGEONING, NONSLV_BLUDGEONING),
	(NONSLV_PIERCING, NONSLV_PIERCING),
	(NONADM_PHYSICAL, NONADM_PHYSICAL),
	(NONADM_SLASHING, NONADM_SLASHING),
	(NONADM_BLUDGEONING, NONADM_BLUDGEONING),
	(NONADM_PIERCING, NONADM_PIERCING),
	(ACID, ACID),
	(COLD, COLD),
	(FIRE, FIRE),
	(FORCE, FORCE),
	(LIGHTNING, LIGHTNING),
	(NECROTIC, NECROTIC),
	(POISON, POISON),
	(PSYCHIC, PSYCHIC),
	(RADIANT, RADIANT),
	(THUNDER, THUNDER),
]

# standard models


class Campaign(models.Model):
	"""
	Defines campaigns. Campaigns are linked to an account. They are the
	outermost wrapper for collections of locations, encounters, items,
	creatures, and plot moments.
	"""

	title = models.CharField(max_length=50, verbose_name='Campaign Title')
	description = models.TextField(verbose_name='Description')
	ufk = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Location(models.Model):
	"""
	Defines locations. Locations are contained in campaigns (connected by
	mapping table).
	"""

	name = models.CharField(max_length=50, verbose_name='Location Name')
	terrain_type = models.CharField(max_length=6, verbose_name='Terrain Type',
		choices=TTYPE_CHOICES, blank=True)
	description = models.TextField(verbose_name='Description')
	ufk = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Encounter(models.Model):
	"""
	Defines encounters. Encounters are contained in campaigns (connected by
	mapping table).
	"""

	name = models.CharField(max_length=50, verbose_name='Encounter Name')
	encounter_type = models.CharField(verbose_name='Encounter Type',
		choices=ETYPE_CHOICES, max_length=6, blank=True)
	description = models.TextField(verbose_name='Description')
	ufk = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Item(models.Model):
	"""
	Defines items. Items are linked to an account. A relationship to an item
	may be created for campaigns, locations, encounters, creatures, and/or
	plot moments.
	"""

	name = models.CharField(max_length=50, verbose_name='Item Name')
	item_type = models.CharField(max_length=3, choices=ITYPE_CHOICES)
	description = models.TextField(verbose_name='Description')
	ufk = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Creature(models.Model):
	"""
	Defines creatures. Creatures are linked to an account. A relationship to a
	creature may be created for campaigns, locations, encounters, items, and
	or plot moments.
	"""

	name = models.CharField(max_length=50, verbose_name='Creature Name')
	description = models.TextField(verbose_name='Description')
	level = models.PositiveIntegerField(verbose_name='Level',
		help_text="This may be a creature's challenge rating, a player " +\
		"character's level, a number of hit die, or whatever else is being " +\
		"used to track a creature's agency in the world")
	creature_type = models.CharField(max_length=6,
		verbose_name='Creature Type',
		choices=CTYPE_CHOICES)
	max_hp = models.PositiveIntegerField(verbose_name='Maximum Hit Points')
	current_hp = models.PositiveIntegerField(verbose_name='Current Hit Points')
	resistances = models.TextField()
		# populated with json string
		# format: [<resname>, <resname>, ...]
	size = models.CharField(verbose_name='Size', max_length=3,
		choices=CREATURESIZE_CHOICES)
	str_score = models.PositiveIntegerField(verbose_name='Strength Score')
	dex_score = models.PositiveIntegerField(verbose_name='Dexterity Score')
	con_score = models.PositiveIntegerField(verbose_name='Constitution Score')
	int_score = models.PositiveIntegerField(verbose_name='Intelligence Score')
	wis_score = models.PositiveIntegerField(verbose_name='Wisdom Score')
	cha_score = models.PositiveIntegerField(verbose_name='Charisma Score')
	override_prof = models.PositiveIntegerField(verbose_name='Override ' +\
		'Proficiency Bonus', blank=True,
		help_text="Leave this blank to use the proficiency associated with " +\
		"the creature's level.")
	ufk = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class PlotMoment(models.Model):
	"""
	Defines plot moments. Plot moments are contained in campaigns (connected
	by mapping table). These are notes at their core, but there may be
	multiple relationships between creatures, locations, encounters and items
	and one plot moment.
	"""

	name = models.CharField(max_length=50, verbose_name='Plot Moment Name')
	description = models.TextField(verbose_name='Description')
	ufk = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Note(models.Model):
	"""
	Defines notes. Notes are linked to an account. If a campaign is made
	public, the notes are NOT duplicated for that campaign. Notes can be
	linked to anything else so that a user can keep track of small information.
	"""

	title = models.CharField(max_length=50, verbose_name='Note Title')
	text = models.TextField(verbose_name='Note Text')
	ufk = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class CreatureSkillProficiency(models.Model):
	"""
	Relates skills to creatures. Acts as a mapping table, but isn't pure
	mapping because it contains additional information (what kind of
	proficiency).
	"""

	proficiency_type = models.CharField(verbose_name='Proficiency Type',
		choices=PTYPE_CHOICES, max_length=4)
	skill = models.ForeignKey('Skill', on_delete=models.PROTECT)
	cr_fk = models.ForeignKey('Creature', on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = 'CreatureSkillProficiencies'


class Skill(models.Model):
	"""
	Defines each skill. There are a finite amount of these, but they are most
	easily represented and worked with via a database.
	"""

	name = models.CharField(max_length=16)
	ability = models.CharField(max_length=3, choices=ABILITY_CHOICES)


class CreatureToolProficiency(models.Model):
	"""
	Relates tools to creatures. Acts as a mapping table, but isn't pure
	mapping because it contains additional information (what kind of
	proficiency).
	"""

	proficiency_type = models.CharField(verbose_name='Proficiency Type',
		choices=PTYPE_CHOICES, max_length=4)
	tool = models.ForeignKey('Tool', on_delete=models.PROTECT)
	cr_fk = models.ForeignKey('Creature', on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = 'CreatureToolProficiencies'


class Tool(models.Model):
	"""
	Defines tools. There are a finite amount of tools, but they are most
	easily represented and worked with via a database.
	"""

	name = models.CharField(max_length=23)
	tool_category = models.CharField(max_length=3, choices=TOOLCAT_CHOICES,
		blank=True, null=True)
	description = models.TextField()


class WeaponProperty(models.Model):
	"""
	Defines properties a given weapon may have. A "weapon" is just an item
	where the selected type is weapon.
	"""

	wpn_fk = models.ForeignKey('Item', on_delete=models.CASCADE)
	wp_type = models.CharField(max_length=4, choices=WEAPONPROPERTY_CHOICES)

	class Meta:
		verbose_name_plural = 'WeaponProperties'


class Map(models.Model):
	"""
	Provides an image field in the database for maps to be stored.
	"""

	map_nme = models.CharField(max_length=30, verbose_name='Map Name')
	map_img = models.ImageField(upload_to='user_uploads/maps/',
		verbose_name='Map Image')
	ufk = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class CreatureInstance(models.Model):
	"""
	Defines instances of creatures. Creature instances are two fields: a foreign key to a creature and TextField which is populated by a json string.

	The json data is in the format of the `Creature` class json serializer (in aux_lib module).
	"""

	cre_fk = models.ForeignKey('Creature', on_delete=models.CASCADE)
	json = models.TextField()


# mapping tables


class CampaignMap(models.Model):
	"""
	Relates campaigns to maps.
	"""

	map_fk = models.ForeignKey('Map', on_delete=models.CASCADE)
	cam_fk = models.ForeignKey('Campaign', on_delete=models.CASCADE)


class CampaignLocation(models.Model):
	"""
	Relates campaigns to locations.
	"""

	cam_fk = models.ForeignKey('Campaign', on_delete=models.CASCADE)
	loc_fk = models.ForeignKey('Location', on_delete=models.CASCADE)


class CampaignEncounter(models.Model):
	"""
	Relates campaigns to encounters.
	"""

	cam_fk = models.ForeignKey('Campaign', on_delete=models.CASCADE)
	enc_fk = models.ForeignKey('Encounter', on_delete=models.CASCADE)


class CampaignItem(models.Model):
	"""
	Relates campaigns to items.
	"""

	cam_fk = models.ForeignKey('Campaign', on_delete=models.CASCADE)
	itm_fk = models.ForeignKey('Item', on_delete=models.CASCADE)


class CampaignCreature(models.Model):
	"""
	Relates campaigns to creatures.
	"""

	cam_fk = models.ForeignKey('Campaign', on_delete=models.CASCADE)
	cre_fk = models.ForeignKey('Creature', on_delete=models.CASCADE)


class CampaignPlotMoment(models.Model):
	"""
	Relates campaigns to plot moments.
	"""

	cam_fk = models.ForeignKey('Campaign', on_delete=models.CASCADE)
	plm_fk = models.ForeignKey('PlotMoment', on_delete=models.CASCADE)


class LocationMap(models.Model):
	"""
	Relates locations to maps.
	"""

	map_fk = models.ForeignKey('Map', on_delete=models.CASCADE)
	loc_fk = models.ForeignKey('Location', on_delete=models.CASCADE)


class LocationEncounter(models.Model):
	"""
	Relates locations and encounters.
	"""

	loc_fk = models.ForeignKey('Location', on_delete=models.CASCADE)
	enc_fk = models.ForeignKey('Encounter', on_delete=models.CASCADE)


class LocationItem(models.Model):
	"""
	Relates locations and items.
	"""

	loc_fk = models.ForeignKey('Location', on_delete=models.CASCADE)
	itm_fk = models.ForeignKey('Item', on_delete=models.CASCADE)


class LocationCreature(models.Model):
	"""
	Relates locations and creatures.
	"""

	loc_fk = models.ForeignKey('Location', on_delete=models.CASCADE)
	cre_fk = models.ForeignKey('Creature', on_delete=models.CASCADE)


class LocationPlotMoment(models.Model):
	"""
	Relates locations and plot moments.
	"""

	loc_fk = models.ForeignKey('Location', on_delete=models.CASCADE)
	plm_fk = models.ForeignKey('PlotMoment', on_delete=models.CASCADE)


class EncounterItem(models.Model):
	"""
	Relates encounters and items.
	"""

	enc_fk = models.ForeignKey('Encounter', on_delete=models.CASCADE)
	itm_fk = models.ForeignKey('Item', on_delete=models.CASCADE)


class EncounterCreature(models.Model):
	"""
	Relates encounters and creatures.
	"""

	enc_fk = models.ForeignKey('Encounter', on_delete=models.CASCADE)
	cre_fk = models.ForeignKey('Creature', on_delete=models.CASCADE)


class EncounterPlotMoment(models.Model):
	"""
	Relates encounters and plot moments.
	"""

	enc_fk = models.ForeignKey('Encounter', on_delete=models.CASCADE)
	plm_fk = models.ForeignKey('PlotMoment', on_delete=models.CASCADE)


class ItemCreature(models.Model):
	"""
	Relates items and creatures.
	"""

	itm_fk = models.ForeignKey('Item', on_delete=models.CASCADE)
	cre_fk = models.ForeignKey('Creature', on_delete=models.CASCADE)


class ItemPlotMoment(models.Model):
	"""
	Relates items plot moments.
	"""

	itm_fk = models.ForeignKey('Item', on_delete=models.CASCADE)
	plm_fk = models.ForeignKey('PlotMoment', on_delete=models.CASCADE)


class CreaturePlotMoment(models.Model):
	"""
	Relates creatures and plot moments.
	"""

	cre_fk = models.ForeignKey('Creature', on_delete=models.CASCADE)
	plm_fk = models.ForeignKey('PlotMoment', on_delete=models.CASCADE)


class NoteCampaign(models.Model):
	"""
	Relates notes and campaigns.
	"""

	nte_fk = models.ForeignKey('Note', on_delete=models.CASCADE)
	cam_fk = models.ForeignKey('Campaign', on_delete=models.CASCADE)


class NoteLocation(models.Model):
	"""
	Relates notes and locations.
	"""

	nte_fk = models.ForeignKey('Note', on_delete=models.CASCADE)
	loc_fk = models.ForeignKey('Location', on_delete=models.CASCADE)


class NoteEncounter(models.Model):
	"""
	Relates notes and locations.
	"""

	nte_fk = models.ForeignKey('Note', on_delete=models.CASCADE)
	enc_fk = models.ForeignKey('Encounter', on_delete=models.CASCADE)


class NoteItem(models.Model):
	"""
	Relates notes and items.
	"""

	nte_fk = models.ForeignKey('Note', on_delete=models.CASCADE)
	itm_fk = models.ForeignKey('Item', on_delete=models.CASCADE)


class NoteCreature(models.Model):
	"""
	Relates notes and creatures.
	"""

	nte_fk = models.ForeignKey('Note', on_delete=models.CASCADE)
	cre_fk = models.ForeignKey('Creature', on_delete=models.CASCADE)


class NotePlotMoment(models.Model):
	"""
	Relates notes and plot moments.
	"""

	nte_fk = models.ForeignKey('Note', on_delete=models.CASCADE)
	plm_fk = models.ForeignKey('PlotMoment', on_delete=models.CASCADE)
