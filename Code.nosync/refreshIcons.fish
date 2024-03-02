#!/opt/homebrew/bin/fish

for file in ../**.webloc
          set -xl tmpicon "/tmp/"(/usr/bin/uuidgen)".png"
          set -x domain (/usr/libexec/PlistBuddy -c "Print :URL" "$file")
          /usr/bin/curl "https://t0.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=$domain&size=256" -o "$tmpicon"
          seticon "$tmpicon" "$file"
          rm "$tmpicon"
 end
