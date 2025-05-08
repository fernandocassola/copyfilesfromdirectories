### Copy Files from Sub Directories
This application allows you to copy all the files in subdirectories from a base directory to another directory.
It responds to the way moodle downloads assignments. Each student has a sub-directory, which forces us to copy everything one by one.
With this approach, as well as copying all the files to a single directory, it also renames each file with the student's name.
ATTENTION: the names of the subdirectories can be changed to the location indicated or can be passed as parameters

## RUN
# option A
: python copyFiles.py "C:\source" "C:\destination"
# option B (uses default dyrectories)
: python copyFiles.py 

# author: Fernando Cassola (maio 2025)
