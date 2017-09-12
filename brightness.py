print("Enter brightness in %(0,100):",end='')
path="/sys/devices/pci0000:00/0000:00:02.0/drm/card0/card0-LVDS-1/intel_backlight/brightness"
br_file=open(path,'w')
br=int(input())
if(br<1 or br>100):
    exit
else:
    brightness=int((br*4882)/100)
    br_file.write(str(brightness))
    br_file.close()
