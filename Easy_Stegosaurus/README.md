# Easy Stegosaurus

### Challenge
>Keith infiltrated the scary evil organization ZORE, and had to fight a cloned stegosaurus!

> After killing the evil beast, they started to dissect the body for potential information. They found a usb containing two similar looking image files: one called [logo.png](logo.png), and one called [changed.png](changed.png).

> What secret information could be contained in these strange files? 

### Solution
From the name, it is using steganography. We shall [StegSolve by Caesum](http://www.caesum.com/handbook/Stegsolve.jar).
However, since 2 images are given, we should use `Analyse > Image Combiner` mode.

Here's where we must be careful. We must open `logo.png` first, before combining with `changed.png` and not the other way round!
***I did the other way round initially and got no results.*** `:(`

Switch to SUB mode and we see the flag: `sammyshouldworkmore`

![solved.bmp](solved.bmp)