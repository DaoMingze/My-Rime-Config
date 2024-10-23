Copy-Item -Path "raw\rime-ice\cn_dicts" -Destination "dict\" -Recurse -Force
Copy-Item -Path "raw\rime-ice\en_dicts" -Destination "dict\" -Recurse -Force

Copy-Item -Path "raw\rime-ice\opencc" -Destination "basic\" -Recurse -Force
Copy-Item -Path "raw\rime-ice\lua" -Destination "basic\" -Recurse -Force
Copy-Item -Path "raw\rime-ice\rime.lua" -Destination "basic\" -Force
Copy-Item -Path "raw\rime-ice\default.yaml" -Destination "basic\" -Force
Copy-Item -Path "raw\rime-ice\squirrel.yaml" -Destination "theme\" -Force
Copy-Item -Path "raw\rime-ice\weasel.yaml" -Destination "theme\" -Force


Copy-Item -Path "raw\rime-ice\*.schema.yaml" -Destination "\schema" -Force
Copy-Item -Path "raw\rime-ice\*.dict.yaml" -Destination "\dict" -Force

Copy-Item -Path "raw\rime-ice\custom_phrase.txt" -Destination "\custom" -Force


