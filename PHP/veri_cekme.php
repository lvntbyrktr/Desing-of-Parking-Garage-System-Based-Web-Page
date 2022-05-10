<?php
$connect=new PDO("mysql:host=localhost;dbname=database_name;charset=utf8","user_name","password");
$arr = $connect->query("SELECT * FROM database_table ORDER BY id DESC LIMIT 1",PDO::FETCH_ASSOC);
$data = $arr->fetch();
echo json_encode($data);
?>