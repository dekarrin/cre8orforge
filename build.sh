#!/bin/bash

# use pyinstaller to create the executable
#
#
# make shore you have done `pip install -U pyinstaller` before running this!

set -e

cd "$(dirname "$0")"
cur_version="$(./cf.sh version)"

# pyinstaller REQUIRES using the correct pathsep
on_windows=
case "$(uname -a)" in
  *CYGWIN*)
    on_windows=1
    ;;
  *MINGW64*)
    on_windows=1
    ;;
esac

if [[ -n "$on_windows" ]]
then
  pathsep=';'
else
  pathsep=':'
fi

pyinstaller launchgui.py --name cre8orforge -y \
  --add-data cre8/components/warning.png${pathsep}assets

cd dist
mv cre8orforge cre8
full_folder="cre8orforge-v${cur_version}"
rm -rf "$full_folder"
mkdir "$full_folder"
mv cre8 "$full_folder/cre8orforge"

cat << EOF > "$full_folder/TESTER-README.md"
Hey! Thanks for volunteering to help test cre8forge.

To start it, open the cre8orforge folder and run cre8orforge.exe.

You can launch a silly tutorial on how the game works using the 'Tutorial' button
on the main window that pops up.

To report a problem, please take the debug.log file and send it to @dekarrin#0413 on discord
or create a new issue on the [GitHub Issues Page](https://github.com/dekarrin/cre8orforge/issues/new)
for the project. Please be shore to include your operating system as well as what you did when
the issue happened.

Thanks again!
EOF

tar czf "${full_folder}.tar.gz" "$full_folder"

rm -rf "$full_folder"

echo "dist/${full_folder}.tar.gz"
