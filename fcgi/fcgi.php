#!/usr/bin/env php
<?php
error_reporting(~E_WARNING);

require('fastcgi.php');

$sock_path = "/services/.sock/*.fpm.sock"; // For FastCGI Unix Socket scanning.
$port_list = array(9000,10000);            // For FastCGI Network port scanning.

$params = array(
    'GATEWAY_INTERFACE' => 'FastCGI/1.0',
    'REQUEST_METHOD'    => 'GET',
    'SCRIPT_FILENAME'   => '/fpm.status',
    'SCRIPT_NAME'       => '/fpm.status',
    'QUERY_STRING'      => 'full&json',
    'SERVER_SOFTWARE'   => 'php/fcgiclient',
    'SERVER_PROTOCOL'   => 'HTTP/1.1',
    'CONTENT_LENGTH'    => 0
);

$json = array();

foreach (glob($sock_path) as $filename) {
    $client = new FCGIClient('unix://'.$filename,-1);
    $content = $client->request($params, false);
    $ex = explode("\n", $content);
    array_push($json,$ex[count($ex)-1]);
}

foreach ($port_list as $port) {
    try {
        $client = new FCGIClient('localhost',$port);
        $content = $client->request($params, false);
        $ex = explode("\n", $content);
        array_push($json,$ex[count($ex)-1]);
    } catch (Exception $e) { }
}

echo '['.implode(',',$json) . ']';

return 0;
