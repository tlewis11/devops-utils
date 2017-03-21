playbook_name="$1"
playbook_file="applications/${playbook_name}/install.yml"
#check args
if [ $# -ne 1 ]
then
  echo "Usage: run_playbook.sh profile_name"
  exit 1
fi

ansible-playbook -i "localhost," -c local $playbook_file 
