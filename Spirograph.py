from graphics import *
import math as j
import time

#Wheels in the spirograph
#The first one is the outermost wheel, and the last one is the innermost wheel.
#This list is the most fun to experiment with.
wheels = [10, 3]

#Angles of the wheels
#This does not need to get changed if you want all of the wheels to start in the same place.
#Weird stuff happens if there are 1 fewer numbers in here than in wheels, but it looks cool.
wthetas = [0 for i in range(len(wheels))]

#Pencil points
#This controls where the lines are drawn from, relative to the center of the innermost wheel.
#Experimenting with this can be fun(as numbers in here can be larger than the radius of the innermost wheel),
#but it has less effect on the final spirograph than the wheels themselves.
ppoints = [2]

#Angles of the pencil points
#Similar to the angles of the wheels, except it has more of an effect on the finished product.
pointangles = [0 for i in range(len(ppoints))]

#Line precision
#How often a point is calculated, in degrees.
#The lower the value is, the smoother the final drawing will look, and the longer it will take to create.
precision = 5

#Background color
#Entirely for aesthetics.
#The colors(this and all future colors) are in rgb, not hsl.
bgcolor = (0, 0, 0)

#Line colors
#This list does not need to be the same length as the ppoints list.
#The program will automatically fill it if it's too short.
color = [(0, 0, 255)]

#Circle colors
#The colors of the fancy spirograph circles.
#This list doesn't matter if you aren't drawing the spirograph circles.
#Again, this list does not need to be the same length as the wheels list.
ccolor = [(255, 0, 0)]

#The width of the window, in pixels.
width = 600

#The height of the window, in pixels.
height = 600

#The delay between drawing lines.
#Adding a bit of delay makes it look nice and aesthetic, but adding too much delay will make you sad when it runs slowly.
#0.01 or 0.001 are good values for delay.
#If delay is set to 0, the screen will not update between lines to prevent crashing.
delay = 0.01

#If this is set to True, the circles representing spirograph wheels will be drawn.
#If this is set to False, the circles will not be drawn.
#Note that setting it to false will make the program run faster.
crurclis = True

#If this is set to True, the circles will break several laws of physics and go the wrong way.
#Like, seriously the wrong way.
#Like, gears with teeth literally going through each other.
#Hey, it looks cool, though.
#If you care about physics, keep this set to False.
backwards = False

#If this is set to True, the lines in the spirograph will be drawn.
#If this is set to False, the lines in the spirograph will not be drawn.
#I would recommend that you only set one variable between this and "crurclis" to False, or else it will be extremely boring.
#But hey, who am I to stop you from living your best life?
liness = True

#Don't change this. Please. It might break something.
#I mean, you can if you want, but it's not my fault if something breaks.
f = []

#Finding the distances between the centers of the wheels
cdist = [wheels[i] - wheels[i + 1] for i in range(len(wheels) - 1)]

#Creating the graph bounds
#This isn't the most readable piece of code I've ever made, but I've been enjoying making one-liners.
#This should work for any combination of wheels, but if it doesn't, sorry.
gbounds = max(wheels) if all([item < min(wheels) for item in ppoints]) else max(wheels) + (max(ppoints) - min(wheels))

#Initializing the drawing surface
win = GraphWin(" ", width, height, autoflush = False)
win.setCoords(gbounds * -1, gbounds * -1, gbounds, gbounds)
win.setBackground(color_rgb(bgcolor[0], bgcolor[1], bgcolor[2]))

#Filling the line color and background color lists, just in case they aren't long enough.
#This should help prevent errors.
if len(color) < len(ppoints):
    color = [color[i % len(color)] for i in range(len(ppoints))]

if len(ccolor) < len(wheels):
    ccolor = [ccolor[i % len(ccolor)] for i in range(len(wheels))]

#A simple function to create lines in the graph.
def lines(starts, ends):
    for i in range(len(starts)):
        #Creating a line object in this particular module.
        linne = Line(Point(starts[i][0], starts[i][1]), Point(ends[i][0], ends[i][1]))

        #Setting its color.
        linne.setFill(color_rgb(color[i][0], color[i][1], color[i][2]))

        #Drawing it to the window(so that you can actually see it. you're welcome.).
        linne.draw(win)

#A less-simple function to update the position of the spirograph.
def get_point(wthetas, wheels, ppoints):
    global cdist
    #Converting things to radians because trig.
    wt = [j.radians(item) for item in wthetas]

    #Probably making the last point or something.
    last = wt[-1]

    #Initializing some variables.
    dtowheelx = 0
    dtowheely = 0
    for i in range(len(cdist)):
        #If you wanted it to draw circles:
        if crurclis:
            #Make a circle
            corcle = Circle(Point(dtowheelx, dtowheely), wheels[i])
            #Color it
            corcle.setOutline(color_rgb(ccolor[i][0], ccolor[i][1], ccolor[i][2]))
            #Put it in the undraw list
            f.append(corcle)
            #Draw it
            corcle.draw(win)

        #It should probably also update the positions of all of the circles, since that's literally the goal of the function.
        dtowheelx += j.cos(wt[i]) * cdist[i]
        dtowheely += j.sin(wt[i]) * cdist[i]

    #But wait, there are more circles!
    if crurclis:
        #(well, there's only actually one, but it's a good one)
        corcle = Circle(Point(dtowheelx, dtowheely), wheels[i + 1])
        corcle.setFill(color_rgb(ccolor[-1][0], ccolor[-1][1], ccolor[-1][2]))
        f.append(corcle)
        corcle.draw(win)
        for point in range(len(ppoints)):
            #Drawing all of the pencil points, and making them the right color.
            pont = Circle(Point(dtowheelx + (j.cos(last + j.radians(pointangles[point])) * ppoints[point]), dtowheely + (j.sin(last + j.radians(pointangles[point])) * ppoints[point])), gbounds / (20 + len(ppoints))) #(wheels[i + 1]) / 10)
            pont.setFill(color_rgb(color[point][0], color[point][1], color[point][2]))
            f.append(pont)
            pont.draw(win)

    #Okay, this is a very large one-liner.
    #This hideous block of code is the thing that actually updates the positions of all of the points.
    #It also puts it in a nice lists because there aren't enough lists here already.
    return [(dtowheelx + (j.cos(last + j.radians(pointangles[point])) * ppoints[point]), dtowheely + (j.sin(last + j.radians(pointangles[point])) * ppoints[point])) for point in range(len(ppoints))]

#Back to initializing some variables, now that we have some nice functions.

#A list that will soon have the values that all of the circles need to change by each time the position updates.
#After all, it would be far too simple if each circle had the same circumference and rotated the same amount every time.
dthetas = [precision]

#Right now, this is the circumference of the outer circle, but it will be the circumference of each successive circle as this iterates.
pcircum = (j.pi * (2 * wheels[0]))

#Some pretty useful but small variables.
#These are used to make it so that the circles do what gears actually do and rotate against each other.
times = -1
thimes = -1

#If you turned on "backwards", of course, it ignores all of that.
if backwards:
    times = 1
    thimes = 1

#Time to figure out how much to turn things.
#Note that this doesn't do the outer circle(the [1:]) because it's already been done.
for item in wheels[1:]:
    #The circumference of the current circle.
    ccircum = (j.pi * (2 * item))

    #This is a weird line that could probably be optimized, but I don't really want to optimize it.
    #Essentially, you have two circles that are touching each other, and you want to figure out how much one circle
    #will change if you turn the other circle a given amount.
    delta = (360 / (ccircum / ((pcircum / 360) * precision)))

    #Yay, now we want to use that value!
    dthetas.append(delta * times)

    #Making gears turn against each other, like real gears.
    times *= thimes

    #Next circle time!
    pcircum = ccircum

#This whole chunk of code is to figure out how few rotations the program can do and still get back to the original spot.
#Essentially, you just have to take the lcm of all of the radii of the wheels.
def lcm(a, b):
    return abs(a*b) // j.gcd(a, b)
rotations = 1
for item in wheels:
    rotations = lcm(rotations, item)
#Then you divide it by the radius of the outer circle because math.
rotations = int(rotations / wheels[0])
#A rough estimate of how many years this is going to take.
print(rotations, "rotations")

#Yay! Time to actually do something, and we're only ~200 lines in!
#This is what I get for writing so many comments.

#Getting the starting points.
starts = get_point(wthetas, wheels, ppoints)
for i in range((rotations * int(360 / precision)) + 1):
    #Undrawing all of the circles.
    #This is what would break if you changed the part where it creates f.
    for item in f:
        item.undraw()
    
    #Getting the end segments of the lines.
    ends = get_point(wthetas, wheels, ppoints)

    #If you're drawing lines, draw lines.
    if liness:
        lines(starts, ends)

    #Yay! More one-liners.
    #This just updates the rotations of all of the circles.
    #A short guide to map() and lambda:
        #map() will apply a function to lists. It's super useful, but it returns a weird thing that I don't actually understand,
        #which is what the list() is for.
        #map() makes it so that I don't need to do this:
        #for i in range(len(wthetas)):
        #    wthetas[i] = (lambda x, y: x + y), wthetas[i], dthetas[i])

        #lambda basically creates an anonymous function. It makes it so that I don't need to do this:
        #def add(x, y):
        #    return x + y
        #It's really fun to experiment with lambda, and it's super useful for short snippets like this.
    #Together, they just simplify and hopefully speed up the code.
    #Without them, this single line would be:
    #
    #def add(x, y):
    #    return x + y
    #
    #for i in range(len(wthetas)):
    #    wthetas[i] = add(wthetas[i], dthetas[i])*
    #
    #That may be more readable, but it's far less compact.
    #*(note that I realize that I could have done wthetas[i] += dthetas[i], but what I did is good for this example)
    wthetas = list(map((lambda x, y: x + y), wthetas, dthetas))

    #The ending points have to become the new starting points.
    starts = ends

    #aesthetic
    if delay > 0:
        update()
        time.sleep(delay)

#Clearing the circles at the end so you can admire the beautiful picture.
for item in f:
    item.undraw()

#:)
#Please do not use this for evil.
