# Dasturchi: Obitov Suhrob
'''

Diqqat!!!
bu dasturni ishlatishdan avval ursina modulini o`rnatishigiz zarur
o`rnatish uchun CMD ga pip install ursina den yozishingiz zarur!
agar sizda pip yo`q bo`lsa brauzerga get pip deb yozasiz va 
birinchi saytga kirib pip ni yuklaysiz!  

'''
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
# Blok yaratildi
class Voxel(Button):
	def __init__(self, position = (0,1,0)):
		super().__init__(
			parent = scene,
			position = position,
			# bu yerda bloklar kub ekanligi aytilmoqda
			model = 'cube',
			origin_y = 0.5,
			texture = 'white_cube',
			color = color.color(0,0,random.uniform(0.9,1)),
			highlight_color = color.gold)
	def input(self, key):
		if self.hovered:
			# bu yerda sichqonchaning chap tugmasi bosilganda yangi blok yarat degan buyruq berilmoqda 
			if key == 'left mouse down':
				voxel = Voxel(position = self.position + mouse.normal)
			# bu yerda sichqonchaning o`ng tugmasi bosilganda blokni o`chir degan buyruq berilmoqda
			if key == 'right mouse down':
				destroy(self)

# bu yerda voxel classi (ya`ni bloklar) x o`qida necha marta bo`lishi va y o`qida necha marta bo`lishi berilmoqda 
for z in range(30):
	for x in range(20):
		voxel = Voxel(position = (x,0,z))

# O`yinchi yaratildi
player = FirstPersonController()
# o`yinchining joylashuvi
player.position = (2,50,2)

app.run()
