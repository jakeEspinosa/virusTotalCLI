<h1>virusTotalCLI</h1>

<h2>Description</h2>
Check if files show up as malicious in VirusTotal straight from the command line! This simple script can be<br>
used on Windows, macOS, or Linux systems to determine if a file is malicious without having to launch the GUI.

<h2>How to Use</h2>
Launch the program from either the CLI or the GUI, enter the absolute path to the suspect file, and press enter.<br>
If a response code of 0 is returned, then the file is not malicious according to VirusTotal. If a response code<br>
of 1 is returned, then the file is malicious.

<h2>Technologies Used</h2>

- Python3 (with standard libraries)<br>
- VirusTotal Python API<br>

<h2>Platforms</h2>

- Windows 10<br>
- macOS<br>
- Linux<br>

<h2>Screenshots</h2>

<p align="center">
On Ubuntu Linux with a non-malicious file:<br>
<img src="https://imgur.com/fXWMlgU.png" height="80%" width="80%" alt="Program Walkthrough"/>
<br />
<br />
On Windows 10 with a malicious file:<br>
<img src="https://imgur.com/JqfiDYk.png" height="80%" width="80%" alt="Program Walkthrough"/>
<br />
<br />
