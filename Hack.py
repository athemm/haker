import os 
if os.name == "posix":
    P = "\r\x1b[0m\x1b[35;1m[+]\x1b[32;m "
    print(P + "Adding hax.sys")
    os.system("sleep 0.7")
    print(P + "Analyzing AppStore")
    print("\x1b[31m")
    os.system("cat /dev/urandom|head -n1100|xxd")
    print(P + "Adding XNU")
    os.system("sleep 0.5")
    print(P + "Finding created WASM ShellCode... MAGIC HAX FOUND!!!")
    print(P + "HACKED!!!")
else:
  os.system('color 0a') 
  print("hacked!")
