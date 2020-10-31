param (
    [Parameter(Mandatory=$true)]
    [string]$ip,
    [Parameter(Mandatory=$true)]
    [string]$p
)

$ipValidity = $ip -as [ipaddress] -as [Bool]


if ($p -match '-'){
    [int32[]] $temp = $p.Split("-")

    $ports = $temp[0] .. $temp[1]   
}
else{
    $ports = $p.Split(",")
}


if (!$ipValidity){
    write-output "Invalid IP"
}
else{
    foreach($port in $ports){   
        try{
            $socket = new-object System.Net.Sockets.TcpClient($ipAddresses, $port)
            $socket.Close()

            write-host "$port is open"
            
        } Catch [System.Net.Sockets.SocketException]{
            
        }
    }
}

