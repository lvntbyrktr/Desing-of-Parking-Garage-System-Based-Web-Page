<?php 
   include('connection.php'); // Include the code containing the $connect variable to connect to the database

   if(isset($_POST['gas'])){ // It checks whether there is gas data from Raspberry Pi, if there is other data, it will pull the values ​​in the database and update it
    $fetchData = $connect->query("SELECT * FROM database_table ORDER BY id LIMIT 1");
    $data = $fetchData->fetch();
    // If there are gas, distance and light values in the incoming $_POST data, use it, otherwise use the old values from the database.
    $gas = isset($_POST['gas']) ? $_POST['gas'] : $data["gas"];
    $ldr = isset($_POST['light']) ? $_POST['light'] : $data["ldr"];
    $ult = isset($_POST['ult']) ? $_POST['ult'] : $data["ult"];
    // Update values in database
    $updateData = $connect->prepare("INSERT INTO database_table (gas, light, mesafe) VALUES ('$gas', '$ldr', '$ult')");
    $updateData->execute(array());
    
   }

?>