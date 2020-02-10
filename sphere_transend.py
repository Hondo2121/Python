from mcpi.minecraft import Minecraft
from mcpi import block
from   time import sleep
import random
import math
pi = math.pi
sin = math.sin
cos = math.cos
def init():
 ipString = "127.0.0.1"
 #ipString = "192.168.7.226"
 #mc = Minecraft.create("127.0.0.1", 4711)
 mc = Minecraft.create(ipString, 4711)
 mc.setting("world_immutable",False)
 #x, y, z = mc.player.getPos()  
 return mc

def platForm(mc,l,h,w,T):
	x,y,z = mc.player.getPos()
	mc.setBlocks(x-l,y-h,z-w,x+l,y+h,z+w,T)
	
def matrixZ(mc,x,y,z):
    m = [[1,2,3,4,5,6,7,8,9,10,11],
        [12,13,14,15,1,2,3,4,5,6]]      
    print(m)
    for k in range (0,2):
        for l  in range (0,11):
            print(m[k][l],end="")
            theBlock = m[k][l]
            #if (theBlock == 7):
             #   theBlock = 47;
            #if (theBlock == 4):
              #  theBlock = 14;
            #if (theBlock == 1):
             #   theBlock = 103
            mc.setBlock(x,9+y-k,z+l,35,theBlock)
    print()

def worldWalker(mc,B):
	while(True):
		x,y,z = mc.player.getPos()
		sleep(0	)
		mc.setBlock(x,y-1,z,B)

def worldEater(mc):
	while(True):
		x=random.randint(-255,255)
		y=random.randint(1,128)
		z=random.randint(-255,255)
		if(mc.getBlock(x,y,z) == 0):
			mc.setBlock(x,y,z,8)
		print("deleting " +str(x)+","+str(y)+","+str(z))
			
def createSphere(r,mc,N,t,p):
	lst = []
	thetas = [(2*pi*i)/N for i in range(N)]
	print("thetas", thetas)
	phis = [(pi*i)/N for i in range(N)]
	x1,y1,z1=mc.player.getPos()
	for theta in thetas:
		for phi in phis:
			x = (r * sin(phi) * cos(theta)) + x1
			y = r * sin(phi) * sin(theta) +y1
			z = r * cos(phi) + z1	
			mc.setBlock(x,y,z,t,p)
    
def main():
 mc = init()
 x,y,z = mc.player.getPos()
 #mc.postToChat("Hondo21")
 matrixZ(mc,x+10,y,+5)
 #platForm(mc,10,0,10,1)
 #createSphere(25,mc,200,89,0)
 #mc.player.setPos(x,y+27,z)
 #print("teleporting")
 #worldWalker(mc,41)
 #worldEater(mc)


if __name__ == "__main__":
 main()

"""
AIR                   0
STONE                 1
GRASS                 2
DIRT                  3
COBBLESTONE           4
WOOD_PLANKS           5
SAPLING               6
BEDROCK               7
WATER_FLOWING         8
WATER                 8
WATER_STATIONARY      9
LAVA_FLOWING         10
LAVA                 10
LAVA_STATIONARY      11
SAND                 12
GRAVEL               13
GOLD_ORE             14
IRON_ORE             15
COAL_ORE             16
WOOD                 17
LEAVES               18
GLASS                20
LAPIS_LAZULI_ORE     21
LAPIS_LAZULI_BLOCK   22
SANDSTONE            24
BED                  26
COBWEB               30
GRASS_TALL           31
WOOL                 35
FLOWER_YELLOW        37
FLOWER_CYAN          38
MUSHROOM_BROWN       39
MUSHROOM_RED         40
GOLD_BLOCK           41
IRON_BLOCK           42
STONE_SLAB_DOUBLE    43
STONE_SLAB           44
BRICK_BLOCK          45
TNT                  46
BOOKSHELF            47
MOSS_STONE           48
OBSIDIAN             49
TORCH                50
FIRE                 51
STAIRS_WOOD          53
CHEST                54
DIAMOND_ORE          56
DIAMOND_BLOCK        57
CRAFTING_TABLE       58
FARMLAND             60
FURNACE_INACTIVE     61
FURNACE_ACTIVE       62
DOOR_WOOD            64
LADDER               65
STAIRS_COBBLESTONE   67
DOOR_IRON            71
REDSTONE_ORE         73
SNOW                 78
ICE                  79
SNOW_BLOCK           80
CACTUS               81
CLAY                 82
SUGAR_CANE           83
FENCE                85
GLOWSTONE_BLOCK      89
BEDROCK_INVISIBLE    95
STONE_BRICK          98
GLASS_PANE          102
MELON               103
FENCE_GATE          107
GLOWING_OBSIDIAN    246
NETHER_REACTOR_CORE 247
"""
