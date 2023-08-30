import sys,datetime
import feedparser

from inky import InkyWHAT

inky_display = InkyWHAT("red") # Change this according to your wHAT model
inky_display.set_border(inky_display.RED) # Again change RED if neccessary

from PIL import Image, ImageFont, ImageDraw

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

# Note that you need to have a font file installed. I'm using Arial here.
# Also note that the location of your file will depend on your
# username. Change "[USERNAME]" accordingly without square brackets
# e.g. to "pi"

font = ImageFont.truetype("/home/[USERNAME]/Pimoroni/inky/news/arial.ttf", 18)
font_small = ImageFont.truetype("/home/[USERNAME]/Pimoroni/inky/news/arial.ttf", 14)

# This function will take a quote as a string, a width to fit
# it into, and a font (one that's been loaded) and then reflow
# that quote with newlines to fit into the space required.

# I have borrowed this code!

def reflow_feed(quote, width, font):
    words = quote.split(" ")
    reflowed = ' '
    line_length = 0

    for i in range(len(words)):
        word = words[i] + " "
        word_length = font.getsize(word)[0]
        line_length += word_length

        if line_length < width:
            reflowed += word
        else:
            line_length = word_length
            reflowed = reflowed[:-1] + "\n " + word

    return reflowed

# Because I am using an Inky wHAT display, and RSS feed titles tend
# to be quite short, I have found that with a 400 x 300 display
# there is room for around four feeds to be displayed.

# The code includes four RSS feeds. Make adjustments to each
# of these accordingly.
# Also change references to RED if you have a different wHAT model.

# First feed

rss_url_1 = 'https://www.bbc.com/news/world/rss.xml'
feed_1 = feedparser.parse(rss_url_1)
most_recent_title_1 = feed_1.entries[0].title

reflowed_most_recent_title_1 = reflow_feed(most_recent_title_1, inky_display.WIDTH, font)

draw.text((0, 0), "BBC News", inky_display.RED, font)
draw.text((0, 20), reflowed_most_recent_title_1, inky_display.BLACK, font)

# Second feed

rss_url_2 = 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'
feed_2 = feedparser.parse(rss_url_2)
most_recent_title_2 = feed_2.entries[0].title

reflowed_most_recent_title_2 = reflow_feed(most_recent_title_2, inky_display.WIDTH, font)

draw.text((0, 75), "New York Times", inky_display.RED, font)
draw.text((0, 95), reflowed_most_recent_title_2, inky_display.BLACK, font)

# Third feed

rss_url_3 = 'https://ft.com/world?format=rss'
feed_3 = feedparser.parse(rss_url_3)
most_recent_title_3 = feed_3.entries[0].title

reflowed_most_recent_title_3 = reflow_feed(most_recent_title_3, inky_display.WIDTH, font)

draw.text((0, 150), "Financial Times", inky_display.RED, font)
draw.text((0, 170), reflowed_most_recent_title_3, inky_display.BLACK, font)

# Fourth feed

rss_url_4 = 'https://theverge.com/rss/index.xml'
feed_4 = feedparser.parse(rss_url_4)
most_recent_title_4 = feed_4.entries[0].title

reflowed_most_recent_title_4 = reflow_feed(most_recent_title_4, inky_display.WIDTH, font)

draw.text((0, 225), "The Verge", inky_display.RED, font)
draw.text((0, 245), reflowed_most_recent_title_4, inky_display.BLACK, font)

# Capture the updated time/date

now = datetime.datetime.now()
last_update = "Updated: " + now.strftime("%d-%m-%y %H:%M")
draw.text((230,285), last_update, inky_display.RED, font_small)

# Display the output

inky_display.set_image(img)
inky_display.show()
