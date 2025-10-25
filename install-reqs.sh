#!/bin/bash

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo "Linux core.."
elif [[ "$OSTYPE" == "darwin"* ]]; then
        echo "Mac core.."
elif [[ "$OSTYPE" == "cygwin" ]]; then
        echo "WSL core.."
elif [[ "$OSTYPE" == "msys" ]]; then
        echo "Msys core.."
elif [[ "$OSTYPE" == "win32" ]]; then
        echo "How did you get a shell working on Windows?.."
        echo "Sadly i cant really install anything from here"
        exit 1
elif [[ "$OSTYPE" == "freebsd"* ]]; then
        echo "FreeBSD core.."
else
        echo "Unkown base, cannot install requirements.."
        exit 1
fi
   