read st

if [[ $st = "Y" ]] || [[ $st = "y" ]]
then
    echo "YES"
elif [[ $st = "n" ]] || [[ $st = "N" ]]
then
    echo "NO"
fi
