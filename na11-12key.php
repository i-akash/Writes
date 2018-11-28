<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <?php

    $defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

    function xor_encrypt($in) {
        $key = base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSRHsLQk4KaAw%3D");
        $text = $in;
        $outText = '';

        for($i=0;$i<strlen($text);$i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
        }
        return $outText;
    }

    function getkey($d) {
        $key=xor_encrypt(json_encode($d));
        echo $key;
    }
    getkey($defaultdata);

    ?>
  </body>
</html>
