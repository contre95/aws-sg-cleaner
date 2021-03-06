 #!/usr/bin/env bash

# lists all unused AWS security groups.
# a group is considered unused if it's not attached to any network interface.
# requires aws-cli and jq.

 #all groups
aws ec2 describe-security-groups \
  | jq --raw-output '.SecurityGroups[] | [.GroupName, .GroupId] | @tsv' \
  | sort > /tmp/sg.all

 #groups in use
aws ec2 describe-network-interfaces \
  | jq --raw-output '.NetworkInterfaces[].Groups[] | [.GroupName, .GroupId] | @tsv' \
  | sort \
  | uniq > /tmp/sg.in.use

diff /tmp/sg.all /tmp/sg.in.use |grep "<" |cut -d ' ' -f2-3
