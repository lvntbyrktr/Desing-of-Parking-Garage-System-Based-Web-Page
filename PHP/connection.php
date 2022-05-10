<?php 

try{
$connect=new PDO("mysql:host=localhost;dbname=database_name;charset=utf8","user_name","password");
if($connect){
    
}
else{
    echo "error";
}
}
catch (PDOException $e)
    {
        echo "Error".$e;
    }

?>