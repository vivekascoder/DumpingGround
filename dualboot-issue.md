## Faced on Kali 20.02


*The Problems are hardware dependent so you may or may not be able to face them but it's good to know about them.*


### Issues List:

* Time Issue:
  * So this is the issue that i've faced and the simple reason is because we need to use the UTC timezone.
  * Take a look at `timedatectl` command.
* Microphone Issue:
  * This is the issue that i've faced in both Kali and Ubuntu now. The problem happens when you need to record the audio. There will be infinite noise.
  * To fix it simply use the `pulseaudio` program and reduce the volume of microphone.
* Bluetooth Issue: 
  * Yeah, i was dumb, just enable it with.
  * `sudo service bluetooth/bluemon start`
* Scaling Issue:
  * It's because the resolution of my monitor is quite high `190x1080` and the fractional scaling was not available in `Ubuntu 18.04` but no problem with kali 20.02


### Final Words:


The thing that you need to know i that no matter how many issues you faced in linux although all of them can be fixed you need to struggle in the beginning to understand this Linux


### Join `#LOSS` community on Social media.


Mail me to join:


[Vivekascoder](mailto:vivekascoder@gmail.com)



[Personal Mail](mailto:pbqre@pm.me)
