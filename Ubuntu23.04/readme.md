## Issues while installing eSim in ubuntu 23.04 using the install-esim.sh script

# Isuue 1 : line number: 158-168   file: install-eSim.sh
```Description
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.
    
    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.
    
    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.
    
    See /usr/share/doc/python3.12/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.

   
```
`Reason` : Ubuntu 23 dosn't allow system wide package installation using pip

# FIX : 
      1)  use pipx 
      2)  use a virtual enviornement 
I suceesfully fixed that issueerror: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.
    
    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.
    
    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.
    
    See /usr/share/doc/python3.12/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
 using the virtual environment aproach , However I also tried the pipx but was not able to install one package with it 

# Issue 2 : line number: 53-54  : file:nghdl/install-nghdl.sh 
```
Error while installing llvm-9 and llvm-9-dev

```
Reason :  I think  Ubuntu 24.04 have no support for the older versions of llvm i.e version 9 because the latest version of llvm is 20 or 18

Temporary Fix :
```
I build llvm 9.0.1 from source on my virtual machine running Ubuntu 23.04
```

# Issue 4 : line number:274 : file:nghdl/install-nghdl.sh
GHDL installation failed
```
Compilation failed

trans-chap2.adb:1043:43: warning: pragma Unreferenced given for "Final" [enabled by default]
gnatmake: "/home/avinash/Downloads/eSim-2.4/nghdl/ghdl-0.37/src/vhdl/translate/trans-chap2.adb" compilation error
make[1]: *** [src/ortho/llvm4-nodebug/Makefile:14: ghdl1-llvm] Error 4
make[1]: Leaving directory '/home/avinash/Downloads/eSim-2.4/nghdl/ghdl-0.37'
make: *** [Makefile:344: ghdl1-llvm] Error 2

```
Reason : Unknown
Fix :  May be fixed if we compile with older versions of ada compiler

# Issue 5 : line no: 275  file:nghdl/install-nghdl.sh
Verilator installation failed 
fix : sucessfuly fixed the issue by adding the "memory" header file which was causing compilation error


## Summary Of Issues
# install-eSim.sh 
                                                                               
  <table>
    <tr>
        <th>Function</th>
        <th>Earlier Status</th>
        <th>Now Status</th>
    </tr>
    <tr>
        <td>createConfigFile</td>
        <td>-</td>
        <td>-</td>
    </tr>
    <tr>
        <td>installDependency</td>
        <td>Failed</td>
        <td>success</td>
    </tr>
    <tr>
        <td>installKicad</td>
        <td>success</td>
        <td>success</td>
    </tr>
    <tr>
        <td>copyKicadLibrary</td>
        <td>success</td>
        <td>success</td>
    </tr>
    <tr>
        <td>installNghdl</td>
        <td>failed</td>
        <td>failed</td>
    </tr>
    <tr>
        <td>installSky130Pdk</td>
        <td>success</td>
        <td>success</td>
    </tr>
    <tr>
        <td>createDesktopStartScript</td>
        <td>-</td>
        <td>-</td>
    </tr>
</table>

# nghdl/install-nghdl.sh

<table>
  <thead>
    <tr>
      <th>Function</th>
      <th>Earlier Status</th>
      <th>Now Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>installGHDL</td>
      <td>failed</td>
      <td>failed</td>
    </tr>
    <tr>
      <td>installVerilator</td>
      <td>failed</td>
      <td>success</td>
    </tr>
    <tr>
      <td>installNGHDL</td>
      <td>success</td>
      <td>success</td>
    </tr>
    <tr>
      <td>createConfigFile</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>createSoftLink</td>
      <td>-</td>
      <td>-</td>
    </tr>
  </tbody>
</table>


## Conclusion 
Only GHDL compilation failed .  otherwise 
All other errors are fixed 









