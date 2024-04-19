# Get the IP address

There are many ways to know the IP address, and two of them are listed as follows.

**Checking via the router**

If you have permission to log in the router(such as a home network), you can check the addresses assigned to Raspberry Pi on the admin interface of router.

The default hostname of the Raspberry Pi OS is raspberrypi, and you need to find it. (If you are using ArchLinuxARM system, please find alarmpi.)





sadas




;pkl

**Step 1**: Enable the I2C port of your Raspberry Pi (If you have enabled it, skip this; if you do not know whether you have done that or not, please continue).

```
sudo raspi-config
```

**3 Interfacing options**

![](./img/image282.png)

**P5 I2C**

![](./img/image283.png)

**<Yes>, then <Ok> -> <Finish>**

![](./img/image284.png)

**Step 2:** Check whether the i2c modules are loaded and active.

```
lsmod | grep i2c
```

Then the following codes will appear (the number may be different).

```
i2c_dev                     6276    0
i2c_bcm2708                 4121    0
```

**Step 3:** Install i2c-tools.

```
sudo apt-get install i2c-tools
```

**Step 4:** Check the address of the I2C device.

```
i2cdetect -y 1      # For Raspberry Pi 2 and higher version

i2cdetect -y 0      # For Raspberry Pi 1
```

```
pi@raspberrypi ~ $ i2cdetect -y 1
    0  1  2  3   4  5  6  7  8  9   a  b  c  d  e  f
00:           -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- 48 -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```

If there is an I2C device connected, the address of the device will be displayed.

**Step 5:**

**For C language users:** Install libi2c-dev.

```
sudo apt-get install libi2c-dev
```

**For Python users:** Install smbus for I2C.



















sad



















kjlkjljh




xxcx
x
x
x
x
xcxvxcv
x
xxcv
x
x
x


xcvxcv

xcvcv














xcvxcv

##b
<a id="b"></a>

**Network Segment Scanning**

You can also use network scanning to look up the IP address of Raspberry Pi. You can apply the software, **Advanced IP scanner** and so on.

Scan the IP range set, and the name of all connected devices will be displayed. Similarly, the default hostname of the Raspberry Pi OS is raspberrypi, if you haven’t modified it.



