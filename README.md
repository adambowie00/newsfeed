# newsfeed
Displaying RSS feeds on a Pimoroni Inky wHAT E-Ink Display

A simple RSS title viewer designed to display news headlines on an E Ink display, powered by a Raspberry Pi Zero W or Raspberry Pi Zero 2 W.

This was designed to replace a similar viewer which used Twitter feeds to populate the display. Following recent changes with Twitter/X and a minimum $100/month fee for accessing their API, I have rewritten the project to use RSS feeds.

I've probably added more detail than many will need, but it may help some beginners!

## Requirements

1. Raspberry Pi Zero W with Headers or Raspberry Pi Zero 2 W with Headers. Note that while you could use any regular sized Raspberry Pi, this would probably be overkill for this project which only runs a small amount of undemanding code. Either buy a pre-soldered "With Headers" model of the Pi Zero W, or you will need to solder some headers on.
2. Micro SD Card. 8GB or 16GB should be sufficient.
3. Pimoroni Inky wHAT. I am using a Pimoroni branded 4.2" screen with a resolution of 400x300 pixels. You could obviously use other devices, but will need to amend the code and libraries accordingly. Note that Inky wHAT comes in Black/White, Red/Black/White and Yellow/Black/White versions. The code here is written for the Red/Black/White model, but can be amended for the slightly cheaper Black/White or Yellow/Black/White versions.
4. Micro USB Power Supply

Additionally, for set-up you will need a keyboard, monitor and mouse, an HDMI cable, a mini-HDMI to HDMI adpater and micro-USB to USB-A adapter. Alternatively, you could complete the set-up using SSH to remote into the device (unless you complete the set-up using SSH).

## OS Set-up

The easiest way to set things up is to use the official [Raspberry Pi Installer Software](https://www.raspberrypi.com/software/) available for Windows, MacOS and Ubuntu. I like to use the Advanced set-up via the gear cog icon, which allows me to name the device, set-up my WiFi SSID and password, enable SSH (for headerless set-up), and change any language or geography settings.

## Hardware Set-up

Mount the Inky wHAT onto the Raspberry Pi's 40 pin header, and boot up the computer. Note that the first boot may take some time.

Then, either using a monitor and keyboard, or using SSH, run the usual updates.

`sudo get update`
`sudo get full-upgrade`

This will take quite a long time on a Pi Zero W.

With the OS up to date, SPI and I2C both need to enabled, which can be done from within the Raspberry Pi Configuration settings. From a Terminal window/SSH type

`raspi-config`

Navigate to Interfaces and enable both SPI and I2C in that menu.

Then install Pimoroni's libraries for the Inky wHAT using either:

`curl https://get.pimoroni.com/inky | bash`

or

`sudo pip install inky[rpi,example-depends]`

## Code

I would note that I am a terrible coder, and there may well be better ways of doing the things I've attempted here, which uses Pimoroni examples and other bits of code as a means to an end.

In particular note that references to "red" and "RED" should be changed to another colour if your Inky wHAT is not a Red/Black/White model.

You should also change the USERNAME to your chosen username.

You will also need to provide a font file, and place that file in the same directory as the main **newsfeeds_inky.py** code.

Finally, amend the RSS feeds to whichever feeds you want to monitor.

Run the code by typing:

`python newsfeeds_inky.py`

It will take some seconds to update, clearing the screen and presenting the updated headlines and sources in black and red lettering respectively.

## Make It Run Automatically

To enable it to autorun on boot, and therefore run without any intervention.

Change the permissions to make it properly executable.

`chmod +x newsfeeds_inky.py`

Then set-up **crontab** to run the program on a regular basis. I've set mine to run every 15 minutes.

`crontab -e`

Choose **nano** if you're given an option. Navigate to the bottom of the file and add the following line to give it 15 minute updates:

`*/15 * * * * python /path/to/your/folder/newsfeeds_inky.py`

Change **/path/to/your/folder/** to the correct folder on your device where the code is saved e.g. /home/pi/inky/news/

Save and exit from Crontab.

## Possible Issues

Different outlets use RSS in different ways. This code collects the most **recent** story published on a given feed. But that may not be the most **important** story currently! So this is not necessarily a **Breaking News machine**! That said, more important stories, get written about more frequently, so the chances are likely to be higher that big stories surface on the device.

There isn't a great deal of space on my chosen disaply, and I'm only using the **Title** of the each RSS feed entry. Titles are designed for you to click on to read the story which you can't do on this device. But some news providers do use long Titles, perhaps for SEO purposes, and in that case, it's possible that titles overlap with one another. Your mileage may vary.

The code could certainly be rewritten to take into account the number of lines of space that are available!

## Next Steps

I think that ideally this would run on something that uses even less power. A Raspberry Pi Pico W would seem sufficient.
