#!/usr/bin/env sh

if [ -z "$SSH_KEY" ]; then
  echo "::error ::You need to set the SSH_KEY secret"
  exit 1
fi

chmod 777 "$GITHUB_WORKSPACE"

node scripts/index.js
jekyll build

KEY_FILE="$HOME/key"
echo "$SSH_KEY" > "$KEY_FILE"
chmod 400 "$KEY_FILE"
rsync -e "ssh -i $KEY_FILE -o StrictHostKeyChecking=no" -a --delete _site/ "$DESTINATION"
