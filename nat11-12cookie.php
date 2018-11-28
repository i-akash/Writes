<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <?php

    $defaultdata = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");

    function xor_encrypt($in) {
        $key = "qw8j";
        $text = $in;
        $outText = '';

        for($i=0;$i<strlen($text);$i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
        }
        return $outText;
    }

    function getCookie($d) {
        $key= base64_encode(xor_encrypt(json_encode($d)));
        echo $key;
    }
    getCookie($defaultdata);

    ?>
  </body>
</html>
